# get_gene_summary_from_NCBI
Use gene name or full name query summary form NCBI.

## Used biopython package.

## Test Result
```
Query gene [macrophage stimulating 1] result: 


Gene ID: 4485
Gene Name: MST1
Gene Full Name: macrophage stimulating 1
Gene Summary: The protein encoded by this gene contains four kringle domains and a serine protease domain, similar to that found in hepatic growth factor. Despite the presence of the serine protease domain, the encoded protein may not have any proteolytic activity. The receptor for this protein is RON tyrosine kinase, which upon activation stimulates ciliary motility of ciliated epithelial lung cells. This protein is secreted and cleaved to form an alpha chain and a beta chain bridged by disulfide bonds. [provided by RefSeq, Jan 2010]
NCBI URL: https://www.ncbi.nlm.nih.gov/gene/4485
-------------------------
Query gene [MST1] result: 


Gene ID: 6789
Gene Name: STK4
Gene Full Name: serine/threonine kinase 4
Gene Summary: The protein encoded by this gene is a cytoplasmic kinase that is structurally similar to the yeast Ste20p kinase, which acts upstream of the stress-induced mitogen-activated protein kinase cascade. The encoded protein can phosphorylate myelin basic protein and undergoes autophosphorylation. A caspase-cleaved fragment of the encoded protein has been shown to be capable of phosphorylating histone H2B. The particular phosphorylation catalyzed by this protein has been correlated with apoptosis, and it's possible that this protein induces the chromatin condensation observed in this process. [provided by RefSeq, Jul 2008]
NCBI URL: https://www.ncbi.nlm.nih.gov/gene/6789
-------------------------
```


还没加异常处理，有空再写。

但是，我相信你一定可以的！


## 开发计划
1. 增加异常处理功能
2. 增加批处理功能（从csv中读取批量基因名称，自动生成数据列表）
3. 增加基因查询结果比对的功能，让我们可以直观的看到检索到的结果是否与自己预期结果相匹配
4. 加个GUI，计划用PyQt来做
5. 再来个相关文献获取的功能
6. 再搞个相关基因的分析...?（这不就变成了另外的项目了么🤔）
