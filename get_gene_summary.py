# coding:utf-8 

# ------------------------------------------------------------------
# FileName:         get_gene_summary_from_NCBI
# Author:           whittea00
# Version:          V 0.9beta
# Created:          2022-09-20
# Description:      get gene summary from_NCBI
# License:          MIT
# Refer to:         mmendez12's code [https://gist.github.com/mmendez12/8b87f0112f6e203d4c81]
# History:
#          2022-09-20    whitetea00  :Create the file
# ------------------------------------------------------------------

from symbol import term
from Bio import Entrez
from urllib.parse import urljoin

# 使用全名查找，不限定物种
# # Use full name to find, do not limit the species
def gene_summary_from_entrez_use_full_name(gene_full_name):
    # 初始化参数
    # Initialization parameters
    Entrez.email = "example@mail.com"
    # 获取基因ID
    # Get the gene ID
    term = "{}[Gene Full Name]".format(gene_full_name)
    handle = Entrez.esearch(db='gene', term=term)
    result = Entrez.read(handle)
    handle.close()
    gene_id = result["IdList"][0]

    # 获取基因信息
    # Get genetic information
    handle = Entrez.esummary(db="gene", id=gene_id)
    result = Entrez.read(handle)
    handle.close()
    # 截取基因描述
    # Intercept gene description
    res = result['DocumentSummarySet']['DocumentSummary'][0]

    # 拼接NCBI的URL
    # Splicing the URL of the NCBI
    ncbi_url = urljoin("https://www.ncbi.nlm.nih.gov/gene/", gene_id)

    return gene_id, res['Name'], res['Description'], res['Summary'], ncbi_url

# 使用基因缩写查找，限定人类物种
# Use gene abbreviation to find, limit human species
def Human_gene_summary_from_entrez_use_name(gene_name):
    # 初始化参数
    # Initialization parameters
    Entrez.email = "example@mail.com"
    # 获取基因ID
    # Get the gene ID
    term = "(\"{}\"[Gene Name]) AND AND \"homo sapiens\"[Organism]".format(gene_name)
    handle = Entrez.esearch(db='gene', term=term)
    result = Entrez.read(handle)
    handle.close()
    gene_id = result["IdList"][0]

    # 获取基因信息
    # Get genetic information
    handle = Entrez.esummary(db="gene", id=gene_id)
    result = Entrez.read(handle)
    handle.close()
    # 截取基因描述
    # Intercept gene description
    res = result['DocumentSummarySet']['DocumentSummary'][0]

    # 拼接NCBI的URL
    # Splicing the URL of the NCBI
    ncbi_url = urljoin("https://www.ncbi.nlm.nih.gov/gene/", gene_id)
    return gene_id, res['Name'], res['Description'], res['Summary'], ncbi_url


# 测试 gene_summary_from_entrez_use_full_name
# Test gene_summary_from_entrez_use_full_name
gene_full_name='macrophage stimulating 1'
gene_sumary_list = gene_summary_from_entrez_use_full_name(gene_full_name)
print("Query gene [" + gene_full_name + "] result: ")
print("\n")
print("Gene ID: " + gene_sumary_list[0])
print("Gene Name: " + gene_sumary_list[1])
print("Gene Full Name: " + gene_sumary_list[2])
print("Gene Summary: " + gene_sumary_list[3])
print("NCBI URL: " + gene_sumary_list[4])
print("-------------------------")

# 测试 Human_gene_summary_from_entrez_use_name
# Test Human_gene_summary_from_entrez_use_name
gene_name='MST1'
gene_sumary_list2 = Human_gene_summary_from_entrez_use_name(gene_name)
print("Query gene [" + gene_name + "] result: ")
print("\n")
print("Gene ID: " + gene_sumary_list2[0])
print("Gene Name: " + gene_sumary_list2[1])
print("Gene Full Name: " + gene_sumary_list2[2])
print("Gene Summary: " + gene_sumary_list2[3])
print("NCBI URL: " + gene_sumary_list2[4])
print("-------------------------")


