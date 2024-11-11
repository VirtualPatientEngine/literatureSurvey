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
  <i class="footer">This page was last updated on 2024-11-11 06:05:28 UTC</i>
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
          <td>ArXiv, MAG, DBLP</td>
          <td>113</td>
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
    
        <tr id="World modelling is essential for understanding and predicting the dynamics of complex systems by learning both spatial and temporal dependencies. However, current frameworks, such as Transformers and selective state-space models like Mambas, exhibit limitations in efficiently encoding spatial and temporal structures, particularly in scenarios requiring long-term high-dimensional sequence modelling. To address these issues, we propose a novel recurrent framework, the \textbf{FACT}ored \textbf{S}tate-space (\textbf{FACTS}) model, for spatial-temporal world modelling. The FACTS framework constructs a graph-structured memory with a routing mechanism that learns permutable memory representations, ensuring invariance to input permutations while adapting through selective state-space propagation. Furthermore, FACTS supports parallel computation of high-dimensional sequences. We empirically evaluate FACTS across diverse tasks, including multivariate time series forecasting and object-centric world modelling, demonstrating that it consistently outperforms or matches specialised state-of-the-art models, despite its general-purpose world modelling design.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/ec840755867d3f5cf175cb57de963f042297f4ef" target='_blank'>FACTS: A Factored State-Space Framework For World Modelling</a></td>
          <td>
            Li Nanbo, Firas Laakom, Yucheng Xu, Wenyi Wang, Jurgen Schmidhuber
          </td>
          <td>2024-10-28</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>7</td>
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
          <td>32</td>
        </tr>
    
        <tr id="Outstanding achievements of graph neural networks for spatiotemporal time series analysis show that relational constraints introduce an effective inductive bias into neural forecasting architectures. Often, however, the relational information characterizing the underlying data-generating process is unavailable and the practitioner is left with the problem of inferring from data which relational graph to use in the subsequent processing stages. We propose novel, principled - yet practical - probabilistic score-based methods that learn the relational dependencies as distributions over graphs while maximizing end-to-end the performance at task. The proposed graph learning framework is based on consolidated variance reduction techniques for Monte Carlo score-based gradient estimation, is theoretically grounded, and, as we show, effective in practice. In this paper, we focus on the time series forecasting problem and show that, by tailoring the gradient estimators to the graph learning problem, we are able to achieve state-of-the-art performance while controlling the sparsity of the learned graph and the computational scalability. We empirically assess the effectiveness of the proposed method on synthetic and real-world benchmarks, showing that the proposed solution can be used as a stand-alone graph identification procedure as well as a graph learning component of an end-to-end forecasting architecture.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/0d01d21137a5af9f04e4b16a55a0f732cb8a540b" target='_blank'>Sparse Graph Learning from Spatiotemporal Time Series</a></td>
          <td>
            Andrea Cini, Daniele Zambon, C. Alippi
          </td>
          <td>2022-05-26</td>
          <td>J. Mach. Learn. Res.</td>
          <td>14</td>
          <td>50</td>
        </tr>
    
        <tr id="Forecasting the behaviour of complex dynamical systems such as interconnected sensor networks characterized by high-dimensional multivariate time series(MTS) is of paramount importance for making informed decisions and planning for the future in a broad spectrum of applications. Graph forecasting networks(GFNs) are well-suited for forecasting MTS data that exhibit spatio-temporal dependencies. However, most prior works of GFN-based methods on MTS forecasting rely on domain-expertise to model the nonlinear dynamics of the system, but neglect the potential to leverage the inherent relational-structural dependencies among time series variables underlying MTS data. On the other hand, contemporary works attempt to infer the relational structure of the complex dependencies between the variables and simultaneously learn the nonlinear dynamics of the interconnected system but neglect the possibility of incorporating domain-specific prior knowledge to improve forecast accuracy. To this end, we propose a hybrid architecture that combines explicit prior knowledge with implicit knowledge of the relational structure within the MTS data. It jointly learns intra-series temporal dependencies and inter-series spatial dependencies by encoding time-conditioned structural spatio-temporal inductive biases to provide more accurate and reliable forecasts. It also models the time-varying uncertainty of the multi-horizon forecasts to support decision-making by providing estimates of prediction uncertainty. The proposed architecture has shown promising results on multiple benchmark datasets and outperforms state-of-the-art forecasting methods by a significant margin. We report and discuss the ablation studies to validate our forecasting architecture.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/05cd3afc8208f1c0dd61b09a90f35dd42497e175" target='_blank'>Multi-Knowledge Fusion Network for Time Series Representation Learning</a></td>
          <td>
            Sakhinana Sagar Srinivas, Shivam Gupta, Krishna Sai Sudhir Aripirala, Venkataramana Runkana
          </td>
          <td>2024-08-22</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>3</td>
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
          <td>60</td>
        </tr>
    
        <tr id="Over the past few years, research on deep graph learning has shifted from static graphs to temporal graphs in response to real-world complex systems that exhibit dynamic behaviors. In practice, temporal graphs are formalized as an ordered sequence of static graph snapshots observed at discrete time points. Sequence models such as RNNs or Transformers have long been the predominant backbone networks for modeling such temporal graphs. Yet, despite the promising results, RNNs struggle with long-range dependencies, while transformers are burdened by quadratic computational complexity. Recently, state space models (SSMs), which are framed as discretized representations of an underlying continuous-time linear dynamical system, have garnered substantial attention and achieved breakthrough advancements in independent sequence modeling. In this work, we undertake a principled investigation that extends SSM theory to temporal graphs by integrating structural information into the online approximation objective via the adoption of a Laplacian regularization term. The emergent continuous-time system introduces novel algorithmic challenges, thereby necessitating our development of GraphSSM, a graph state space model for modeling the dynamics of temporal graphs. Extensive experimental results demonstrate the effectiveness of our GraphSSM framework across various temporal graph benchmarks.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/919e5db29c7b7be4468b975eb4c0fa4a543165fc" target='_blank'>State Space Models on Temporal Graphs: A First-Principles Study</a></td>
          <td>
            Jintang Li, Ruofan Wu, Xinzhou Jin, Boqun Ma, Liang Chen, Zibin Zheng
          </td>
          <td>2024-06-03</td>
          <td>ArXiv</td>
          <td>1</td>
          <td>12</td>
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