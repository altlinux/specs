%define srcName fixme

Name: texmf-latex-%srcName
Version: 4.1
Release: alt1
Summary: Insert "fixme" notes into draft documents.
License: %lppl
Group: Publishing
Url: http://www.ctan.org/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-texmf rpm-build-licenses rpm-macros-emacs
BuildRequires: ctanify texlive-latex-base emacs-mode-auctex

Requires: emacs-mode-auctex

Source0: %srcName-%version.tar

%description 
This package provides a way to insert fixme notes in documents being developed
(in draft mode). Such notes can appear in the margin of the document, as index
entries, in the log file and as warnings on stdout. It is also possible to
summarize them in a list. If your document is in a final version, any remaining
fixme notes will produce an error. FiXme also comes with support for AUC-TeX.


%prep
%setup -n %srcName-%version

%build
latex %srcName.ins
%byte_compile_file fixme.el

%install
mkdir -p %buildroot%_texmfmain/{doc,source,tex}/latex/%srcName/
cp -at %buildroot%_texmfmain/tex/latex/%srcName/ layouts themes %srcName.sty
cp -at %buildroot%_texmfmain/doc/latex/%srcName/ README %srcName.pdf
cp -at %buildroot%_texmfmain/source/latex/%srcName/ %srcName.{dtx,ins}

mkdir -p %buildroot%_emacslispdir/auctex/styles
install -m644 fixme.el fixme.elc %buildroot%_emacslispdir/auctex/styles


%files
%_texmfmain/tex/latex/%srcName
%_texmfmain/doc/latex/%srcName
%_texmfmain/source/latex/%srcName
%_emacslispdir/auctex/styles/*

%changelog
* Fri Apr 02 2010 Kirill Maslinsky <kirill@altlinux.org> 4.1-alt1
- initial revision

