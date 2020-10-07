Summary:    Small, simple HTTP daemon, supports SSL
Name:       mini_httpd
Version:    1.30
Release:    alt1
License:    freely distributable
Group:      Networking/WWW
Source0:    %name-%version.tar
Source1:    %name.init
Source2:    %name.config
URL:        http://www.acme.com/software/mini_httpd/
Packager:   Andriy Stepanov <stanv@altlinux.ru>

BuildRequires:    openssl-devel >= 0.9.7d
Requires: webserver-common

%define     htmldir /var/www/html

%description
Simple and small HTTP daemon supporting SSL.

%package -n %name-htpasswd
Summary:    mini_httpd htpasswd utility
Group:      Networking/WWW
Provides:   htpasswd
Obsoletes:  htpasswd

%description -n %name-htpasswd
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from mini_httpd; it supports only CRYPT
encryption algorithm.

%package -n %name-single
Summary:    mini_httpd htpasswd utility
Group:      Networking/WWW

%description -n %name-single
Simple and small HTTP daemon without supporting SSL.

%prep
%setup -q
#ALT 39048
sed -i  's/htpasswd/mini_htpasswd/g' Makefile
mv htpasswd.c mini_htpasswd.c
mv htpasswd.1 mini_htpasswd.1

%build
# Build single version without SSL support
%make \
    BINDIR=%_bindir \
    MANDIR=%_mandir \
    CFLAGS="%optflags -fno-strict-aliasing $CFLAGS"
    mv %name %name-single

%make clean

%make \
    SSL_INCDIR=%_includedir/openssl \
    SSL_LIBDIR=%_libdir \
    SSL_DEFS=-DUSE_SSL \
    SSL_INC=-I%_includedir/openssl \
    SSL_LIBS='-lssl -lcrypto' \
    BINDIR=%_bindir \
    MANDIR=%_mandir \
    CFLAGS="-DUSE_SSL -I%_includedir/openssl %optflags -fno-strict-aliasing $CFLAGS"


%install
rm -rf %buildroot
install -d %buildroot/etc/rc.d/init.d
install -d %buildroot%_bindir
install -d %buildroot%_mandir/man{1,8}
install -d %buildroot%_sysconfdir/sysconfig

install mini_httpd          %buildroot%_bindir
install mini_httpd-single   %buildroot%_bindir
install mini_htpasswd       %buildroot%_bindir/mini_htpasswd
install mini_htpasswd.1     %buildroot%_man1dir/mini_htpasswd.1
install *.8                 %buildroot%_man8dir

install %SOURCE1            %buildroot/%_initdir/%name

sed -e 's,@DOCROOT@,%htmldir,' %SOURCE2 > %buildroot/%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README
%attr(755,root,root) %_bindir/%name
%attr(754,root,root) %_initdir/%name
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/%name
%_man8dir/*

%files -n %name-htpasswd
%attr(755,root,root) %_bindir/mini_htpasswd
%_mandir/man1/mini_htpasswd.1*

%files -n %name-single
%attr(755,root,root) %_bindir/%name-single

%changelog
* Wed Oct 07 2020 Grigory Ustinov <grenka@altlinux.org> 1.30-alt1
- Build new version.
- Fix htpasswd name conflict (#39048).

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.19-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Feb 17 2012 Andriy Stepanov <stanv@altlinux.ru> 1.19-alt2
- Update init script

* Fri Feb 17 2012 Andriy Stepanov <stanv@altlinux.ru> 1.19-alt1
- Initial build for Sisyphus

