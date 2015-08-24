%define sname oslo.db

%def_with python3

Name: python-module-%sname
Version: 1.7.2
Release: alt1
Summary: OpenStack oslo.db library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-db = %EVR
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-migrate python-module-migrate-tests
BuildRequires: python-module-alembic >= 0.7.2
BuildRequires: python-module-eventlet
BuildRequires: python-module-oslotest
BuildRequires: python-module-stevedore >= 1.3.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-iso8601 >= 0.1.9

Requires: python-module-oslo.i18n
Requires: python-module-migrate
Requires: python-module-stevedore
Requires: python-module-SQLAlchemy
Requires: python-module-iso8601

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-oslo.utils >= 1.4.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.config >= 1.9.3
BuildRequires: python3-module-migrate python3-module-migrate-tests
BuildRequires: python3-module-alembic >= 0.7.2
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-stevedore >= 1.3.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-iso8601 >= 0.1.9
%endif

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.
* Documentation: http://docs.openstack.org/developer/oslo.db
* Source: http://git.openstack.org/cgit/openstack/oslo.db
* Bugs: http://bugs.launchpad.net/oslo

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
%endif


%package doc
Summary: Documentation for the Oslo database handling library
Group: Development/Documentation
Provides: python-module-oslo-db-doc = %EVR

%description doc
Documentation for the Oslo database handling library.

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

# Delete tests
rm -fr %buildroot%python_sitelibdir/test*
rm -fr %buildroot%python_sitelibdir/*/test*
rm -fr %buildroot%python_sitelibdir/*/*/test*
rm -fr %buildroot%python3_sitelibdir/test*
rm -fr %buildroot%python3_sitelibdir/*/test*
rm -fr %buildroot%python3_sitelibdir/*/*/test*

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release
