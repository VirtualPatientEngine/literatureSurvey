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
  <i class="footer">This page was last updated on 2024-07-15 06:04:57 UTC</i>
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
    Recommendations for the article <i>Graph state-space models</i>
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
    
        <tr id="State-space models (SSMs) are a highly expressive model class for learning patterns in time series data and for system identification. Deterministic versions of SSMs (e.g. LSTMs) proved extremely successful in modeling complex time series data. Fully probabilistic SSMs, however, are often found hard to train, even for smaller problems. To overcome this limitation, we propose a novel model formulation and a scalable training algorithm based on doubly stochastic variational inference and Gaussian processes. In contrast to existing work, the proposed variational approximation allows one to fully capture the latent state temporal correlations. These correlations are the key to robust training. The effectiveness of the proposed PR-SSM is evaluated on a set of real-world benchmark datasets in comparison to state-of-the-art probabilistic model learning methods. Scalability and robustness are demonstrated on a high dimensional problem.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/408570c02ba213a856bc8186c62a4e5bf91a18de" target='_blank'>Probabilistic Recurrent State-Space Models</a></td>
          <td>
            Andreas Doerr, Christian Daniel, Martin Schiegg, D. Nguyen-Tuong, S. Schaal, Marc Toussaint, Sebastian Trimpe
          </td>
          <td>2018-01-31</td>
          <td>MAG, ArXiv, DBLP</td>
          <td>108</td>
          <td>93</td>
        </tr>
    
        <tr id="We introduce a new version of deep state-space models (DSSMs) that combines a recurrent neural network with a state-space framework to forecast time series data. The model estimates the observed series as functions of latent variables that evolve non-linearly through time. Due to the complexity and non-linearity inherent in DSSMs, previous works on DSSMs typically produced latent variables that are very difficult to interpret. Our paper focus on producing interpretable latent parameters with two key modifications. First, we simplify the predictive decoder by restricting the response variables to be a linear transformation of the latent variables plus some noise. Second, we utilize shrinkage priors on the latent variables to reduce redundancy and improve robustness. These changes make the latent variables much easier to understand and allow us to interpret the resulting latent variables as random effects in a linear mixed model. We show through two public benchmark datasets the resulting model improves forecasting performances.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/b5d92a67cb7adb40d982df2f6fb6c8669d34604b" target='_blank'>Interpretable Latent Variables in Deep State Space Models</a></td>
          <td>
            Haoxuan Wu, David S. Matteson, M. Wells
          </td>
          <td>2022-03-03</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>40</td>
        </tr>
    
        <tr id="Time series with long-term structure arise in a variety of contexts and capturing this temporal structure is a critical challenge in time series analysis for both inference and forecasting settings. Traditionally, state space models have been successful in providing uncertainty estimates of trajectories in the latent space. More recently, deep learning, attention-based approaches have achieved state of the art performance for sequence modeling, though often require large amounts of data and parameters to do so. We propose Stanza, a nonlinear, non-stationary state space model as an intermediate approach to fill the gap between traditional models and modern deep learning approaches for complex time series. Stanza strikes a balance between competitive forecasting accuracy and probabilistic, interpretable inference for highly structured time series. In particular, Stanza achieves forecasting accuracy competitive with deep LSTMs on real-world datasets, especially for multi-step ahead forecasting.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/9c619e58d073772ff298228d47afcab625c7f37a" target='_blank'>Stanza: A Nonlinear State Space Model for Probabilistic Inference in Non-Stationary Time Series</a></td>
          <td>
            Anna K. Yanchenko, S. Mukherjee
          </td>
          <td>2020-06-11</td>
          <td>ArXiv</td>
          <td>6</td>
          <td>31</td>
        </tr>
    
        <tr id="Outstanding achievements of graph neural networks for spatiotemporal time series analysis show that relational constraints introduce an effective inductive bias into neural forecasting architectures. Often, however, the relational information characterizing the underlying data-generating process is unavailable and the practitioner is left with the problem of inferring from data which relational graph to use in the subsequent processing stages. We propose novel, principled - yet practical - probabilistic score-based methods that learn the relational dependencies as distributions over graphs while maximizing end-to-end the performance at task. The proposed graph learning framework is based on consolidated variance reduction techniques for Monte Carlo score-based gradient estimation, is theoretically grounded, and, as we show, effective in practice. In this paper, we focus on the time series forecasting problem and show that, by tailoring the gradient estimators to the graph learning problem, we are able to achieve state-of-the-art performance while controlling the sparsity of the learned graph and the computational scalability. We empirically assess the effectiveness of the proposed method on synthetic and real-world benchmarks, showing that the proposed solution can be used as a stand-alone graph identification procedure as well as a graph learning component of an end-to-end forecasting architecture.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/0d01d21137a5af9f04e4b16a55a0f732cb8a540b" target='_blank'>Sparse Graph Learning from Spatiotemporal Time Series</a></td>
          <td>
            Andrea Cini, Daniele Zambon, C. Alippi
          </td>
          <td>2022-05-26</td>
          <td>J. Mach. Learn. Res.</td>
          <td>10</td>
          <td>49</td>
        </tr>
    
        <tr id="Time series modeling is a well-established problem, which often requires that methods (1) expressively represent complicated dependencies, (2) forecast long horizons, and (3) efficiently train over long sequences. State-space models (SSMs) are classical models for time series, and prior works combine SSMs with deep learning layers for efficient sequence modeling. However, we find fundamental limitations with these prior approaches, proving their SSM representations cannot express autoregressive time series processes. We thus introduce SpaceTime, a new state-space time series architecture that improves all three criteria. For expressivity, we propose a new SSM parameterization based on the companion matrix -- a canonical representation for discrete-time processes -- which enables SpaceTime's SSM layers to learn desirable autoregressive processes. For long horizon forecasting, we introduce a"closed-loop"variation of the companion SSM, which enables SpaceTime to predict many future time-steps by generating its own layer-wise inputs. For efficient training and inference, we introduce an algorithm that reduces the memory and compute of a forward pass with the companion matrix. With sequence length $\ell$ and state-space size $d$, we go from $\tilde{O}(d \ell)$ na\"ively to $\tilde{O}(d + \ell)$. In experiments, our contributions lead to state-of-the-art results on extensive and diverse benchmarks, with best or second-best AUROC on 6 / 7 ECG and speech time series classification, and best MSE on 14 / 16 Informer forecasting tasks. Furthermore, we find SpaceTime (1) fits AR($p$) processes that prior deep SSMs fail on, (2) forecasts notably more accurately on longer horizons than prior state-of-the-art, and (3) speeds up training on real-world ETTh1 data by 73% and 80% relative wall-clock time over Transformers and LSTMs.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/a7d68b1702af08ce4dbbf2cd0b083e744ae5c6be" target='_blank'>Effectively Modeling Time Series with Simple Discrete State Spaces</a></td>
          <td>
            Michael Zhang, Khaled Kamal Saab, Michael Poli, Tri Dao, Karan Goel, Christopher Ré
          </td>
          <td>2023-03-16</td>
          <td>ArXiv</td>
          <td>27</td>
          <td>43</td>
        </tr>
    
        <tr id="
 
 Gaussian state space models have been used for decades as generative models of sequential data. They admit an intuitive probabilistic interpretation, have a simple functional form, and enjoy widespread adoption. We introduce a unified algorithm to efficiently learn a broad class of linear and non-linear state space models, including variants where the emission and transition distributions are modeled by deep neural networks. Our learning algorithm simultaneously learns a compiled inference network and the generative model, leveraging a structured variational approximation parameterized by recurrent neural networks to mimic the posterior distribution. We apply the learning algorithm to both synthetic and real-world datasets, demonstrating its scalability and versatility. We find that using the structured approximation to the posterior results in models with significantly higher held-out likelihood.
 
">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/2af17f153e3fd71e15db9216b972aef222f46617" target='_blank'>Structured Inference Networks for Nonlinear State Space Models</a></td>
          <td>
            R. G. Krishnan, Uri Shalit, D. Sontag
          </td>
          <td>2016-09-30</td>
          <td>MAG, ArXiv, DBLP</td>
          <td>420</td>
          <td>48</td>
        </tr>
    
        <tr id="Probabilistic inference in high-dimensional state-space models is computationally challenging. For many spatiotemporal systems, however, prior knowledge about the dependency structure of state variables is available. We leverage this structure to develop a computationally efficient approach to state estimation and learning in graph-structured state-space models with (partially) unknown dynamics and limited historical data. Building on recent methods that combine ideas from deep learning with principled inference in Gaussian Markov random fields (GMRF), we reformulate graph-structured state-space models as Deep GMRFs defined by simple spatial and temporal graph layers. This results in a flexible spatiotemporal prior that can be learned efficiently from a single time sequence via variational inference. Under linear Gaussian assumptions, we retain a closed-form posterior, which can be sampled efficiently using the conjugate gradient method, scaling favourably compared to classical Kalman filter based approaches">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/66173ff04bc062987a4395181001bf9b7c3eb21b" target='_blank'>Deep Gaussian Markov Random Fields for Graph-Structured Dynamical Systems</a></td>
          <td>
            Fiona Lippert, B. Kranstauber, E. E. V. Loon, Patrick Forr'e
          </td>
          <td>2023-06-14</td>
          <td>ArXiv</td>
          <td>1</td>
          <td>23</td>
        </tr>
    
        <tr id="Many applications, e.g., healthcare, education, call for effective methods methods for constructing predictive models from high dimensional time series data where the relationship between variables can be complex and vary over time. In such settings, the underlying system undergoes a sequence of unobserved transitions among a finite set of hidden states. Furthermore, the relationships between the observed variables and their temporal dynamics may depend on the hidden state of the system. To further complicate matters, the hidden state sequences underlying the observed data from different individuals may not be aligned relative to a common frame of reference. Against this background, we consider the novel problem of jointly learning the state-dependent inter-variable relationships as well as the pattern of transitions between hidden states from multi-variate time series data. To solve this problem, we introduce the State-Regularized Vector Autoregressive Model (SrVARM) which combines a state-regularized recurrent neural network to learn the dynamics of transitions between discrete hidden states with an augmented autoregressive model which models the inter-variable dependencies in each state using a state-dependent directed acyclic graph (DAG). We propose an efficient algorithm for training SrVARM by leveraging a recently introduced reformulation of the combinatorial problem of optimizing the DAG structure with respect to a scoring function into a continuous optimization problem. We report results of extensive experiments with simulated data as well as a real-world benchmark that show that SrVARM outperforms state-of-the-art baselines in recovering the unobserved state transitions and discovering the state-dependent relationships among variables.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/4ddaa0ff15691ba148dd88c82b03547e9d2aa013" target='_blank'>SrVARM: State Regularized Vector Autoregressive Model for Joint Learning of Hidden State Transitions and State-Dependent Inter-Variable Dependencies from Multi-variate Time Series</a></td>
          <td>
            Tsung-Yu Hsieh, Yiwei Sun, Xianfeng Tang, Suhang Wang, Vasant G Honavar
          </td>
          <td>2021-04-19</td>
          <td>Proceedings of the Web Conference 2021</td>
          <td>7</td>
          <td>54</td>
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