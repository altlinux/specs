%define ocamlmod fileutils
Name: ocaml-%ocamlmod
Version: 0.6.4
Release: alt1
Summary: OCaml library for common file and filename operations
Group: Development/ML
License: LGPLv2.1 with OCaml-LGPL-linking-exception
VCS: https://github.com/gildor478/ocaml-fileutils
Url: https://forge.ocamlcore.org/projects/ocaml-fileutils/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml dune ocaml-ounit-devel

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
sed -i '/stdlib-shims/d;/seq/d' *.opam
sed -i 's/stdlib-shims//;s/seq//' *.opam src/lib/fileutils/dune test/dune
%dune_build -p %ocamlmod

%install
%dune_install %ocamlmod

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel
%doc LICENSE.txt CHANGES.md README.md

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 0.6.4-alt1
- 0.6.3 -> 0.6.4
- added patch from fedora with fix broken FuleUtils.cmp

* Mon Jan 10 2022 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1
- 0.5.3 -> 0.6.3

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.5.3-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- rebuilt with ocaml-4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- rebuilt for ocaml-4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- new version

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt3
- moved out from site-lib dir
- added ubt tag

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt3
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt2
- rebuild with ocaml-4.04

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- Initial build for ALT (based on 0.5.1-2.fc26.src)

