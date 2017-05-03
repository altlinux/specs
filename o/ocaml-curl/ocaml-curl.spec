%global pkgname curl
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 0.7.9
Release: alt2%ubt
Summary: OCaml Curl library (ocurl)
License: MIT
Group: Development/ML
Url: http://ocurl.forge.ocamlcore.org/
# https://github.com/ygrek/ocurl
Source0: %name-%version.tar

BuildRequires: ocaml ocaml-findlib libcurl-devel
BuildRequires(pre):rpm-build-ubt

%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
# Parallel builds don't work.
unset MAKEFLAGS

# Add -fPIC to avoid:
# /usr/bin/ld: /usr/lib64/ocaml/curl/libcurl-helper.a(curl-helper.o):
# relocation R_X86_64_32S against `.rodata' can not be used when
# making a shared object; recompile with -fPIC
CFLAGS="%optflags -fPIC" \
%configure --libdir=%_libdir --with-findlib
make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%ocamlsitelib  %buildroot%ocamlstublib 
make install

# Make clean in the examples dir so our docs don't contain binaries.
make -C examples clean

%files
%doc COPYING
%pkgsitelib
%exclude %pkgsitelib/*.mli
%ocamlstublib/*.so
%ocamlstublib/*.so.owner

%files devel
%doc examples/*
%pkgsitelib/*.mli

%changelog
* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.7.9-alt2%ubt
- rebuild with ocaml 4.04.1

* Sun Apr 16 2017 Anton Farygin <rider@altlinux.ru> 0.7.9-alt1%ubt
- first build for ALT
