%define _unpackaged_files_terminate_build 1

%def_with check

Name: apache2-mod_wsgi
Version: 4.7.0
Release: alt1

Summary: Python WSGI module for Apache2
Group: System/Servers
License: Apache-2.0
# Source-git: https://github.com/GrahamDumpleton/mod_wsgi
Url: http://www.modwsgi.org

Source: %name-%version.tar
Patch0: 0001-Add-basic-tests.patch

BuildRequires(pre): apache2-devel
BuildRequires: python-devel
BuildRequires: python3-dev

%if_with check
BuildRequires: nss_wrapper
BuildRequires: socket_wrapper
BuildRequires: pytest
BuildRequires: python-module-nose
BuildRequires: python-module-requests
BuildRequires: pytest3
BuildRequires: python3-module-nose
BuildRequires: python3-module-requests
%endif

Requires: apache2 >= %apache2_version
Provides: mod_wsgi = %EVR

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
%patch0 -p1
cp -a . ../wsgi-py3

%build
%add_optflags -fno-strict-aliasing
%configure --with-apxs=%apache2_apxs --with-python=python
%make

pushd ../wsgi-py3
%configure --with-apxs=%apache2_apxs --with-python=python3
%make
popd

%install

mkdir -p %buildroot%apache2_mods_available
pushd ../wsgi-py3
%makeinstall_std
mv %buildroot%apache2_moduledir/mod_wsgi{,-py3}.so
echo -e '<IfModule !wsgi_module>\n\tLoadModule wsgi_module %apache2_moduledir/mod_wsgi-py3.so\n</IfModule>' > \
    %buildroot%apache2_mods_available/wsgi-py3.load
popd

%makeinstall_std
echo -e '<IfModule !wsgi_module>\n\tLoadModule wsgi_module %apache2_libexecdir/mod_wsgi.so\n</IfModule>' > \
    %buildroot%apache2_mods_available/wsgi.load

%check
%make check DESTDIR=%buildroot

pushd ../wsgi-py3
%make check DESTDIR=%buildroot
popd

%files
%doc *.rst LICENSE
%apache2_moduledir/mod_wsgi.so
%config(noreplace) %apache2_mods_available/wsgi.load

%files py3
%doc *.rst LICENSE
%apache2_moduledir/mod_wsgi-py3.so
%config(noreplace) %apache2_mods_available/wsgi-py3.load

%changelog
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



