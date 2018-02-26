%def_without M24

%if_with M24
%define _release alt0.M24.1
%else
%define _release alt1
%endif

Name: trac-spawn-fcgi
Version: 0.2
Release: %_release
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Trac FastCGI frontend spawn daemon
License: BSD
Group: Development/Other

# taken from lighttpd-1.4.13
Source0: spawn-fcgi-1.4.13.c
Source1: spawn-fcgi.copying

Source2: %name-0.1-alt-init
Source3: %name-0.1-alt-sysconfig

%description
This package contains trac FastCGI frontend spawn daemon
for use with web server like nginx.

%prep
%setup -q -c -T
install -m644 %SOURCE0 %name.c
install -m644 %SOURCE1 COPYING.spawn-fcgi
cat << _EOF > sys-socket.h
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <sys/un.h>
#include <arpa/inet.h>
_EOF

%build
cc -g %optflags \
	-DHAVE_PWD_H \
	-DHAVE_GETOPT_H \
	-DHAVE_SYS_WAIT_H \
	-DHAVE_SOCKLEN_T \
	-DHAVE_SYS_UN_H \
	-DPACKAGE_VERSION=\"1.4.10\" \
	-o %name %name.c

%install
mkdir -p %buildroot{%_bindir,%_initdir,%_sysconfdir/sysconfig,%_var/run/%name}
install -m755 %name %buildroot%_bindir/%name
install -m755 %SOURCE2 %buildroot%_initdir/%name
install -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
touch %buildroot%_var/run/%name/%name.pid

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING.spawn-fcgi
%_bindir/%name
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_var/run/%name/
%ghost %_var/run/%name/%name.pid

%changelog
* Sun Mar 25 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Update spawn-fcgi.c to version 1.4.13.

* Tue Mar 14 2006 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux
