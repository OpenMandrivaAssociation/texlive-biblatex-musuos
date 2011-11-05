# revision 24097
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-musuos
# catalog-date 2011-09-23 15:58:32 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-biblatex-musuos
Version:	1.0
Release:	1
Summary:	A biblatex style for citations in musuos.cls
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-musuos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-musuos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-musuos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The style is designed for use with the musuos class, but it
should be usable with other classes, too.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-musuos/german-musuos.lbx
%{_texmfdistdir}/tex/latex/biblatex-musuos/musuos.bbx
%{_texmfdistdir}/tex/latex/biblatex-musuos/musuos.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-musuos/README
%doc %{_texmfdistdir}/doc/latex/biblatex-musuos/biblatex-musuos.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-musuos/biblatex-musuos.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-musuos/musuos-bsp.bib
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
