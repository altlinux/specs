Name: ocaml-ssl
Version: 0.5.3
Release: alt1%ubt
Summary: OCaml bindings for the OpenSSL library
License: LGPLv2.1 with exemptions
Group: Development/ML
Url: https://github.com/savonet/ocaml-ssl
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: ocaml-findlib libssl-devel

BuildRequires(pre): ocaml rpm-build-ubt

# .so file always needed to link stuff with %name
Requires: libssl-devel

%description
This package contains OCaml bindings for libssl.

Install it if you intend to develop
SSL-enabled applications in OCaml.

%prep
%setup
%patch0 -p1
%build
autoreconf -fisv
%configure --disable-ldconf
%make

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
mkdir -p %buildroot/%ocamlsitelib
%make_install OCAMLFIND_INSTFLAGS="-destdir %buildroot/%ocamlsitelib" install

%files
%ocamlsitelib/ssl

%changelog
* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1%ubt
- 0.5.3

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jan 06 2008 Alex V. Myltsev <avm@altlinux.ru> 0.4.2-alt1
- Initial build for Sisyphus
