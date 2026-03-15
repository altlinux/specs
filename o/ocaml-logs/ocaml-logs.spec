%define libname logs
Name:           ocaml-%libname
Version: 0.10.0
Release: alt1
Summary:        Logging infrastructure for OCaml
License:        ISC
Group:          Development/ML
Url:            https://erratique.ch/software/logs
VCS: https://github.com/dbuenzli/logs
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml-findlib-devel ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1
BuildRequires: ocaml-opam-installer
BuildRequires: ocaml-fmt-devel ocaml-lwt-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6.1

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Logs provides a logging infrastructure for OCaml. Logging is performed on sources 
whose reporting level can be set independently. Log message report is decoupled 
from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and the API 
easily allows to implement your own.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q
%patch0 -p1

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml pkg/pkg.ml build --with-js_of_ocaml-compiler false \
                       --with-lwt true

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel
%_ocamldir/logs/top/logs_top_init_ml

%changelog
* Sun Mar 15 2026 Anton Farygin <rider@altlinux.org> 0.10.0-alt1
- 0.9.0 -> 0.10.0

* Sun Jan 11 2026 Anton Farygin <rider@altlinux.org> 0.9.0-alt1
- 0.7.0 -> 0.9.0

* Wed Jan 22 2025 Anton Farygin <rider@altlinux.ru> 0.7.0-alt3
- changed BR - use ocaml-findlib-devel instead of the ocaml-findlib

* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.7.0-alt2
- added support for bytecode-only version of the ocaml package

* Tue Mar 23 2021 Anton Farygin <rider@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 0.6.3-alt3
- built with lwt support

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2
- built without js_of_ocaml against cyclic dependencies

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.6.2-alt3
- rebuilt with js_of_ocaml

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.6.2-alt2
- rebuild with js_of_ocaml 3.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.6.2-alt1
- first build for ALT

