%define _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

%define _pseudouser_user     _uwsgi
%define _pseudouser_group    _uwsgi
%define _pseudouser_home     /var/empty

%define gemname uwsgi
%define pypi_name uWSGI
%define mod_name uwsgidecorators
%define distinfo_name uWSGI

%def_without check

Name: uwsgi
Version: 2.0.23
Release: alt2

Summary: fast (pure C), self-healing, developer-friendly WSGI server
License: GPLv2
Group: System/Servers
Url: http://projects.unbit.it/uwsgi/
Vcs: https://github.com/unbit/uwsgi.git

Source: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Source3: %name.sysconfig
Patch1: %name-2.0.15-alt-no-rpath.patch
%ifarch %e2k
Patch2000: %name-e2k.patch
%endif

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-python3
BuildRequires: libxml2-devel
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: gem(rack) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

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


%package       -n python3-module-%name
Summary:       fast (pure C), self-healing, developer-friendly WSGI server python3 module
Group:         Development/Python3
BuildArch:     noarch

%py3_provides  %name
Requires:      %name = %EVR

%description -n python3-module-%name
uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications. From the 0.9.5 release it
includes a plugin loading technology that can be used to add support for
other languages or platform. A Lua wsapi adaptor, a PSGI handler and an
Erlang message exchanger are already available.


%package       -n gem-uwsgi
Version:       2.0.23
Release:       alt2
Summary:       The uWSGI server for Ruby/Rack
Group:         Development/Ruby

Requires:      gem(rack) >= 0
Provides:      gem(uwsgi) = 2.0.23

%description   -n gem-uwsgi
The uWSGI server for Ruby/Rack library.

uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications. From the 0.9.5 release it
includes a plugin loading technology that can be used to add support for
other languages or platform. A Lua wsapi adaptor, a PSGI handler and an
Erlang message exchanger are already available.

%description   -n gem-uwsgi -l ru_RU.UTF-8
Самоцвет uwsgi.


%if_enabled    doc
%package       -n gem-uwsgi-doc
Version:       2.0.23
Release:       alt2
Summary:       The uWSGI server for Ruby/Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uwsgi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uwsgi) = 2.0.23

%description   -n gem-uwsgi-doc
The uWSGI server for Ruby/Rack documentation files.

uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications. From the 0.9.5 release it
includes a plugin loading technology that can be used to add support for
other languages or platform. A Lua wsapi adaptor, a PSGI handler and an
Erlang message exchanger are already available.

%description   -n gem-uwsgi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uwsgi.
%endif


%if_enabled    devel
%package       -n gem-uwsgi-devel
Version:       2.0.23
Release:       alt2
Summary:       The uWSGI server for Ruby/Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uwsgi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uwsgi) = 2.0.23

%description   -n gem-uwsgi-devel
The uWSGI server for Ruby/Rack development package.

uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications. From the 0.9.5 release it
includes a plugin loading technology that can be used to add support for
other languages or platform. A Lua wsapi adaptor, a PSGI handler and an
Erlang message exchanger are already available.

%description   -n gem-uwsgi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uwsgi.
%endif


%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The uwsgi daemon' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%prep
%setup
%autopatch -p1

%build
%make
%ruby_build
%python3_build_debug

%install
%python3_install
%ruby_install
install -dm0775 %buildroot%_logdir/%name

install -pDm0755 %name %buildroot%_bindir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -pDm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

%check
%ruby_test

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

%files -n python3-module-%name
%doc CONTRIBUTORS LICENSE README contrib
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/%{distinfo_name}*
%python3_sitelibdir_noarch/__pycache__/%{mod_name}*

%files         -n gem-uwsgi
%doc CONTRIBUTORS LICENSE README contrib
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-uwsgi-doc
%doc CONTRIBUTORS LICENSE README contrib
#%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-uwsgi-devel
%doc CONTRIBUTORS LICENSE README contrib
%endif


%changelog
* Wed Aug 14 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.23-alt2
- + added python3 and ruby subpackages

* Wed Nov 22 2023 Oleg Solovyov <mcpain@altlinux.org> 2.0.23-alt1
- update to 2.0.23 (Fixes: CVE-2023-27522)

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

