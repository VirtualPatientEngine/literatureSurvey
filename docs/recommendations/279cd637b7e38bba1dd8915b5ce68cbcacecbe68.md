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
  <i class="footer">This page was last updated on 2026-03-16 06:42:01 UTC</i>
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
          <td>ArXiv, DBLP, MAG</td>
          <td>139</td>
          <td>96</td>
        </tr>
    
        <tr id="World modelling is essential for understanding and predicting the dynamics of complex systems by learning both spatial and temporal dependencies. However, current frameworks, such as Transformers and selective state-space models like Mambas, exhibit limitations in efficiently encoding spatial and temporal structures, particularly in scenarios requiring long-term high-dimensional sequence modelling. To address these issues, we propose a novel recurrent framework, the \textbf{FACT}ored \textbf{S}tate-space (\textbf{FACTS}) model, for spatial-temporal world modelling. The FACTS framework constructs a graph-structured memory with a routing mechanism that learns permutable memory representations, ensuring invariance to input permutations while adapting through selective state-space propagation. Furthermore, FACTS supports parallel computation of high-dimensional sequences. We empirically evaluate FACTS across diverse tasks, including multivariate time series forecasting, object-centric world modelling, and spatial-temporal graph prediction, demonstrating that it consistently outperforms or matches specialised state-of-the-art models, despite its general-purpose world modelling design.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/ec840755867d3f5cf175cb57de963f042297f4ef" target='_blank'>FACTS: A Factored State-Space Framework For World Modelling</a></td>
          <td>
            Nanbo Li, Firas Laakom, Yucheng Xu, Wenyi Wang, Jurgen Schmidhuber
          </td>
          <td>2024-10-28</td>
          <td>ArXiv</td>
          <td>2</td>
          <td>8</td>
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
          <td>41</td>
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
          <td>30</td>
        </tr>
    
        <tr id="Real-world dynamical systems often consist of multiple stochastic subsystems that interact with each other. Modeling and forecasting the behavior of such dynamics are generally not easy, due to the inherent hardness in understanding the complicated interactions and evolutions of their constituents. This paper introduces the relational state-space model (R-SSM), a sequential hierarchical latent variable model that makes use of graph neural networks (GNNs) to simulate the joint state transitions of multiple correlated objects. By letting GNNs cooperate with SSM, R-SSM provides a flexible way to incorporate relational information into the modeling of multi-object dynamics. We further suggest augmenting the model with normalizing flows instantiated for vertex-indexed random variables and propose two auxiliary contrastive objectives to facilitate the learning. The utility of R-SSM is empirically evaluated on synthetic and real time series datasets.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/7a1e5377b08489c2969f73c56efc557e34f578e1" target='_blank'>Relational State-Space Model for Stochastic Multi-Object Systems</a></td>
          <td>
            Fan Yang, Ling Chen, Fan Zhou, Yusong Gao, Wei Cao
          </td>
          <td>2020-01-13</td>
          <td>ArXiv</td>
          <td>8</td>
          <td>74</td>
        </tr>
    
        <tr id="Interactive systems are omnipresent across various domains, ranging from dynamic systems in physics to intricate societal dynamics. Relational inference aims to uncover implicit interactions between components based on observed system trajectories. Existing neural relational inference methods rely on fully connected graphs for message passing, leading to computational inefficiency and redundant message passing. While Transformer-based models excel in multivariate time series forecasting, their contextual attention mechanism disrupts the integrity and independence of dynamics in time-invariant relational inference. Besides, the implicit interactions should have non-trivial correlations with the attention coefficients, yet how to read out an explicit interaction graph from Transformer also still needs to be explored. In this study, we propose RIVA, a novel relational inference model with a variate attention mechanism. Unlike contextual attention in vanilla Transformer, which encodes multiple variables at the same time point as a single token, RIVA encodes entire dynamics. Furthermore, we incorporate the inferred graph structure as a mask in the causal attention, allowing each variable to effectively aggregate features from its neighbors and greatly enhancing the model's ability to capture complex interactions. Through extensive experimental evaluations, RIVA demonstrates superior performance in time-invariant continuous interaction inference and future state prediction, outperforming existing methods and providing highly accurate predictions in dynamic environments.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/cdd4e532084bbd68fd22c56f7abbec1ceaff28b1" target='_blank'>RIVA: Efficient relational inference with variate attention</a></td>
          <td>
            Ruizi Wu, Liming Pan, Linyuan Lu
          </td>
          <td>2025-06-01</td>
          <td>Neural networks : the official journal of the International Neural Network Society</td>
          <td>0</td>
          <td>6</td>
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
          <td>ArXiv, DBLP, MAG</td>
          <td>510</td>
          <td>53</td>
        </tr>
    
        <tr id="Probabilistic inference in high-dimensional state-space models is computationally challenging. For many spatiotemporal systems, however, prior knowledge about the dependency structure of state variables is available. We leverage this structure to develop a computationally efficient approach to state estimation and learning in graph-structured state-space models with (partially) unknown dynamics and limited historical data. Building on recent methods that combine ideas from deep learning with principled inference in Gaussian Markov random fields (GMRF), we reformulate graph-structured state-space models as Deep GMRFs defined by simple spatial and temporal graph layers. This results in a flexible spatiotemporal prior that can be learned efficiently from a single time sequence via variational inference. Under linear Gaussian assumptions, we retain a closed-form posterior, which can be sampled efficiently using the conjugate gradient method, scaling favourably compared to classical Kalman filter based approaches">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/66173ff04bc062987a4395181001bf9b7c3eb21b" target='_blank'>Deep Gaussian Markov Random Fields for Graph-Structured Dynamical Systems</a></td>
          <td>
            Fiona Lippert, B. Kranstauber, E. E. V. Loon, Patrick Forr'e
          </td>
          <td>2023-06-14</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>25</td>
        </tr>
    
        <tr id="Many applications, e.g., healthcare, education, call for effective methods methods for constructing predictive models from high dimensional time series data where the relationship between variables can be complex and vary over time. In such settings, the underlying system undergoes a sequence of unobserved transitions among a finite set of hidden states. Furthermore, the relationships between the observed variables and their temporal dynamics may depend on the hidden state of the system. To further complicate matters, the hidden state sequences underlying the observed data from different individuals may not be aligned relative to a common frame of reference. Against this background, we consider the novel problem of jointly learning the state-dependent inter-variable relationships as well as the pattern of transitions between hidden states from multi-variate time series data. To solve this problem, we introduce the State-Regularized Vector Autoregressive Model (SrVARM) which combines a state-regularized recurrent neural network to learn the dynamics of transitions between discrete hidden states with an augmented autoregressive model which models the inter-variable dependencies in each state using a state-dependent directed acyclic graph (DAG). We propose an efficient algorithm for training SrVARM by leveraging a recently introduced reformulation of the combinatorial problem of optimizing the DAG structure with respect to a scoring function into a continuous optimization problem. We report results of extensive experiments with simulated data as well as a real-world benchmark that show that SrVARM outperforms state-of-the-art baselines in recovering the unobserved state transitions and discovering the state-dependent relationships among variables.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/4ddaa0ff15691ba148dd88c82b03547e9d2aa013" target='_blank'>SrVARM: State Regularized Vector Autoregressive Model for Joint Learning of Hidden State Transitions and State-Dependent Inter-Variable Dependencies from Multi-variate Time Series</a></td>
          <td>
            Tsung-Yu Hsieh, Yiwei Sun, Xianfeng Tang, Suhang Wang, Vasant G Honavar
          </td>
          <td>2021-04-19</td>
          <td>Proceedings of the Web Conference 2021</td>
          <td>9</td>
          <td>57</td>
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