%define  modulename crunch
Name:    ocaml-%modulename
Version: 3.3.1
Release: alt1
Summary: Convert a filesystem into a static OCaml module
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-crunch
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-ptime-devel >= 1.1.0
BuildPreReq: rpm-build-ocaml >= 1.6

%description
ocaml-crunch takes a directory of files and compiles them into a standalone
OCaml module which serves the contents directly from memory.
This can be convenient for libraries that need a few embedded files
(such as a web server) and do not want to deal
with all the trouble of file configuration.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

# TODO
#%check
#%dune_check

%files -f ocaml-files.runtime
%_bindir/ocaml-crunch
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 3.3.1-alt1
- first build for ALT Linux
