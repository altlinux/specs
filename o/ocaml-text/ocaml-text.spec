# on i586: ./usr/lib/ocaml/text/text.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed

Name: ocaml-text
License: BSD
Group: Development/ML
Summary: Development files for %name-runtime
Version: 0.8
Release: alt4%ubt
Url: https://github.com/vbmithr/ocaml-text
Source: %name-%version.tar
Patch0: ocaml-text-alt-fix-rpath.patch
Requires: %name-runtime = %version-%release

BuildRequires: ocaml ocaml-ocamldoc ocaml-ocamlbuild ocaml-findlib ocaml-camlp4-devel
BuildRequires: ocaml-pcre libncurses-devel
BuildRequires(pre): rpm-build-ubt

%description
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way

It supports:

  - character encoding/decoding using iconv
  - manipulation of text as UTF-8 encoded strings
  - localised text functions such as compare, upper, ...
  - human readable regular expression inside patterns

In order to be the compatible with other ocaml library without pain,
OCaml-Text choose to use only regular strings for dealing with text.

This package contains the development files needed to build applications
using %name.

%package runtime
Summary: Ocaml-text is a library for manipulation of unicode text
Group: Development/ML

%description runtime
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way

It supports:

  - character encoding/decoding using iconv
  - manipulation of text as UTF-8 encoded strings
  - localised text functions such as compare, upper, ...
  - human readable regular expression inside patterns

In order to be the compatible with other ocaml library without pain,
OCaml-Text choose to use only regular strings for dealing with text.

%prep
%setup
%patch0 -p1

%build
ocaml setup.ml -configure --prefix %_prefix --destdir '%buildroot' --enable-pcre 
make

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
%makeinstall_std OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml

%files runtime
%_libdir/ocaml/text
%_libdir/ocaml/stublibs/*.so*
%exclude %_libdir/ocaml/text/*.a
%exclude %_libdir/ocaml/text/*.cmxa
%exclude %_libdir/ocaml/text/*.mli

%files
%doc LICENSE CHANGES  README
%_libdir/ocaml/text/*.a
%_libdir/ocaml/text/*.cmxa
%_libdir/ocaml/text/*.mli

%changelog
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.8-alt4%ubt
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.8-alt3%ubt
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 0.8-alt2%ubt
- rebuild in new environment

* Wed Apr 12 2017 Anton Farygin <rider@altlinux.ru> 0.8-alt1%ubt
- updated to 0.8

* Tue Apr 11 2017 Anton Farygin <rider@altlinux.ru> 0.6-alt1
- updated to 0.6

* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- initial build
