%set_verify_elf_method textrel=relaxed
Name: ocaml-trie
Version: 1.0.0
Release: alt2
Summary: Strict impure trie tree

Group: Development/ML
License: MIT
Url: https://github.com/kandu/trie
Source: %name-%version.tar

BuildRequires: dune ocaml 
BuildRequires: rpm-build-ocaml >= 1.4

%description
%summary.

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
%dune_build -p trie

%install
%dune_install

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Tue Oct 13 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- migrated to rpm-build-ocaml 1.4

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
