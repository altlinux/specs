%define srcName logreq

Name: texmf-latex-%srcName
Version: 1.0
Release: alt1
Summary: Support for automation of the LaTeX workflow
License: LPPL (LaTeX Project Public License), version 1.3 or later
Group: Publishing
Url: http://www.ctan.org/pkg/logreq
Packager: Kirill Maslinsky <kirill at altlinux.org>

BuildRequires(pre): rpm-build-texmf

BuildArch: noarch

Source0: %srcName.tar

%description
The package helps to automate a typical LaTeX workflow that involves running
LaTeX several times, running tools such as BibTeX or makeindex, and so on. It
will log requests like "please rerun LaTeX" or "please run BibTeX on file X" to
an external XML file which lists all open tasks in a machine-readable format.
Compiler scripts and integrated LaTeX editing environments may parse this file
to determine the next steps in the workflow in a way that is more efficient
than parsing the main log file. In sum, the package will do two things:

    1) enable package authors to use LaTeX commands to issue requests, 
    2) collect all requests from all packages and write them to an external 
       XML file at the end of the document.



%prep
%setup %srcName.tar

%build

%install
mkdir -p %buildroot%_texmfmain/tex/latex/%srcName
mkdir -p %buildroot%_texmfdoc/latex/%srcName
cp -a logreq.{sty,def} %buildroot%_texmfmain/tex/latex/%srcName
cp -a examples/ %buildroot/%_texmfdoc/latex/%srcName

%files
%_texmfmain/tex/latex/%srcName
%_texmfdoc/latex/%srcName
%doc README 

%changelog
* Wed Nov 02 2011 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus

