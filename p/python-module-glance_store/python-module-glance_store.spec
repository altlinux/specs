%define sname glance_store

# for python3 need python3.3(glance)
%def_without python3

Name: python-module-%sname
Version: 0.9.1
Release: alt1
Summary: OpenStack Image Service Store Library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%sname
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.concurrency >= 2.3.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-enum34
BuildRequires: python-module-cinderclient >= 1.3.1
BuildRequires: python-module-eventlet >= 0.17.4
BuildRequires: python-module-jsonschema >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-oslo.concurrency >= 2.3.0
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python-module-cinderclient >= 1.3.1
BuildRequires: python3-module-eventlet >= 0.17.4
BuildRequires: python3-module-jsonschema >= 2.0.0
%endif

BuildArch: noarch

%description
OpenStack Image Service Store Library

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack Image Service Store Library
Group: Development/Python3

%description -n python3-module-%sname
OpenStack Image Service Store Library
%endif


%package doc
Summary: Documentation for OpenStack Image Service Store Library
Group: Development/Documentation

%description doc
Documentation for OpenStack Image Service Store Library

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
