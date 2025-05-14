Name: ocaml-sawja
Version: 1.5.12
Release: alt1

Summary: Provides a high level representation of Java .class files in OCaml
Group: Development/ML
License: GPL-3.0
Url: https://github.com/javalib-team/sawja
Vcs: https://github.com/javalib-team/sawja

Source: %name-%version.tar
Patch1: Adapt-to-javalib-3.2.2-gitae04c6b3.patch
Patch2: Extend-install-target-with-module-artifacts.patch

BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-javalib-devel

# Uses ocamlopt
ExclusiveArch: x86_64

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%autopatch -p1
OCAML_DESTDIR="%{buildroot}%{_ocamldir}"
sed -i "s|\(INSTALL = \$(FINDER) install\)|\1 -destdir=$OCAML_DESTDIR|" \
  Makefile.config.example

%build
./configure.sh
make

%install
mkdir -p %buildroot%_ocamldir
make install
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc LICENSE CHANGELOG

%changelog
* Tue May 13 2025 Denis Rastyogin <gerben@altlinux.org> 1.5.12-alt1
- Initial build for ALT Sisyphus.
