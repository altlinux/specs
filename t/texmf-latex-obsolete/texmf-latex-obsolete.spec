Name: texmf-latex-obsolete
Version: 0.1
Release: alt1
Summary: Collection of obsolete LaTeX packages, kept for compatibility with old documents
License: %lppl
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-texmf rpm-build-licenses
BuildRequires: ctanify texlive-latex-base

Source0: %name-%version.tar

%description
Collection of obsolete LaTeX packages, kept for compatibility with old documents.

This collection was created primarily to provide those packages which are
not included in texlive but rewuired by some other texlive packages.

Packages included:
* pst-char.sty (really wrappers for pst-text)
* mathtime.sty (really uses compatible belleek fonts)

%prep
%setup

%build
cd mathtime
latex mathtime.ins

%install
mkdir -p %buildroot%_texmfmain/tex/{generic,latex}
install -pD -m644 mathtime/mathtime.sty %buildroot/%_texmfmain/tex/latex/mathtime/mathtime.sty
install -pD -m644 pst-text/pst-char.sty %buildroot/%_texmfmain/tex/latex/pst-text/pst-char.sty
install -pD -m644 pst-text/pst-char.tex %buildroot/%_texmfmain/tex/generic/pst-text/pst-char.tex


%files
%_texmfmain/*

%changelog
* Thu Jun 11 2009 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

