Name: camlp5
Version: 6.17
Release: alt1%ubt

Summary: preprocessor-pretty-printer of OCaml
License: BSD-style
Group: Development/ML
Url: https://camlp5.github.io/

Source: %name-%version.tar
Source2: META.src
Patch1: camlp5-5.08-alt-dynlink.patch

BuildRequires: ocaml
BuildRequires(pre): rpm-build-ubt

%description
Camlp5 is a preprocessor-pretty-printer of OCaml.
It is compatible with OCaml versions from 3.08.0 to 3.11 included.

This package is compiled in 'transitional' mode, to simplify
compilation of older packages (e.g. ocamlnet).

%prep
%setup -q
%patch1 -p1

%build
./configure --transitional --mandir %_mandir
%make world.opt

sed -e 's,@NAME@,%name,' %SOURCE2 > META

%install
%make_install DESTDIR=%buildroot install

install -p -m644 compile/pa_o_fast.cmi %buildroot%_libdir/ocaml/%name/
install -pD -m644 META %buildroot%_libdir/ocaml/site-lib/%name/META

%files
%_bindir/%{name}*
%_bindir/mk%{name}*
%_bindir/ocpp5
%_libdir/ocaml/%name
%_libdir/ocaml/site-lib/%name
%_man1dir/*5*.1*

%changelog
* Tue Mar 28 2017 Anton Farygin <rider@altlinux.ru> 6.17-alt1%ubt
- new version

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 6.02.3-alt1
- 6.02.3-1

* Thu Apr 10 2008 Alexey Tourbin <at@altlinux.ru> 5.08-alt1
- 5.03 -> 5.08
- alt-dynlink.patch: don't link in a copy of dynlink.cma

* Wed Nov 21 2007 Alex V. Myltsev <avm@altlinux.ru> 5.03-alt1
- Initial build for Sisyphus.
