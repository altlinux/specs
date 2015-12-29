%define oname engine_pkcs11
%def_disable static

Summary: PKCS#11 engine for OpenSSL
Name: openssl-%oname
Version: 0.2.0
Release: alt1
License: BSD
Group: System/Libraries
# https://github.com/OpenSC/engine_pkcs11.git
Source: %name-%version.tar
Url: https://github.com/OpenSC/engine_pkcs11.git

BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(libp11) >= 0.2.5
BuildRequires: pkgconfig(libcrypto) >= 0.9.7 pkgconfig(openssl) >= 0.9.7


%description
Engine_pkcs11 is an implementation of an engine for OpenSSL. It can be loaded
using code, config file or command line and will pass any function call by
openssl to a PKCS#11 module. Engine_pkcs11 is meant to be used with smart cards
and software for using smart cards in PKCS#11 format, such as OpenSC. Originaly
this engine was a part of OpenSC, until OpenSC was split into several small
projects for improved flexibility.

%prep
%setup
cat > README.ALT <<EOF
In ALTLinux, the engine file has been placed in the
%_libdir/openssl/engines directory instead of the default
%_libdir/engines. This was done so in order to match our openssl
installation.

Considering this new path, below is the suggested change to openssl.cnf
in order to use this engine:

openssl_conf = openssl_def

[openssl_def]
engines = engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
dynamic_path = %_libdir/openssl/engines/engine_pkcs11.so
MODULE_PATH = %_libdir/opensc-pkcs11.so
init = 0

EOF

chmod 0644 README.ALT

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--with-enginesdir=%_libdir/openssl/engines

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README.md README.ALT NEWS
%_libdir/openssl/engines/*.so

%changelog
* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 0.1.8-alt2.qa2
- NMU: rebuilt against recent libp11

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.8-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.1.8-alt2
- rebuild with new openssl

* Tue Jun 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Tue Nov 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Sun Aug 30 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Thu Jan 15 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Sun Dec 23 2007 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt0.1
- packaged for ALTLinux

