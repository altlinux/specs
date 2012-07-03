%define srcName pdfcomment

Name: texmf-latex-%srcName
Version: 1.5d
Release: alt1
Summary: A user-friendly interface to pdf annotations
License: %lppl
Group: Publishing
Url: http://pdfcomment.josef-kleber.de/en_index.htm
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-texmf rpm-build-licenses
BuildRequires: ctanify

Source0: %srcName-%version.tar

%description
For a long time pdfLaTeX has offered the command \pdfannot for inserting
arbitrary PDF annotations. However, the command is presented in a form where
additional knowledge of the definition of the PDF format is indispensable. This
package is an answer to the - occasional - questions in newsgroups, about how
one could use the comment function of Adobe Reader. At least for the writer of
LaTeX code, the package offers a convenient and user-friendly means of using
\pdfannot to provide comments in PDF files.

 Since version v1.1, pdfcomment.sty also supports:

 LaTeX -> dvips -> ps2pdf, LaTeX -> dvipdfmx

 and XeLaTeX.

 Unfortunately, support of PDF annotations by PDF viewers is sparse to
 nonexistent. The reference viewer for the development of this package is Adobe
 Reader.

%prep
%setup -n %srcName-%version

%build

%install
mkdir -p %buildroot%_texmfmain
# ctanify is not universal, but is a recommended way to create TEXMF file layouts 
# for packages. Adjustments may be necessary in some cases, see ctanify(1) for more info.
ctanify --pkgname=%srcName --tdsdir=%buildroot/%_texmfmain "*" "doc/*.tex=doc/latex/%srcName"

%files
%_texmfmain/tex/latex/*
%_texmfmain/doc/latex/*

%changelog
* Sun Apr 04 2010 Kirill Maslinsky <kirill@altlinux.org> 1.5d-alt1
- Initial build for ALT Linux Sisyphus

