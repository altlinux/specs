%def_with check
Name: ocaml-pcre2
Version: 8.0.4
Release: alt1
Summary: Bindings to the Perl Compatibility Regular Expressions library (version 2)
Group: Development/ML
License: LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Url: https://github.com/camlp5/pcre2-ocaml
VCS: https://github.com/camlp5/pcre2-ocaml
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune

BuildRequires: ocaml-dune-configurator-devel
BuildRequires: libpcre2-devel
BuildRequires: ocaml-odoc-devel

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
pcre2-ocaml offers library functions for string pattern matching and
substitution, similar to the functionality offered by the Perl language.

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
%dune_build -p pcre2

%install
%dune_install pcre2

%check
%dune_check -p pcre2

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Fri Jan 16 2026 Anton Farygin <rider@altlinux.org> 8.0.4-alt1
- Initial build for ALT Linux.

