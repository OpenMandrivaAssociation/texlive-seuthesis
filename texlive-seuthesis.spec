%global tl_name seuthesis
%global tl_revision 33042

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.2
Release:	%{tl_revision}.1
Summary:	LaTeX template for theses at Southeastern University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/seuthesis
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This template is for theses at Southeastern University, Nanjing, China.

