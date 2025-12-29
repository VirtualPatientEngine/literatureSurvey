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
  <i class="footer">This page was last updated on 2025-12-29 06:14:10 UTC</i>
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
    
        <tr id="World modelling is essential for understanding and predicting the dynamics of complex systems by learning both spatial and temporal dependencies. However, current frameworks, such as Transformers and selective state-space models like Mambas, exhibit limitations in efficiently encoding spatial and temporal structures, particularly in scenarios requiring long-term high-dimensional sequence modelling. To address these issues, we propose a novel recurrent framework, the \textbf{FACT}ored \textbf{S}tate-space (\textbf{FACTS}) model, for spatial-temporal world modelling. The FACTS framework constructs a graph-structured memory with a routing mechanism that learns permutable memory representations, ensuring invariance to input permutations while adapting through selective state-space propagation. Furthermore, FACTS supports parallel computation of high-dimensional sequences. We empirically evaluate FACTS across diverse tasks, including multivariate time series forecasting, object-centric world modelling, and spatial-temporal graph prediction, demonstrating that it consistently outperforms or matches specialised state-of-the-art models, despite its general-purpose world modelling design.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/ec840755867d3f5cf175cb57de963f042297f4ef" target='_blank'>FACTS: A Factored State-Space Framework For World Modelling</a></td>
          <td>
            Nanbo Li, Firas Laakom, Yucheng Xu, Wenyi Wang, Jurgen Schmidhuber
          </td>
          <td>2024-10-28</td>
          <td>ArXiv</td>
          <td>1</td>
          <td>7</td>
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
          <td>70</td>
        </tr>
    
        <tr id="None">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/cdd4e532084bbd68fd22c56f7abbec1ceaff28b1" target='_blank'>RIVA: Efficient relational inference with variate attention</a></td>
          <td>
            Ruizi Wu, Liming Pan, Linyuan Lu
          </td>
          <td>2025-06-01</td>
          <td>Neural networks : the official journal of the International Neural Network Society</td>
          <td>0</td>
          <td>2</td>
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
          <td>DBLP, ArXiv, MAG</td>
          <td>486</td>
          <td>52</td>
        </tr>
    
        <tr id="Complex systems are characterized by intricate interactions between entities that evolve dynamically over time. Accurate inference of these dynamic relationships is crucial for understanding and predicting system behavior. In this paper, we propose Regulatory Temporal Interaction Network Inference (RiTINI) for inferring time-varying interaction graphs in complex systems using a novel combination of space-and-time graph attentions and graph neural ordinary differential equations (ODEs). RiTINI leverages time-lapse signals on a graph prior, as well as perturbations of signals at various nodes in order to effectively capture the dynamics of the underlying system. This approach is distinct from traditional causal inference networks, which are limited to inferring acyclic and static graphs. In contrast, RiTINI can infer cyclic, directed, and time-varying graphs, providing a more comprehensive and accurate representation of complex systems. The graph attention mechanism in RiTINI allows the model to adaptively focus on the most relevant interactions in time and space, while the graph neural ODEs enable continuous-time modeling of the system's dynamics. We evaluate RiTINI's performance on simulations of dynamical systems, neuronal networks, and gene regulatory networks, demonstrating its state-of-the-art capability in inferring interaction graphs compared to previous methods.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/017758833be6b6155b4b012b81affa1b62937b58" target='_blank'>Inferring dynamic regulatory interaction graphs from time series data with perturbations</a></td>
          <td>
            Dhananjay Bhaskar, Sumner Magruder, E. Brouwer, Aarthi Venkat, Frederik Wenkel, Guy Wolf, Smita Krishnaswamy
          </td>
          <td>2023-06-13</td>
          <td>Proceedings of machine learning research</td>
          <td>9</td>
          <td>29</td>
        </tr>
    
        <tr id="Knowledge about the hidden factors that determine particular system dynamics is crucial for both explaining them and pursuing goal-directed interventions. Inferring these factors from time series data without supervision remains an open challenge. Here, we focus on spatiotemporal processes, including wave propagation and weather dynamics, for which we assume that universal causes (e.g. physics) apply throughout space and time. A recently introduced DIstributed SpatioTemporal graph Artificial Neural network Architecture (DISTANA) is used and enhanced to learn such processes, requiring fewer parameters and achieving significantly more accurate predictions compared to temporal convolutional neural networks and other related approaches. We show that DISTANA, when combined with a retrospective latent state inference principle called active tuning, can reliably derive location-respective hidden causal factors. In a current weather prediction benchmark, DISTANA infers our planet's land-sea mask solely by observing temperature dynamics and, meanwhile, uses the self inferred information to improve its own future temperature predictions.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/bff58be5a77a356a4aaa1b1a923b5ba536ace307" target='_blank'>Latent State Inference in a Spatiotemporal Generative Model</a></td>
          <td>
            Matthias Karlbauer, Tobias Menge, S. Otte, H. Lensch, Thomas Scholten, V. Wulfmeyer, Martin Volker Butz
          </td>
          <td>2020-09-21</td>
          <td>ArXiv, DBLP</td>
          <td>1</td>
          <td>53</td>
        </tr>
    
        <tr id="Switching dynamical systems can model complicated time series data while maintaining interpretability by inferring a finite set of dynamics primitives and explaining different portions of the observed time series with one of these primitives. However, due to the discrete nature of this set, such models struggle to capture smooth, variable-speed transitions, as well as stochastic mixtures of overlapping states, and the inferred dynamics often display spurious rapid switching on real-world datasets. Here, we propose the Gumbel Dynamical Model (GDM). First, by introducing a continuous relaxation of discrete states and a different noise model defined on the relaxed-discrete state space via the Gumbel distribution, GDM expands the set of available state dynamics, allowing the model to approximate smoother and non-stationary ground-truth dynamics more faithfully. Second, the relaxation makes the model fully differentiable, enabling fast and scalable training with standard gradient descent methods. We validate our approach on standard simulation datasets and highlight its ability to model soft, sticky states and transitions in a stochastic setting. Furthermore, we apply our model to two real-world datasets, demonstrating its ability to infer interpretable states in stochastic time series with multiple dynamics, a setting where traditional methods often fail.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/c097e9889ddff5e6af450c15755d66e9f902677d" target='_blank'>Interpretable time series analysis with Gumbel dynamics</a></td>
          <td>
            Yiliu Wang, Timothy Doyeon Kim, Eric Shea-Brown, U. Sümbül
          </td>
          <td>2025-09-25</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>17</td>
        </tr>
    
        <tr id="Understanding interactions between entities, e.g., joints of the human body, team sports players, etc., is crucial for tasks like forecasting. However, interactions between entities are commonly not observed and often hard to quantify. To address this challenge, recently, `Neural Relational Inference' was introduced. It predicts static relations between entities in a system and provides an interpretable representation of the underlying system dynamics that are used for better trajectory forecasting. However, generally, relations between entities change as time progresses. Hence, static relations improperly model the data. In response to this, we develop Dynamic Neural Relational Inference (dNRI), which incorporates insights from sequential latent variable models to predict separate relation graphs for every time-step. We demonstrate on several real-world datasets that modeling dynamic relations improves forecasting of complex trajectories.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/6c32d084117d093ac3d2735d9d323f20bb2d2074" target='_blank'>Dynamic Neural Relational Inference</a></td>
          <td>
            Colin Graber, A. Schwing
          </td>
          <td>2020-06-01</td>
          <td>2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)</td>
          <td>63</td>
          <td>65</td>
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