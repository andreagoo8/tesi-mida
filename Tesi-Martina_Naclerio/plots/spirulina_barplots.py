base = '''% !TeX encoding = UTF-8

\begin{figure}[H]
\centering
% Subfigure 1
	\subcaptionbox%
	[]%
	{Ashes content\label{subfig:}}%
		{\includegraphics[width=0.5\textwidth]{../plots/mpl/barplots_anova/barplots_outs/spirulina_ashes}}%
\hfill
% Subfigure 2
	\subcaptionbox%
	[]%
	{Moisture content\label{subfig:}}%
		{\includegraphics[width=0.5\textwidth]{../plots/mpl/barplots_anova/barplots_outs/spirulina_moisture}}%
\\[\vbtwsfig]
% Subfigure 3
	\subcaptionbox%
	[]%
	{Lipids content\label{subfig:}}%
		{\includegraphics[width=0.5\textwidth]{../plots/mpl/barplots_anova/barplots_outs/spirulina_lipids}}%
\hfill
% Subfigure 4
	\subcaptionbox%
	[]%
	{Proteins content\label{subfig:}}%
		{\includegraphics[width=0.5\textwidth]{../plots/mpl/barplots_anova/barplots_outs/spirulina_proteins}}%
\caption%
[]%
{\brpltfigtitle{} \species{Spirulina}}
\label{fig:}
\end{figure}'''

print(base)