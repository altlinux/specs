%def_without check
Name: ocaml-ISO8601
Version: 0.2.6
Release: alt1
Summary: ISO 8601 and RFC 3999 date parsing for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/ISO8601.ml
VCS: https://github.com/ocaml-community/ISO8601.ml
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-odoc-devel

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
ISO 8601 and RFC 3999 date parsing for OCaml

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
%dune_build -p ISO8601

%install
%dune_install ISO8601

%check
%dune_check -p ISO8601

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Jan 18 2026 Anton Farygin <rider@altlinux.org> 0.2.6-alt1
- Initial build for ALT Linux.

