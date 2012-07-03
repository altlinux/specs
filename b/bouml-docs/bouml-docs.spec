Name: bouml-docs
Version: 20070303
Release: alt1

Summary: Documentation for BOUML project

License: GPL
Group: Documentation
Url: http://bouml.free.fr/doc.tar.gz

Packager: Yuriy Kashirin <uka@altlinux.ru>

Source: doc.tar.gz

BuildArch: noarch

%description
Documentation for BOUML project.
Last revision March 03th 2007, compatible with BOUML releases
since 2.21.7

Not yet documented :
- new toggle add operation profile on body edition in the menu
  miscellaneous,
- new drawing setting called show parameter direction,
- modification of the drawing setting called draw all classes
  relations,
- to freeze of getter and setter operations,
- new generation settings to ask for a C++ setter operation to
  receive its argument by reference,
- the generation directories specified in the generation settings
  can be relative to the project

%prep
%setup -c %name

%build
%install
mkdir -p %buildroot%_docdir/%name-%version/html
cp -Rf doc/* %buildroot%_docdir/%name-%version/html

%files
%_docdir/%name-%version

%changelog
* Tue Apr 03 2007 Yuriy Kashirin <uka@altlinux.ru> 20070303-alt1
- Avoid using internal rpm macros started with %%__ in spec

* Tue Mar 27 2007 Yuriy Kashirin <uka@altlinux.ru> 20070303-alt0.1
- Initial build for ALT Linux (Sisyphus)

