Name: ocaml-afl-persistent
Version: 1.4
Release: alt1
Summary: Use afl-fuzz in persistent mode
Group: Development/ML
License: MIT
Url: https://github.com/stedolan/ocaml-afl-persistent
VCS: https://github.com/stedolan/ocaml-afl-persistent
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.05
BuildRequires: dune >= 2.9

%description
afl-fuzz normally works by repeatedly fork()ing the program being
tested. using this package, you can run afl-fuzz in 'persistent mode',
which avoids repeated forking and is much faster.

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
%dune_build -p afl-persistent

%install
%dune_install afl-persistent

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Dec 25 2025 Anton Farygin <rider@altlinux.org> 1.4-alt1
- Initial build for ALT Linux.
