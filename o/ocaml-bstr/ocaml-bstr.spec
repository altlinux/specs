%def_with check
Name: ocaml-bstr
Version: 0.1.1
Release: alt1
Summary: A DSL to describe binary formats
Group: Development/ML
License: MIT
Url: https://git.robur.coop/robur/bstr
VCS: https://github.com/robur-coop/bstr
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.14.0
BuildRequires: dune >= 3.5.0

%if_with check
BuildRequires: ocaml-crowbar-devel >= 0.2.2
%endif

%description
A DSL to describe binary formats

%package devel
Summary: Development files for ocaml-bstr
Requires: %name = %EVR
Group: Development/ML

%description devel
Development files for ocaml-bstr.

%prep
%setup

%build
%dune_build -p bstr

%install
%dune_install_multi bstr

%check
%dune_check -p bstr

%files -f ocaml-files.runtime.bstr

%files devel -f ocaml-files.devel.bstr

%changelog
* Sat Oct 10 2026 Anton Farygin <rider@altlinux.org> 0.1.1-alt1
- initial build for ALT Linux

