# SPEC file for litmus package

Name:    litmus
Version: 0.12.1
Release: alt3

Summary: a WebDAV server test suite
Summary(ru_RU.UTF-8): утилита тестирования серверов WebDAV

License: %gpl2plus
Group:   Networking/File transfer
URL:     http://webdav.org/neon/litmus/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %url/%name-%version.tar
Patch0: litmus-0.12.1-alt-neon_0.29.0.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2011
BuildRequires: libexpat-devel libkeyutils-devel libneon-devel libssl-devel zlib-devel

%description
litmus is a WebDAV server test suite, which aims to test whether
a server is compliant with the  WebDAV protocol  as specified in
RFC2518.

Current tests covers  OPTIONS, PUT, GET, MKCOL, DELETE, COPY and
MOVE methods, property manipulation and querying, locking.

Note that a server which passes all these tests will not
necessarily work with any real DAV clients; though the chances
are good. litmus is built using the neon library, so supports
digest and basic authentication, TLS/SSL, and proxy servers.


%prep
%setup
%patch0
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
./autogen.sh
%configure --with-ssl=openssl --with-neon \
	--enable-warnings \
	--with-ca-bundle=%_datadir/ca-certificates/ca-bundle.crt \
	--with-expat
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files  -f %name.lang
%doc FAQ README THANKS TODO ChangeLog NEWS
%doc --no-dereference COPYING

%_bindir/%name
%_libexecdir/%{name}*
%_datadir/%{name}*

%changelog
* Sun Mar 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt3
- Rebuild with libneon-0.29.5-alt1

* Mon Nov 23 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt2
- Rebuild with libneon-0.29.0-alt1

* Tue Jul 14 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt1
- Initial build for ALT Linux Sisyphus
