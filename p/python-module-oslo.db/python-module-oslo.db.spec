%define sname oslo.db

%def_with python3

Name: python-module-%sname
Version: 2.6.0
Release: alt1.1.1
Summary: OpenStack oslo.db library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-db = %EVR
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-beaker python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-decorator python-module-docutils python-module-ecdsa python-module-ed25519 python-module-enum34 python-module-extras python-module-fixtures python-module-flake8 python-module-genshi python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-lingua python-module-mako python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-nose python-module-nss python-module-ntlm python-module-oslo.config python-module-oslo.i18n python-module-oslo.utils python-module-paste python-module-pbr python-module-polib python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sqlparse python-module-stevedore python-module-tempita python-module-testtools python-module-tox python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-beaker python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-lingua python3-module-mako python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-nose python3-module-ntlm python3-module-paste python3-module-pbr python3-module-pip python3-module-polib python3-module-pycparser python3-module-pycrypto python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-module-zope python3-module-zope.interface python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-alembic python-module-debtcollector python-module-dns python-module-greenlet python-module-html5lib python-module-migrate python-module-oslosphinx python-module-oslotest python-module-psycopg2 python-module-testresources python-module-testscenarios python3-module-alembic python3-module-dns python3-module-greenlet python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-migrate python3-module-oslo.config python3-module-psycopg2 python3-module-tox python3-module-wrapt python3-module-yaml python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.context >= 0.2.0
#BuildRequires: python-module-migrate >= 0.9.6 python-module-migrate-tests
#BuildRequires: python-module-alembic >= 0.8.0
#BuildRequires: python-module-eventlet
#BuildRequires: python-module-oslotest
#BuildRequires: python-module-stevedore >= 1.5.0
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-iso8601 >= 0.1.9

#BuildRequires: python-module-testresources python-module-testscenarios

Requires: python-module-oslo.i18n
Requires: python-module-migrate
Requires: python-module-stevedore
Requires: python-module-SQLAlchemy
Requires: python-module-iso8601

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.context >= 0.2.0
#BuildRequires: python3-module-migrate python3-module-migrate-tests
#BuildRequires: python3-module-alembic >= 0.8.0
#BuildRequires: python3-module-eventlet
#BuildRequires: python3-module-oslotest
#BuildRequires: python3-module-stevedore >= 1.5.0
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-iso8601 >= 0.1.9

#BuildRequires: python3-module-testresources python3-module-testscenarios
%endif

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.
* Documentation: http://docs.openstack.org/developer/oslo.db
* Source: http://git.openstack.org/cgit/openstack/oslo.db
* Bugs: http://bugs.launchpad.net/oslo


%package doc
Summary: Documentation for the Oslo database handling library
Group: Development/Documentation
Provides: python-module-oslo-db-doc = %EVR

%description doc
Documentation for the Oslo database handling library.

%package tests
Summary: Tests for the Oslo database handling library
Group: Development/Python
Requires: %name = %EVR

%description tests
Tests for the Oslo database handling library.

%if_with python3
%package -n python3-module-%sname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-db = %EVR

Requires: python3-module-oslo.i18n
Requires: python3-module-migrate
Requires: python3-module-stevedore
Requires: python3-module-SQLAlchemy
Requires: python3-module-iso8601

%description -n python3-module-%sname
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.

%package -n python3-module-%sname-tests
Summary: Tests for the Oslo database handling library
Group: Development/Python
Requires: python3-module-%sname = %EVR

%description -n python3-module-%sname-tests
Tests for the Oslo database handling library.

%endif


%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files doc
%doc doc/build/html

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%sname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif


%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release
