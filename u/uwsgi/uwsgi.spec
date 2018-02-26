%define _pseudouser_user     _uwsgi
%define _pseudouser_group    _uwsgi
%define _pseudouser_home     /var/empty

Name: uwsgi
Version: 0.9.6.5
Release: alt1.2

Summary: fast (pure C), self-healing, developer-friendly WSGI server
License: GPLv2
Group: System/Servers

Url: http://projects.unbit.it/uwsgi/

Source: %name-%version.tar
Patch: %name-0.9.6.5-alt-no-Werror.patch

BuildRequires: libxml2-devel python-devel

%description
uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications. From the 0.9.5 release it
includes a plugin loading technology that can be used to add support for
other languages or platform. A Lua wsapi adaptor, a PSGI handler and an
Erlang message exchanger are already available.

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The uwsgi daemon' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%prep
%setup
%patch -p1

%build
%make

%install
install -dm0775 %buildroot%_logdir/%name

install -pDm0755 %name %buildroot%_sbindir/%name
install -pDm0755 altlinux/%name.init %buildroot%_initdir/%name
install -pDm0644 altlinux/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 altlinux/%name.logrotate %buildroot%_sysconfdir/logrotate.d/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%dir %attr(0775,root,%_pseudouser_group) %_logdir/%name
%config %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%doc ChangeLog README contrib django

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.5-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6.5-alt1.1
- Rebuild with Python-2.7

* Mon Oct 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.6.5-alt1
- 0.9.6.5
- uwsgi.init: wait for daemon shutdown in stop()

* Mon Jun 21 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.5.1-alt2
- uwsgi.init: use SIGQUIT for stopping uwsgi.
- uwsgi.init: never use reload().

* Fri Jun 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.5.1-alt1
- Initial build for Sisyphus.

