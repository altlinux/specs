%define pypi_name fasteners

Name: python-module-%pypi_name
Version: 0.13.0
Release: alt2

Summary: A python package that provides useful locks
Group: Development/Python
License: ASL 2.0
Url: https://github.com/harlowja/fasteners
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-six python-module-monotonic

# tests:
BuildRequires: python-module-testtools
BuildRequires: python-module-nose


%description
A python package that provides useful locks.

%package -n python3-module-%pypi_name
Summary: A python package that provides useful locks
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six python3-module-monotonic

# tests
BuildRequires: python3-module-testtools
BuildRequires: python3-module-nose
BuildRequires: python-module-futures

%description -n python3-module-%pypi_name
A python package that provides useful locks.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%check
nosetests
nosetests3

%files
%doc README.rst
%python_sitelibdir/%pypi_name
%python_sitelibdir/%{pypi_name}*.egg-info

%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pypi_name}*.egg-info


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- Initial package.

