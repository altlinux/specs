%define sname oslo.serialization

%def_with python3

Name: python-module-%sname
Version: 2.4.0
Release: alt1
Summary: OpenStack oslo.serialization library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-serialization = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-msgpack >= 0.4.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
%endif

%description
The OpenStack Oslo serialization handling library.
* Documentation: http://docs.openstack.org/developer/oslo.serialization
* Source: http://git.openstack.org/cgit/openstack/oslo.serialization
* Bugs: http://bugs.launchpad.net/oslo

%if_with python3
%package -n python3-module-oslo.serialization
Summary: OpenStack oslo.serialization library
Group: Development/Python3
Provides: python3-module-oslo-serialization = %EVR

%description -n python3-module-oslo.serialization
The OpenStack Oslo serialization handling library.
%endif


%package doc
Summary: Documentation for the Oslo serialization handling library
Group: Development/Documentation
Provides: python-module-oslo-serialization-doc = %EVR

%description doc
Documentation for the Oslo serialization handling library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-oslo.serialization
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- Initial release
