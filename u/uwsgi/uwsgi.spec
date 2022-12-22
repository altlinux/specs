%define _pseudouser_user     _uwsgi
%define _pseudouser_group    _uwsgi
%define _pseudouser_home     /var/empty

Name: uwsgi
Version: 2.0.21
Release: alt1

Summary: fast (pure C), self-healing, developer-friendly WSGI server
License: GPLv2
Group: System/Servers

Url: http://projects.unbit.it/uwsgi/

Source: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Source3: %name.sysconfig
Patch1: %name-2.0.15-alt-no-rpath.patch
Patch2000: %name-e2k.patch

BuildRequires: libxml2-devel python3-devel

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
%patch1 -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%make

%install
install -dm0775 %buildroot%_logdir/%name

install -pDm0755 %name %buildroot%_bindir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -pDm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%dir %attr(0775,root,%_pseudouser_group) %_logdir/%name
%config %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%doc README contrib

%changelog
* Thu Dec 22 2022 Oleg Solovyov <mcpain@altlinux.org> 2.0.21-alt1
- update to 2.0.21

* Tue Dec 07 2021 Oleg Solovyov <mcpain@altlinux.org> 2.0.20-alt1
- update to 2.0.20

* Mon Dec 06 2021 Oleg Solovyov <mcpain@altlinux.org> 2.0.18-alt3
- Moved /usr/sbin/uwsgi -> /usr/bin/uwsgi (Closes: #41510)

* Thu Sep 02 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.18-alt2
- Added patch for Elbrus

* Mon Nov 18 2019 Oleg Solovyov <mcpain@altlinux.org> 2.0.18-alt1
- update to 2.0.18
- built with python3

* Thu Nov 02 2017 Oleg Solovyov <mcpain@altlinux.org> 2.0.15-alt1
- update to 2.0.15

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.6.5-alt1.2.qa1
- NMU: rebuilt for updated dependencies.

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

