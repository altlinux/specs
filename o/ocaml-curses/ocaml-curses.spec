%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-curses
Version: 1.0.11
Release: alt1
Summary: OCaml bindings for ncurses
Group: Development/ML
License: LGPLv2.1
Url: https://github.com/mbacarella/curses
Source: %name-%version.tar

BuildRequires: ocaml
BuildRequires: rpm-build-ocaml dune ocaml-dune-configurator-devel
BuildRequires: libncursesw-devel

%description
OCaml bindings for ncurses.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup


%build
%dune_build --release @install

%install
%dune_install

%files -f ocaml-files.runtime
%doc COPYING

%files devel -f ocaml-files.devel
%doc COPYING

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Sun Jun 28 2020 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.0.3-alt8
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt7
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt6
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt5
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt4
- rebuild with ocaml 4.04.2

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- moved out from site-lib dir
- added ubt tag

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- rebuild with new ocaml

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-33.fc26.src)

