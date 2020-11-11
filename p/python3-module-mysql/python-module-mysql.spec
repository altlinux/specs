%define oname mysql-connector-python
#def_with bootstrap

Name: python3-module-mysql
Version: 8.0.22
Release: alt1

Summary: MySQL Connector for Python 3

License: GPLv2 with exceptions
Group: Development/Python3
Url: http://dev.mysql.com/doc/connector-python/en/index.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

Provides: %{oname}3 = %version

# TODO: we miss The _mysql_connector C Extension Module
%add_python3_req_skip _mysql_connector

%description
MySQL driver written in Python which does not depend on MySQL C client
libraries and implements the DB API v2.0 specification (PEP-249).

%package django
Summary: Django MySQL Connector for Python 3
Group: Development/Python3
Requires: %name = %EVR

%if_with bootstrap
%add_python3_req_skip django
%add_python3_req_skip django.db.backends.creation django.db.backends.schema
%endif

%description django
DJango connector for %name.

%prep
%setup -n %oname-%version

%build
%python3_build_debug
cd build ; ln -s lib.linux* lib ; cd ..

%install
%python3_install
%python3_prune

%files
%doc CHANGES.txt LICENSE.txt README.rst
%doc examples
%python3_sitelibdir/mysql/
%python3_sitelibdir/mysqlx/
%exclude %python3_sitelibdir/mysql/connector/django
%python3_sitelibdir/mysql_connector_python-%version-py3*.egg-info

%files django
%python3_sitelibdir/mysql/connector/django/

%changelog
* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 8.0.22-alt1
- new version 8.0.22 (with rpmrb script) (ALT bug 39255)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt2
- build python3 package separately

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt1
- new version 2.1.7 (with rpmrb script)

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.4-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 26 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)

* Sat Sep 20 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- import archive mysql-connector-python-1.2.3

* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- initial build for ALT Linux Sisyphus

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- version 1.1.6 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1-6.html

* Tue Feb  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- version 1.1.5 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1-5.html

* Tue Dec 17 2013 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- version 1.1.4 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1.html
- add link to documentation in package description
- raise dependency on python 2.6

* Mon Aug 26 2013 Remi Collet <remi@fedoraproject.org> - 1.0.12-1
- version 1.0.12 GA

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Remi Collet <remi@fedoraproject.org> - 1.0.11-1
- version 1.0.11 GA

* Wed May  8 2013 Remi Collet <remi@fedoraproject.org> - 1.0.10-1
- version 1.0.10 GA
- archive is now free (no more doc to strip)

* Wed Feb 27 2013 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- version 1.0.9 GA
- disable test suite in mock, fix FTBFS #914203

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- version 1.0.8 GA

* Wed Oct  3 2012 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- version 1.0.7 GA

* Sat Sep 15 2012 Remi Collet <remi@fedoraproject.org> - 1.0.6-2.b2
- version 1.0.6b2

* Fri Sep  7 2012 Remi Collet <remi@fedoraproject.org> - 1.0.6-1.b1
- version 1.0.6 (beta)
- remove non GPL documentation
- disable test_network and test_connection on EL-5

* Fri Aug 10 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-2
- disable test_bugs with MySQL 5.1 (EL-6)

* Wed Aug  8 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- version 1.0.5 (beta)
- move from launchpad (devel) to dev.mysql.com

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 0.3.2-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Remi Collet <Fedora@famillecollet.com> 0.3.2-2
- run unittest during %%check
- fix License
- add python3 sub package

* Wed Mar 09 2011 Remi Collet <Fedora@famillecollet.com> 0.3.2-1
- first RPM

