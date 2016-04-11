%define pypi_name os-brick

%def_with python3

Name: python-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-babel
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.service >= 1.0.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-six >= 1.9.0


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-oslo.concurrency >= 3.5.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.service >= 1.0.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-retrying >= 1.2.3
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
OpenStack Cinder brick library for managing local volume attaches

%package doc
Summary: Documentation for OpenStack os-brick library
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python3

%description -n python3-module-%pypi_name
OpenStack Cinder brick library for managing local volume attaches

%endif

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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

python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%pypi_name/rootwrap.d
mv %buildroot/usr/etc/os-brick/rootwrap.d/*.filters %buildroot%_sysconfdir/%pypi_name/rootwrap.d/

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%python_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*

%files doc
%doc README.rst doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*
%endif

%changelog
* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial packaging
