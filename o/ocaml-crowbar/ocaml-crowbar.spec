# Missing test dependencies in Sisyphus:
#   - ocaml-calendar-devel
#   - ocaml-pprint-devel
%def_without check
Name: ocaml-crowbar
Version: 0.2.2
Release: alt1
Summary: Write tests, let a fuzzer find failing cases
Group: Development/ML
License: MIT
Url: https://github.com/stedolan/crowbar
VCS: https://github.com/stedolan/crowbar
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.08
BuildRequires: dune >= 2.9
BuildRequires: ocaml-cmdliner-devel >= 1.1.0
BuildRequires: ocaml-afl-persistent-devel >= 1.1
BuildRequires: ocaml-odoc-devel

%if_with check
BuildRequires: ocaml-calendar-devel >= 2.00
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-pprint-devel
BuildRequires: ocaml-uucp-devel
BuildRequires: ocaml-uunf-devel
BuildRequires: ocaml-uutf-devel
%endif

%description
Crowbar is a library for testing code, combining QuickCheck-style
property-based testing and the magical bug-finding powers of
[afl-fuzz](http://lcamtuf.coredump.cx/afl/).

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
%dune_build -p crowbar

%install
%dune_install crowbar

%check
%dune_check -p crowbar

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Dec 25 2025 Anton Farygin <rider@altlinux.org> 0.2.2-alt1
- Initial build for ALT Linux.

