%define  modulename ppx_pipebang
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: A ppx rewriter that inlines reverse application operators |> and |!
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_pipebang
VCS:	https://github.com/janestreet/ppx_pipebang
BuildRequires: dune
BuildRequires: ocaml-base-devel ocaml-ppxlib-devel >= %version
Source:  %name-%version.tar

%description
A ppx rewriter that inlines the reverse application operator |>.
ppx_pipebang rewrites x |> f as f x, regardless of whether |> has
been redefined.

This inlining is mostly done for historical reasons but it also
allows f to have optional arguments (like Option.value_exn).

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
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt2
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
