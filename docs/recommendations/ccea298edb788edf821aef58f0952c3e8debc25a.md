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
  <i class="footer">This page was last updated on 2024-07-15 06:04:50 UTC</i>
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
    Recommendations for the article <i>Graph Deep Learning for Time Series Forecasting</i>
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
    
        <tr id="Time series forecasting lies at the core of important real-world applications in many fields of science and engineering. The abundance of large time series datasets that consist of complex patterns and long-term dependencies has led to the development of various neural network architectures. Graph neural network approaches, which jointly learn a graph structure based on the correlation of raw values of multivariate time series while forecasting, have recently seen great success. However, such solutions are often costly to train and difficult to scale. In this paper, we propose TimeGNN, a method that learns dynamic temporal graph representations that can capture the evolution of inter-series patterns along with the correlations of multiple series. TimeGNN achieves inference times 4 to 80 times faster than other state-of-the-art graph-based methods while achieving comparable forecasting performance">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/d9916caa8da69496ecc8e0b1c229c73a60d6f861" target='_blank'>TimeGNN: Temporal Dynamic Graph Learning for Time Series Forecasting</a></td>
          <td>
            Nancy R. Xu, Chrysoula Kosma, M. Vazirgiannis
          </td>
          <td>2023-07-27</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>54</td>
        </tr>
    
        <tr id="Accurate forecasting of multivariate time series is an extensively studied subject in finance, transportation, and computer science. Fully mining the correlation and causation between the variables in a multivariate time series exhibits noticeable results in improving the performance of a time series model. Recently, some models have explored the dependencies between variables through end-to-end graph structure learning without the need for predefined graphs. However, current models do not incorporate the trade-off between efficiency and flexibility and lack the guidance of domain knowledge in the design of graph structure learning algorithms. This paper alleviates the above issues by proposing Balanced Graph Structure Learning for Forecasting (BGSLF), a novel deep learning model that joins graph structure learning and forecasting. Technically, BGSLF leverages the spatial information into convolutional operations and extracts temporal dynamics using the diffusion convolutional recurrent network. The proposed framework balance the trade-off between efficiency and flexibility by introducing Multi-Graph Generation Network (MGN) and Graph Selection Module. In addition, a method named Smooth Sparse Unit (SSU) is designed to sparse the learned graph structures, which conforms to the sparse spatial correlations in the real world. Extensive experiments on four real-world datasets demonstrate that our model achieves state-of-the-art performances with minor trainable parameters. Code will be made publicly available.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/cf803de5a63ec6893960af15756a8e4766c99e0d" target='_blank'>Balanced Graph Structure Learning for Multivariate Time Series Forecasting</a></td>
          <td>
            Weijun Chen, Yanze Wang, Chengshuo Du, Zhenglong Jia, Feng Liu, Ran Chen
          </td>
          <td>2022-01-24</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>10</td>
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
    
        <tr id="The challenge of effectively learning inter-series correlations for multivariate time series forecasting remains a substantial and unresolved problem. Traditional deep learning models, which are largely dependent on the Transformer paradigm for modeling long sequences, often fail to integrate information from multiple time series into a coherent and universally applicable model. To bridge this gap, our paper presents ForecastGrapher, a framework reconceptualizes multivariate time series forecasting as a node regression task, providing a unique avenue for capturing the intricate temporal dynamics and inter-series correlations. Our approach is underpinned by three pivotal steps: firstly, generating custom node embeddings to reflect the temporal variations within each series; secondly, constructing an adaptive adjacency matrix to encode the inter-series correlations; and thirdly, augmenting the GNNs' expressive power by diversifying the node feature distribution. To enhance this expressive power, we introduce the Group Feature Convolution GNN (GFC-GNN). This model employs a learnable scaler to segment node features into multiple groups and applies one-dimensional convolutions with different kernel lengths to each group prior to the aggregation phase. Consequently, the GFC-GNN method enriches the diversity of node feature distribution in a fully end-to-end fashion. Through extensive experiments and ablation studies, we show that ForecastGrapher surpasses strong baselines and leading published techniques in the domain of multivariate time series forecasting.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/60560da7e2483d4f788c228ebd5e226ae1f40002" target='_blank'>ForecastGrapher: Redefining Multivariate Time Series Forecasting with Graph Neural Networks</a></td>
          <td>
            Wanlin Cai, Kun Wang, Hao Wu, Xiaoxu Chen, Yuankai Wu
          </td>
          <td>2024-05-28</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>3</td>
        </tr>
    
        <tr id="Modeling multivariate time series has long been a subject that has attracted researchers from a diverse range of fields including economics, finance, and traffic. A basic assumption behind multivariate time series forecasting is that its variables depend on one another but, upon looking closely, it is fair to say that existing methods fail to fully exploit latent spatial dependencies between pairs of variables. In recent years, meanwhile, graph neural networks (GNNs) have shown high capability in handling relational dependencies. GNNs require well-defined graph structures for information propagation which means they cannot be applied directly for multivariate time series where the dependencies are not known in advance. In this paper, we propose a general graph neural network framework designed specifically for multivariate time series data. Our approach automatically extracts the uni-directed relations among variables through a graph learning module, into which external knowledge like variable attributes can be easily integrated. A novel mix-hop propagation layer and a dilated inception layer are further proposed to capture the spatial and temporal dependencies within the time series. The graph learning, graph convolution, and temporal convolution modules are jointly learned in an end-to-end framework. Experimental results show that our proposed model outperforms the state-of-the-art baseline methods on 3 of 4 benchmark datasets and achieves on-par performance with other approaches on two traffic datasets which provide extra structural information.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/75e924bd79d27a23f3f93d9b1ab62a779505c8d2" target='_blank'>Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks</a></td>
          <td>
            Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Xiaojun Chang, Chengqi Zhang
          </td>
          <td>2020-05-24</td>
          <td>Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining</td>
          <td>903</td>
          <td>54</td>
        </tr>
    
        <tr id="Graph Neural Networks (GNN) have gained significant traction in the forecasting domain, especially for their capacity to simultaneously account for intra-series temporal correlations and inter-series relationships. This paper introduces a novel Hierarchical GNN (DeepHGNN) framework, explicitly designed for forecasting in complex hierarchical structures. The uniqueness of DeepHGNN lies in its innovative graph-based hierarchical interpolation and an end-to-end reconciliation mechanism. This approach ensures forecast accuracy and coherence across various hierarchical levels while sharing signals across them, addressing a key challenge in hierarchical forecasting. A critical insight in hierarchical time series is the variance in forecastability across levels, with upper levels typically presenting more predictable components. DeepHGNN capitalizes on this insight by pooling and leveraging knowledge from all hierarchy levels, thereby enhancing the overall forecast accuracy. Our comprehensive evaluation set against several state-of-the-art models confirm the superior performance of DeepHGNN. This research not only demonstrates DeepHGNN's effectiveness in achieving significantly improved forecast accuracy but also contributes to the understanding of graph-based methods in hierarchical time series forecasting.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/699d32e116b67bd6f64d689ce7ed97a0aef60ad6" target='_blank'>DeepHGNN: Study of Graph Neural Network based Forecasting Methods for Hierarchically Related Multivariate Time Series</a></td>
          <td>
            Abishek Sriramulu, Nicolas Fourrier, Christoph Bergmeir
          </td>
          <td>2024-05-29</td>
          <td>ArXiv</td>
          <td>0</td>
          <td>4</td>
        </tr>
    
        <tr id="Multivariate time series (MTS) forecasting has shown great importance in numerous industries. Current state-of-the-art graph neural network (GNN)-based forecasting methods usually require both graph networks (e.g., GCN) and temporal networks (e.g., LSTM) to capture inter-series (spatial) dynamics and intra-series (temporal) dependencies, respectively. However, the uncertain compatibility of the two networks puts an extra burden on handcrafted model designs. Moreover, the separate spatial and temporal modeling naturally violates the unified spatiotemporal inter-dependencies in real world, which largely hinders the forecasting performance. To overcome these problems, we explore an interesting direction of directly applying graph networks and rethink MTS forecasting from a pure graph perspective. We first define a novel data structure, hypervariate graph, which regards each series value (regardless of variates or timestamps) as a graph node, and represents sliding windows as space-time fully-connected graphs. This perspective considers spatiotemporal dynamics unitedly and reformulates classic MTS forecasting into the predictions on hypervariate graphs. Then, we propose a novel architecture Fourier Graph Neural Network (FourierGNN) by stacking our proposed Fourier Graph Operator (FGO) to perform matrix multiplications in Fourier space. FourierGNN accommodates adequate expressiveness and achieves much lower complexity, which can effectively and efficiently accomplish the forecasting. Besides, our theoretical analysis reveals FGO's equivalence to graph convolutions in the time domain, which further verifies the validity of FourierGNN. Extensive experiments on seven datasets have demonstrated our superior performance with higher efficiency and fewer parameters compared with state-of-the-art methods.">
          <td id="tag"><i class="material-icons">visibility_off</i></td>
          <td><a href="https://www.semanticscholar.org/paper/9dbcb0893d05e6176353eee401afa4929b570cf6" target='_blank'>FourierGNN: Rethinking Multivariate Time Series Forecasting from a Pure Graph Perspective</a></td>
          <td>
            Kun Yi, Qi Zhang, Wei Fan, Hui He, Liang Hu, Pengyang Wang, Ning An, Longbin Cao, Zhendong Niu
          </td>
          <td>2023-11-10</td>
          <td>ArXiv</td>
          <td>17</td>
          <td>4</td>
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