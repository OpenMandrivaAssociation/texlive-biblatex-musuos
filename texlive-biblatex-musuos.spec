%global tl_name biblatex-musuos
%global tl_revision 24097

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A BibLaTeX style for citations in musuos.cls
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-musuos
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-musuos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-musuos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The style is designed for use with the musuos class, but it should be
usable with other classes, too.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-musuos
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-musuos
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-musuos/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-musuos/biblatex-musuos.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-musuos/biblatex-musuos.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-musuos/musuos-bsp.bib
%{_datadir}/texmf-dist/tex/latex/biblatex-musuos/german-musuos.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-musuos/musuos.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-musuos/musuos.cbx
