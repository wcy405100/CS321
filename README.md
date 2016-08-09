# CS321
CS321-Theory of Computation

This is the final project of CS321-Theory of Computation course. 

In this project I use python to implement the CKY algorithm. (wikipedia explanation: https://en.wikipedia.org/wiki/CYK_algorithm)

The idea of CKY algorithm is using dynamic programming to test whether the given expression has at least a parse tree or not. In the .in file, the grammar in CNF is separated by a empty line. And the testing expression is listed below the empty line. The time complexity of CKY is O(n^3).

The instruction to run this program is very straight forward. You open the terminal cd to the right directory, then type: python Chenyu_wang_cky.py cfg1.in 
You can change the cfg1.in to cfg2.in or cfg3.in.

中文说明：

此文件是CS321，计算理论课程的期末附加作业。

在这个项目中，我使用python编写了CKY算法 （关于CKY算法的连接： https://en.wikipedia.org/wiki/CYK_algorithm）

CKY算法的大意是使用动态规划，去测试所给的表达式，是否符合CNF的语法规则。如果符合规则，就能输出分析树的结构和不同结构分析树的个数，如果不符合语法规则，就输出0分析树。在.in文件里，空行以上的部分是CNF的语法规则，在空行以下的部分为需要测试的表达式。此算法虽然能给出想要的结果，但是其时间复杂度却需要O(n^3);同时还需要语法规则是CNF形式的。

语言使用：Python

运行指南：
打开terminal，移动到文件所在位置，输入：python Chenyu_wang_cky.py cfg1.in
其中cfg1.in可改为其他两个.in 文件
