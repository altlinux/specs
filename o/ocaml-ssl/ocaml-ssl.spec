Name: ocaml-ssl
Version: 0.4.6
Release: alt1

Summary: OCaml bindings for the OpenSSL library
License: LGPLv2.1 with exemptions
Group: Development/ML
Url: http://savonet.sourceforge.net/wiki/OCamlLibs
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: findlib libssl-devel

BuildRequires(pre): ocaml
Requires: ocaml = %{get_version ocaml}

# .so file always needed to link stuff with %name
Requires: libssl-devel

%description
This package contains OCaml bindings for libssl.

Install it if you intend to develop
SSL-enabled applications in OCaml.

%prep
%setup

%build
%configure --disable-ldconf
%make

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
mkdir -p %buildroot/%ocamlsitelib
%make_install OCAMLFIND_INSTFLAGS="-destdir %buildroot/%ocamlsitelib" install

%files
%ocamlsitelib/ssl

%changelog
* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jan 06 2008 Alex V. Myltsev <avm@altlinux.ru> 0.4.2-alt1
- Initial build for Sisyphus
