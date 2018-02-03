%def_with python3

%define oname futurist

Name: python-module-%oname
Version: 0.21.1
Release: alt1.1
Summary: Useful additions to futures, from the future
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/futurist
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

#Requires: python-module-six >= 1.9.0
Requires: python-module-monotonic
Requires: python-module-futures >= 3.0
Requires: python-module-contextlib2 >= 0.4.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-contextlib2 >= 0.4.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx >= 4.7.0
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-contextlib2 >= 0.4.0
BuildRequires: python3-module-prettytable >= 0.7.1
%endif

%description
Code from the future, delivered to you in the now.

%package doc
Summary: Documentation for futurist library
Group: Development/Documentation

%description doc
Documentation for futurist library.

%package tests
Summary: Tests for futurist library
Group: Development/Python
BuildArch: noarch

%description tests
Tests for futurist library.

%package -n python3-module-%oname
Summary: Useful additions to futures, from the future
Group: Development/Python3

#Requires: python3-module-six >= 1.9.0
Requires: python3-module-monotonic
Requires: python3-module-contextlib2 >= 0.4.0

%description -n python3-module-%oname
Code from the future, delivered to you in the now.

%package -n python3-module-%oname-tests
Summary: Tests for futurist library
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname-tests
Tests for futurist library.

%prep
%setup -n %oname-%version

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

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files doc
%doc doc/build/html

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.0-alt1
- 0.21.0
- add tests package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial package.
