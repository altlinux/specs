%def_with check
Name: ocaml-optint
Version: 0.3.0
Release: alt1
Summary: Efficient integer types on 64-bit architectures
Group: Development/ML
License: ISC
Url: https://github.com/mirage/optint
VCS: https://github.com/mirage/optint
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.07.0
BuildRequires: dune

%if_with check
BuildRequires: ocaml-crowbar-devel >= 0.2
BuildRequires: ocaml-monolith-devel
BuildRequires: ocaml-fmt-devel
%endif

%description
This library provides two new integer types, `Optint.t` and `Int63.t`,
which guarantee efficient representation on 64-bit architectures and
provide a best-effort boxed representation on 32-bit architectures.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p optint

%install
%dune_install optint

%check
%dune_check -p optint

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Oct 06 2026 Anton Farygin <rider@altlinux.org> 0.3.0-alt1
- initial build for ALT Linux