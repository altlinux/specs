%define srcName etoolbox

Name: texmf-latex-%srcName
Version: 2.1
Release: alt1
Summary: Tool-box for LaTeX programmers using e-TeX
License: %lppl
Group: Publishing
Url: http://www.ctan.org/pkg/etoolbox
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-texmf rpm-build-licenses
BuildRequires: ctanify

Source0: %srcName-%version.tar

%description
The etoolbox package is a toolbox of programming facilities geared primarily
towards LaTeX class and package authors. It provides LaTeX frontends to some of
the new primitives provided by e-TeX as well as some generic tools which are
not strictly related to e-TeX but match the profile of this package. Note that
the initial versions of this package were released under the name elatex.

The package provides functions that seem to offer alternative ways of
implementing some LaTeX kernel commands; nevertheless, the package will not
modify any part of the LaTeX kernel.


%prep
%setup -n %srcName-%version

%build

%install
mkdir -p %buildroot%_texmfmain
# ctanify is not universal, but is a recommended way to create TEXMF file layouts 
# for packages. Adjustments may be necessary in some cases, see ctanify(1) for more info.
ctanify --pkgname=%srcName --tdsdir=%buildroot/%_texmfmain "*" 

%files
%_texmfmain/tex/latex/*
%_texmfmain/doc/latex/*

%changelog
* Wed Nov 02 2011 Kirill Maslinsky <kirill@altlinux.org> 2.1-alt1
- 2.1
- new uniform ctan url

* Mon Apr 12 2010 Kirill Maslinsky <kirill@altlinux.org> 1.9-alt1
- 1.9
- correct url

* Sat Apr 10 2010 Kirill Maslinsky <kirill@altlinux.org> 1.8-alt1
- Initial build for ALT Linux Sisyphus

