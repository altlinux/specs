%define _unpackaged_files_terminate_build 1

%def_with check

Name: apache2-mod_wsgi
Version: 5.0.0
Release: alt1

Summary: Python WSGI module for Apache2
Group: System/Servers
License: Apache-2.0
Url: http://www.modwsgi.org
Vcs: https://github.com/GrahamDumpleton/mod_wsgi

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): apache2-devel
BuildRequires: python3-dev

%if_with check
BuildRequires: nss_wrapper
BuildRequires: socket_wrapper
BuildRequires: pytest3
BuildRequires: python3-module-requests
%endif

%description
The mod_wsgi package implements a simple to use Apache module which can host
any Python web application which supports the Python WSGI specification.

%package py3
Summary: Python3 WSGI module for Apache2
Group: System/Servers
Requires: apache2 >= %apache2_version
Provides: mod_wsgi-py3 = %EVR

%description py3
The mod_wsgi-py3 package implements a simple to use Apache module which can
host any Python3 web application which supports the Python3 WSGI specification.

%prep
%setup
%autopatch -p1

%build
%add_optflags -fno-strict-aliasing
%configure --with-apxs=%apache2_apxs --with-python=python3
%make

%install
mkdir -p %buildroot%apache2_mods_available
%makeinstall_std
mv %buildroot%apache2_moduledir/mod_wsgi{,-py3}.so
echo -e '<IfModule !wsgi_module>\n\tLoadModule wsgi_module %apache2_moduledir/mod_wsgi-py3.so\n</IfModule>' > \
    %buildroot%apache2_mods_available/wsgi-py3.load

%check
%make check DESTDIR=%buildroot

%files
%files py3
%doc README*.*
%apache2_moduledir/mod_wsgi-py3.so
%config(noreplace) %apache2_mods_available/wsgi-py3.load

%changelog
* Tue Dec 19 2023 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.9.4 -> 5.0.0.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 4.9.4-alt1
- 4.9.0 -> 4.9.4.

* Wed Sep 01 2021 Stanislav Levin <slev@altlinux.org> 4.9.0-alt1
- 4.8.0 -> 4.9.0.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 4.8.0-alt2
- Dropped unused dependency on pytest.

* Tue May 25 2021 Stanislav Levin <slev@altlinux.org> 4.8.0-alt1
- 4.7.1 -> 4.8.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 4.7.1-alt2
- Stopped Python2 package build (Python2 EOL).

* Sun May 03 2020 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- New version.

* Tue Dec 24 2019 Stanislav Levin <slev@altlinux.org> 4.7.0-alt1
- 4.6.8 -> 4.7.0.

* Fri Oct 11 2019 Stanislav Levin <slev@altlinux.org> 4.6.8-alt1
- 4.6.7 -> 4.6.8.

* Thu Aug 01 2019 Stanislav Levin <slev@altlinux.org> 4.6.7-alt1
- 4.6.5 -> 4.6.7.

* Mon Oct 22 2018 Stanislav Levin <slev@altlinux.org> 4.6.5-alt1
- 4.6.4 -> 4.6.5.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.6.4-alt2.qa1
- NMU: applied repocop patch

* Fri Jun 01 2018 Stanislav Levin <slev@altlinux.org> 4.6.4-alt2
- Build with python3
- Add basic tests

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt1
- New version.

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt1
- New version.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.24-alt1
- New version.

* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.23-alt1
- New version.

* Sun Nov 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.22-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.21-alt1
- New version.

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.20-alt1
- New version

* Sun Oct 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.19-alt1
- New version

* Thu Aug 31 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.18-alt1
- New version

* Sun Jul 09 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.17-alt1
- New version

* Tue Mar 14 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.15-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.14-alt1
- new version 4.5.14

* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.13-alt1
- new version 4.5.13

* Mon Dec 19 2016 Andrey Cherepanov <cas@altlinux.org> 4.5.11-alt1
- new version 4.5.11

* Wed Apr 06 2016 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- New version

* Tue Apr 05 2016 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1.2
- Rebuild with new apache2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3-alt1.1
- Rebuild with Python-2.7

* Fri Nov 26 2010 Michael A. Kangin <prividen@altlinux.org> 3.3-alt1
- new version

* Sun Dec 20 2009 Alexey Morsov <swi@altlinux.ru> 3.1-alt1
- new version

* Sat Nov 28 2009 Alexey Morsov <swi@altlinux.ru> 2.8-alt1
- new version

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Wed Sep 09 2009 Alexey Morsov <swi@altlinux.ru> 2.5-alt1
- new version

* Thu Sep 04 2008 Alexey Morsov <swi@altlinux.ru> 2.3-alt1
- initial build

