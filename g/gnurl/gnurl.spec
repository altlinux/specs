Name: gnurl
Version: 7.63.0
Release: alt1

Summary: libgnurl is a fork of libcurl (use GnuTLS only)
License: MPL or MIT
Group: Networking/File transfer
Url: https://gnunet.org/gnurl

Source: https://mirror.tochlab.net/pub/gnu/gnunet/gnurl-%version.tar
Source1: %name.watch

Requires: lib%name = %EVR

BuildRequires: libgnutls-devel libgcrypt-devel
BuildRequires: groff-base libidn2-devel zlib-devel python-modules python-modules-logging python-modules-xml
#
# libpsl-devel libldap-devel libbrotli-devel libssl-devel libkrb5-devel libssh2-devel 

%package -n lib%name
Summary: The shared library for file transfer
Group: System/Libraries
Requires: ca-certificates

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description
libgnurl is a fork of libcurl with the following major changes:

Compilation requirements:
* libgnurl must be compiled so that it supports only HTTP and HTTPS
  (remove Gopher, SSH, IMAP, etc.)
* libgnurl must be compiled so that it supports only GnuTLS
  (remove CaySSL, QsoSSL, GSKit, etc.)
* removed support for NTLM, GSSAPI, SPNEGO, LDAP, metalink, HTTP2
* We recommend to build GnuTLS with DANE support, provided by 'unbound'.
  This is optional.

%description -n lib%name
This package contains lib%name shared library of functions for
sending and receiving files through various protocols, including
http and ftp.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет содержит разделяемую библиотеку функций для отправки или
получения файлов через различные сетевые протоколы, включая http и ftp.

%description -n lib%name-devel
This package contains lib%name development library of functions for
sending and receiving files through various protocols, including
http and ftp.

This package is required for development of applications that
utilize lib%name.

%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит девелоперскую библиотеку функций для отправки или
получения файлов через различные сетевые протоколы, включая http и ftp.

Этот пакет необходим для разработки приложений, использующих lib%name.

%prep
%setup

%build
./buildconf
%configure \
	--disable-ftp --disable-file \
	--disable-ldap --disable-ldaps \
	--disable-rtsp --disable-proxy \
	--disable-dict --disable-telnet \
	--disable-tftp --disable-pop3 \
	--disable-imap --disable-smb \
	--disable-smtp --disable-gopher \
	--disable-ntlm-wb \
	--disable-rpat \
	--with-ssl \
	--with-libidn \
	--without-libssh2 \
	--without-libpsl \
	--without-gssapi \
	--disable-static \
	--enable-ipv6 \
	--enable-sspi \
	--enable-threaded-resolver \
	--with-ca-bundle=%_datadir/ca-certificates/ca-bundle.crt

%make_build

%install
%makeinstall_std
#makeinstall_std -C docs/libcurl

#check
#make_build -k test

%files
%_bindir/%name
%_man1dir/%name.1*

%files -n lib%name
%_libdir/*.so.*

%doc CHANGES README* docs/{FAQ,FEATURES}

%files -n lib%name-devel
%_libdir/*.so
%_libdir/pkgconfig/lib%name.pc
%_bindir/%name-config
%_aclocaldir/lib%name.m4
%_includedir/*
%_man3dir/*
%_man1dir/%name-config.1*
%doc docs/{THANKS,BUGS,RESOURCES,TheArtOfHttpScripting,TODO,examples}

%changelog
* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 7.63.0-alt1
- new version 7.63.0 (with rpmrb script)

* Mon Dec 03 2018 Vitaly Lipatov <lav@altlinux.ru> 7.62.0-alt1
- initial build for ALT Sisyphus
