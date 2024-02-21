const package_name = "demo"

const config = {
    branches: ['main'],
    plugins: [
      '@semantic-release/commit-analyzer',
      '@semantic-release/release-notes-generator',
    ["@semantic-release/exec", {
      // "publishCmd": "echo 'RELEASE_VERSION=${nextRelease.version}' >> $GITHUB_ENV && echo ${nextRelease.version} > release_version.txt",
      // "prepareCmd": "echo ${nextRelease.version} > release_version.txt ; python3 setup.py bdist_wheel --dist-dir dist/ ; mv dist/*-${nextRelease.version}-*whl dist/gurdeep-demo.whl",
      // "publishCmd": "echo 'RELEASE_VERSION=${nextRelease.version}' > release_version.txt",
      // "prepareCmd": "python3 setup.py bdist_wheel --dist-dir dist/",
      "prepareCmd": "echo ${nextRelease.version} > release_version.txt ; python3 setup.py bdist_wheel --dist-dir dist/ ; mv dist/*-${nextRelease.version}-*whl dist/"+package_name+"-latest-py3-none-any.whl",
        }],
      ["@semantic-release/git", {
        // "assets": ["dist/*.js", "dist/*.js.map"],
        // "assets": ["dist/gurdeep-demo.whl"],
        // "assets": ["dist/gurdeepdemo-${nextRelease.version}-py3-none-any.whl"],
        "assets": ["dist/"+package_name+"-latest-py3-none-any.whl"],
      }],
      
      // '@semantic-release/github'
        [
          "@semantic-release/github",
          {
            "assets": [
              {
                // "path": "dist/gurdeep-demo.whl",
                // "path": "dist/gurdeep-demo-${nextRelease.version}-*whl",
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
