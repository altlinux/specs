%define modname csv
Name: ocaml-%modname
Version: 2.4
Release: alt4
Summary: OCaml library for reading and writing CSV files
License: LGPLv2+
Group: Development/ML

Url: https://opam.ocaml.org/packages/csv/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml
BuildRequires: ocaml-uutf-devel
BuildRequires: dune
BuildRequires(pre): rpm-build-ocaml

%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%package -n csvtool
Summary: Command line tool for handling CSV files
Group:Text tools
Conflicts: %name < %EVR

%description -n csvtool
This is a handy command line tool for handling CSV files from shell
scripts based on the library ocaml-csv.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %modname,csvtool

%install
%dune_install %modname csvtool

%files -f ocaml-files.runtime

%files -n csvtool
%doc LICENSE.md
%_bindir/csvtool

%files devel -f ocaml-files.devel
%doc README.md LICENSE.md

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 2.4-alt4
- fixed build with ocaml 5.2.0

* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 2.4-alt3
- removed ocaml-findlib from BuildRequires

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 2.4-alt2
- lwt variant is removed to resolve cyclic dependencies with lwt
- csvtool moved to a separate package

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- 2.4-alt1

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 2.2-alt2
- rebuilt with ocaml-4.08

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- 2.2

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.1-alt1
- 2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- 2.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- rebuild with ocaml-extlib-devel
- added ubt

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- new version

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 1.3.1-alt1
- Initial build for ALT (2.3-0.19.svn234.fc26.src)

