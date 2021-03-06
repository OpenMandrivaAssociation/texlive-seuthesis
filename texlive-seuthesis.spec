# revision 33042
# category Package
# catalog-ctan /macros/latex/contrib/seuthesis
# catalog-date 2014-02-24 07:33:27 +0100
# catalog-license gpl3
# catalog-version 2.1.2
Name:		texlive-seuthesis
Version:	2.1.2
Release:	6
Summary:	LaTeX template for theses at Southeastern University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/seuthesis
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This template is for theses at Southeastern University,
Nanjing, China.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/seuthesis/seuthesis.bst
%doc %{_texmfdistdir}/doc/latex/seuthesis/Makefile
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/A3cover.tex
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/A4cover.tex
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/a3cover.bat
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/a3cover.sh
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/a4cover.bat
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/a4cover.sh
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/bookspine_hor.tex
%doc %{_texmfdistdir}/doc/latex/seuthesis/a3cover/bookspine_ver.tex
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/back-cover.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/doctor-hwzs.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/doctor.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/engineering.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/front-cover.jpg
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/master-hwzs.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/master.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/seu-badge-logo.eps
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/seu-badge-logo.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/seu-color-logo.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/seu-text-logo.eps
%doc %{_texmfdistdir}/doc/latex/seuthesis/figures/seu-text-logo.png
%doc %{_texmfdistdir}/doc/latex/seuthesis/sample-bachelor.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/sample-doctor.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/sample-master.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/sample.tex
%doc %{_texmfdistdir}/doc/latex/seuthesis/seuthesis.bib
%doc %{_texmfdistdir}/doc/latex/seuthesis/seuthesis.pdf
%doc %{_texmfdistdir}/doc/latex/seuthesis/zharticle/scrsize9pt.clo
%doc %{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.bst
%doc %{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.cfg
%doc %{_texmfdistdir}/doc/latex/seuthesis/zharticle/zharticle.cls
#- source
%doc %{_texmfdistdir}/source/latex/seuthesis/seuthesis.dtx
%doc %{_texmfdistdir}/source/latex/seuthesis/seuthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
