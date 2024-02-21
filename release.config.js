const package_name = "demo"

const config = {
    branches: ['main'],
    plugins: [
      '@semantic-release/commit-analyzer',
      '@semantic-release/release-notes-generator',
    ["@semantic-release/exec", {
      "prepareCmd": "echo ${nextRelease.version} > release_version.txt ; python3 setup.py bdist_wheel --dist-dir dist/ ; mv dist/*-${nextRelease.version}-*whl dist/"+package_name+"-latest-py3-none-any.whl",
        }],
      ["@semantic-release/git", {
        "assets": ["dist/"+package_name+"-latest-py3-none-any.whl"],
      }],
        [
          "@semantic-release/github",
          {
            "assets": [
              {
                "path": "dist/"+package_name+"-latest-py3-none-any.whl",
                "label": package_name+"-${nextRelease.version}",
                "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
              }
            ]
          }
        ],
    ]
  };
  
  module.exports = config;
