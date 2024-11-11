---
hide:
 - navigation
---
<!DOCTYPE html>
#
<html lang="en">
<head>
  <meta charset="utf-8">
</head>

<body>
  <p>
  <i class="footer">This page was last updated on 2024-11-11 06:05:51 UTC</i>
  </p>
  
  <div class="note info" onclick="startIntro()">
    <p>
      <button type="button" class="buttons">
        <div style="display: flex; align-items: center;">
        Click here for a quick intro of the page! <i class="material-icons">help</i>
        </div>
      </button>
    </p>
  </div>

  <p>
  <h3 data-intro='Recommendations for the article'>
    Recommendations for the article <i>Data-driven discovery of partial differential equations</i>
  </h3>
  <table id="table1" class="display wrap" style="width:100%">
  <thead>
    <tr>
        <th data-intro='Click to view the abstract (if available)'>Abstract</th>
        <th>Title</th>
        <th>Authors</th>
        <th>Publication Date</th>
        <th>Journal/ Conference</th>
        <th>Citation count</th>
        <th data-intro='Highest h-index among the authors'>Highest h-index</th>
    </tr>
  </thead>
  <tbody>
    
        <tr id="This study presents a general framework, namely, Sparse Spatiotemporal System Discovery (S3d), for discovering dynamical models given by Partial Differential Equations (PDEs) from spatiotemporal data. S3d is built on the recent development of sparse Bayesian learning, which enforces sparsity in the estimated PDEs. This approach enables a balance between model complexity and fitting error with theoretical guarantees. The proposed framework integrates Bayesian inference and a sparse priori distribution with the sparse regression method. It also introduces a principled iterative re-weighted algorithm to select dominant features in PDEs and solve for the sparse coefficients. We have demonstrated the discovery of the complex Ginzburg-Landau equation from a traveling-wave convection experiment, as well as several other PDEs, including the important cases of Navier-Stokes and sine-Gordon equations, from simulated data.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/a28eb9166ed38ff571770f8d6cb1558b0089e507" target='_blank'>Machine discovery of partial differential equations from spatiotemporal data: A sparse Bayesian learning framework.</a></td>
          <td>
            Ye Yuan, Xiuting Li, Liang Li, Frank J. Jiang, Xiuchuan Tang, Fumin Zhang, Jorge Gonçalves, Henning U. Voss, Han Ding, Jürgen Kurths
          </td>
          <td>2023-11-01</td>
          <td>Chaos</td>
          <td>4</td>
          <td>11</td>
        </tr>
    
        <tr id="The study presents a general framework for discovering underlying Partial Differential Equations (PDEs) using measured spatiotemporal data. The method, called Sparse Spatiotemporal System Discovery ($\text{S}^3\text{d}$), decides which physical terms are necessary and which can be removed (because they are physically negligible in the sense that they do not affect the dynamics too much) from a pool of candidate functions. The method is built on the recent development of Sparse Bayesian Learning; which enforces the sparsity in the to-be-identified PDEs, and therefore can balance the model complexity and fitting error with theoretical guarantees. Without leveraging prior knowledge or assumptions in the discovery process, we use an automated approach to discover ten types of PDEs, including the famous Navier-Stokes and sine-Gordon equations, from simulation data alone. Moreover, we demonstrate our data-driven discovery process with the Complex Ginzburg-Landau Equation (CGLE) using data measured from a traveling-wave convection experiment. Our machine discovery approach presents solutions that has the potential to inspire, support and assist physicists for the establishment of physical laws from measured spatiotemporal data, especially in notorious fields that are often too complex to allow a straightforward establishment of physical law, such as biophysics, fluid dynamics, neuroscience or nonlinear optics.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/85835648e0d92d2b6115a66525b1f5d54af4f83e" target='_blank'>Machine Discovery of Partial Differential Equations from Spatiotemporal Data</a></td>
          <td>
            Ye Yuan, Junlin Li, Liang Li, Frank Jiang, Xiuchuan Tang, Fumin Zhang, Sheng Liu, J. Gonçalves, H. Voss, Xiuting Li, J. Kurths, Han Ding
          </td>
          <td>2019-09-15</td>
          <td>ArXiv</td>
          <td>9</td>
          <td>107</td>
        </tr>
    
        <tr id="Significance Understanding dynamic constraints and balances in nature has facilitated rapid development of knowledge and enabled technology, including aircraft, combustion engines, satellites, and electrical power. This work develops a novel framework to discover governing equations underlying a dynamical system simply from data measurements, leveraging advances in sparsity techniques and machine learning. The resulting models are parsimonious, balancing model complexity with descriptive ability while avoiding overfitting. There are many critical data-driven problems, such as understanding cognition from neural recordings, inferring climate patterns, determining stability of financial markets, predicting and suppressing the spread of disease, and controlling turbulence for greener transportation and energy. With abundant data and elusive laws, data-driven discovery of dynamics will continue to play an important role in these efforts. Extracting governing equations from data is a central challenge in many diverse areas of science and engineering. Data are abundant whereas models often remain elusive, as in climate science, neuroscience, ecology, finance, and epidemiology, to name only a few examples. In this work, we combine sparsity-promoting techniques and machine learning with nonlinear dynamical systems to discover governing equations from noisy measurement data. The only assumption about the structure of the model is that there are only a few important terms that govern the dynamics, so that the equations are sparse in the space of possible functions; this assumption holds for many physical systems in an appropriate basis. In particular, we use sparse regression to determine the fewest terms in the dynamic governing equations required to accurately represent the data. This results in parsimonious models that balance accuracy with model complexity to avoid overfitting. We demonstrate the algorithm on a wide range of problems, from simple canonical systems, including linear and nonlinear oscillators and the chaotic Lorenz system, to the fluid vortex shedding behind an obstacle. The fluid example illustrates the ability of this method to discover the underlying dynamics of a system that took experts in the community nearly 30 years to resolve. We also show that this method generalizes to parameterized systems and systems that are time-varying or have external forcing.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/5d150cec2775f9bc863760448f14104cc8f42368" target='_blank'>Discovering governing equations from data by sparse identification of nonlinear dynamical systems</a></td>
          <td>
            S. Brunton, J. Proctor, J. Kutz
          </td>
          <td>2015-09-11</td>
          <td>Proceedings of the National Academy of Sciences</td>
          <td>3408</td>
          <td>67</td>
        </tr>
    
        <tr id="None">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/1f18c5206491626d36c2271aaf491dbc945f6247" target='_blank'>Automatically discovering ordinary differential equations from data with sparse regression</a></td>
          <td>
            Kevin Egan, Weizhen Li, Rui Carvalho
          </td>
          <td>2024-01-09</td>
          <td>Communications Physics</td>
          <td>11</td>
          <td>2</td>
        </tr>
    
        <tr id="None">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/e596988b1df3a0bc78bf72c0bfdb21c85eaab6c9" target='_blank'>Physics-informed learning of governing equations from scarce data</a></td>
          <td>
            Zhao Chen, Yang Liu, Hao Sun
          </td>
          <td>2020-05-05</td>
          <td>Nature Communications</td>
          <td>289</td>
          <td>13</td>
        </tr>
    
        <tr id="Discovering the partial differential equations underlying spatio-temporal datasets from very limited and highly noisy observations is of paramount interest in many scientific fields. However, it remains an open question to know when model discovery algorithms based on sparse regression can actually recover the underlying physical processes. In this work, we show the design matrices used to infer the equations by sparse regression can violate the irrepresentability condition (IRC) of the Lasso, even when derived from analytical PDE solutions (i.e. without additional noise). Sparse regression techniques which can recover the true underlying model under violated IRC conditions are therefore required, leading to the introduction of the randomised adaptive Lasso. We show once the latter is integrated within the deep learning model discovery framework DeepMod, a wide variety of nonlinear and chaotic canonical PDEs can be recovered: (1) up to $\mathcal{O}(2)$ higher noise-to-sample ratios than state-of-the-art algorithms, (2) with a single set of hyperparameters, which paves the road towards truly automated model discovery.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/45633bde87d3fecdb0ef577036f2465e70c51f24" target='_blank'>Sparsistent Model Discovery</a></td>
          <td>
            Georges Tod, G. Both, R. Kusters
          </td>
          <td>2021-06-22</td>
          <td>ArXiv</td>
          <td>1</td>
          <td>13</td>
        </tr>
    
        <tr id="We investigate the problem of learning an evolution equation directly from some given data. This work develops a learning algorithm to identify the terms in the underlying partial differential equations and to approximate the coefficients of the terms only using data. The algorithm uses sparse optimization in order to perform feature selection and parameter estimation. The features are data driven in the sense that they are constructed using nonlinear algebraic equations on the spatial derivatives of the data. Several numerical experiments show the proposed method's robustness to data noise and size, its ability to capture the true features of the data, and its capability of performing additional analytics. Examples include shock equations, pattern formation, fluid flow and turbulence, and oscillatory convection.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/29fd552660768b191c36d16894faee7db5f18949" target='_blank'>Supplementary material from "Learning partial differential equations via data discovery and sparse optimization"</a></td>
          <td>
            Hayden Schaeffer
          </td>
          <td>2017-01-16</td>
          <td></td>
          <td>0</td>
          <td>16</td>
        </tr>
    
        <tr id="We propose a regression method based upon group sparsity that is capable of discovering parametrized governing dynamical equations of motion of a given system by time series measurements. The method balances model complexity and regression accuracy by selecting a parsimonious model via Pareto analysis. This gives a promising new technique for disambiguating governing equations from simple parametric dependencies in physical, biological and engineering systems.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/a8bbfc159dd6951e50e366daa7359626873aec45" target='_blank'>Data-Driven discovery of governing physical laws and their parametric dependencies in engineering, physics and biology</a></td>
          <td>
            J. Kutz, Samuel H. Rudy, A. Alla, S. Brunton
          </td>
          <td>2017-12-01</td>
          <td>2017 IEEE 7th International Workshop on Computational Advances in Multi-Sensor Adaptive Processing (CAMSAP)</td>
          <td>12</td>
          <td>67</td>
        </tr>
    
  </tbody>
  <tfoot>
    <tr>
        <th>Abstract</th>
        <th>Title</th>
        <th>Authors</th>
        <th>Publication Date</th>
        <th>Journal/Conference</th>
        <th>Citation count</th>
        <th>Highest h-index</th>
    </tr>
  </tfoot>
  </table>
  </p>

</body>

<script>
var dataTableOptions = {
        initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                let column = this;
 
                // Create select element
                let select = document.createElement('select');
                select.add(new Option(''));
                column.footer().replaceChildren(select);
 
                // Apply listener for user change in value
                select.addEventListener('change', function () {
                    column
                        .search(select.value, {exact: true})
                        .draw();
                });

                // keep the width of the select element same as the column
                select.style.width = '100%';
 
                // Add list of options
                column
                    .data()
                    .unique()
                    .sort()
                    .each(function (d, j) {
                        select.add(new Option(d));
                    });
            });
    },
    scrollX: false,
    scrollCollapse: true,
    paging: true,
    fixedColumns: true,
    columnDefs: [
        {"className": "dt-center", "targets": "_all"},
        // set width for both columns 0 and 1 as 25%
        { width: '5%', targets: 0 },
        { width: '25%', targets: 1 },
        { width: '20%', targets: 2 },
        { width: '10%', targets: 3 },
        { width: '20%', targets: 4 }

      ],
    pageLength: 10,
    layout: {
        topStart: {
            buttons: ['copy', 'csv', 'excel', 'pdf', 'print']
        }
    }
  }
  new DataTable('#table1', dataTableOptions);
  
  var table = $('#table1').DataTable();
  $('#table1 tbody').on('click', 'td:first-child', function () {
    var tr = $(this).closest('tr');
    var row = table.row( tr );

    var rowId = tr.attr('id');
    // alert(rowId);

    if (row.child.isShown()) {
      // This row is already open - close it.
      row.child.hide();
      tr.removeClass('shown');
      tr.find('td:first-child').html('<i class="material-icons">visibility_off</i>');
    } else {
      // Open row.
      // row.child('foo').show();
      var content = '<div class="child-row-content"><strong>Abstract:</strong> ' + rowId + '</div>';
      row.child(content).show();
      tr.addClass('shown');
      tr.find('td:first-child').html('<i class="material-icons">visibility</i>');
    }
  });
</script>
<style>
  .child-row-content {
    text-align: justify;
    text-justify: inter-word;
    word-wrap: break-word; /* Ensure long words are broken */
    white-space: normal; /* Ensure text wraps to the next line */
    max-width: 100%; /* Ensure content does not exceed the table width */
    padding: 10px; /* Optional: add some padding for better readability */
    /* font size */
    font-size: small;
  }
</style>
</html>