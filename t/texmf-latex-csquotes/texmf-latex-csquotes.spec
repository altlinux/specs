%define srcName csquotes

Name: texmf-latex-%srcName
Version: 4.4d
Release: alt1
Summary: Context sensitive quotation facilities for LaTeX
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/contrib/csquotes/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

Source0: %srcName-%version.tar

BuildRequires(pre): rpm-build-texmf
BuildRequires: ctanify

Provides: tetex-latex-csquotes
Obsoletes: tetex-latex-csquotes

%description
This package provides advanced facilities for inline and display quotations. It
is designed for a wide range of tasks ranging from the most simple applications
to the more complex demands of formal quotations. The facilities include
commands, environments, and user-definable `smart quotes' which dynamically
adjust to their context. Quotation marks are switched automatically if
quotations are nested and they can be adjusted to the current language if the
babel  package is available.  There are additional facilities designed to cope
with the more specific demands of academic writing, especially in the
humanities and the social sciences.  All quote styles as well as the optional
active quotes are freely configurable.

The package is dependent on e-TeX, and requires the author's  etoolbox
package.

%prep
%setup -q -n %srcName-%version

%build

%install
install -d %buildroot%_texmfmain
ctanify --pkgname=%srcName --tdsdir=%buildroot/%_texmfmain "*" "tutorial.tex=doc/latex/%srcName" "csquotes.{cfg,def}=tex/latex/%srcName"

%files
%_texmfmain/tex/latex/%srcName
%_texmfmain/doc/latex/%srcName

%changelog
* Sat Apr 10 2010 Kirill Maslinsky <kirill@altlinux.org> 4.4d-alt1
- 4.4d
- package renamed to texmf-latex-csquotes
- modernize spec
  + use ctanify
  + use rpm-build-texmf
  + remove obsolete post(un) calls

* Wed Nov 14 2007 Kirill Maslinsky <kirill@altlinux.org> 3.7-alt1
- Initial build for Sisyphus



