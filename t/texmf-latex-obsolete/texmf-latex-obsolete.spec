Name: texmf-latex-obsolete
Version: 0.1
Release: alt2
Summary: Collection of obsolete LaTeX packages, kept for compatibility with old documents
License: %lppl
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-tex rpm-build-licenses
BuildRequires: ctanify texlive-collection-latex

Source0: %name-%version.tar

# * pst-char.sty (really wrappers for pst-text)
%description
Collection of obsolete LaTeX packages, kept for compatibility with old documents.

This collection was created primarily to provide those packages which are
not included in texlive but rewuired by some other texlive packages.

Packages included:
* mathtime.sty (really uses compatible belleek fonts)

%prep
%setup

%build
cd mathtime
latex mathtime.ins

%install
mkdir -p %buildroot%_texmfmain/tex/{generic,latex}
install -pD -m644 mathtime/mathtime.sty %buildroot/%_texmfmain/tex/latex/mathtime/mathtime.sty
#install -pD -m644 pst-text/pst-char.sty %buildroot/%_texmfmain/tex/latex/pst-text/pst-char.sty
#install -pD -m644 pst-text/pst-char.tex %buildroot/%_texmfmain/tex/generic/pst-text/pst-char.tex

%files
%_texmfmain/*

%changelog
* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2
- NMU:
- removed pst-char as it is included even in texlive 2017
- rebuild with rpm-build-tex

* Thu Jun 11 2009 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

