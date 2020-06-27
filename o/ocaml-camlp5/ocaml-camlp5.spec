%define module camlp5
Name: ocaml-camlp5
Version: 7.12
Release: alt1

Summary: preprocessor-pretty-printer of OCaml
License: BSD-style
Group: Development/ML
Url: https://camlp5.github.io/

Source: %name-%version.tar
Source2: META.src
Patch1: camlp5-5.08-alt-dynlink.patch
Provides: camlp5 = %EVR
Obsoletes: camlp5 < %EVR
BuildRequires: ocaml >= 4.08.1

%description
Camlp5 is a preprocessor-pretty-printer of OCaml.
It is compatible with OCaml versions from 3.08.0 to 3.11 included.

This package is compiled in 'transitional' mode, to simplify
compilation of older packages (e.g. ocamlnet).

%prep
%setup -q
%patch1 -p1

%build
./configure --strict --mandir %_mandir
%make world.opt

sed -e 's,@NAME@,%module,' %SOURCE2 > META

%install
%make_install DESTDIR=%buildroot install

install -p -m644 compile/pa_o_fast.cmi %buildroot%_libdir/ocaml/%module/
install -pD -m644 META %buildroot%_libdir/ocaml/site-lib/%module/META

%files
%_bindir/%{module}*
%_bindir/mk%{module}*
%_bindir/ocpp5
%_libdir/ocaml/%module
%_libdir/ocaml/site-lib/%module
%_man1dir/*5*.1*

%changelog
* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 7.12-alt1
- 7.12

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 7.11-alt1
- 7.11

* Mon Oct 07 2019 Anton Farygin <rider@altlinux.ru> 7.10-alt1
- 7.10

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 7.08-alt1
- 7.08 release

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 7.08-alt0.g7abc971d
- up to 7.08 from upstream git
- renamed to ocaml-camlp5

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 7.07-alt1
- 7.07

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 7.06-alt1
- 7.06

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 7.05-alt1
- 7.05

* Mon Dec 18 2017 Anton Farygin <rider@altlinux.ru> 7.03-alt1
- 7.03

* Tue Jul 04 2017 Anton Farygin <rider@altlinux.ru> 7.00-alt1
- 7.00

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 6.17-alt2
- rebuild with ocaml 4.04.1

* Tue Mar 28 2017 Anton Farygin <rider@altlinux.ru> 6.17-alt1
- new version

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 6.02.3-alt1
- 6.02.3-1

* Thu Apr 10 2008 Alexey Tourbin <at@altlinux.ru> 5.08-alt1
- 5.03 -> 5.08
- alt-dynlink.patch: don't link in a copy of dynlink.cma

* Wed Nov 21 2007 Alex V. Myltsev <avm@altlinux.ru> 5.03-alt1
- Initial build for Sisyphus.
