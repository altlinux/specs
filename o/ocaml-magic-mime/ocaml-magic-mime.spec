%define  modulename magic-mime
Name:    ocaml-%modulename
Version: 1.3.1
Release: alt1
Summary: An OCaml library for mapping filenames to common MIME types
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-magic-mime 
BuildRequires: dune ocaml
BuildRequires: rpm-build-ocaml >= 1.4
Source:  %name-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %{modulename}

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Wed Sep 08 2021 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 1.1.2-alt2
- migrated to rpm-build-ocaml-1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- first build for ALT

