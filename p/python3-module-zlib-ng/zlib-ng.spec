Name: python3-module-zlib-ng
Version: 0.4.3
Release: alt1

Summary: Python bindings for the zlib-ng library
License: PSF-2.0
Group: Development/Python
Url: https://pypi.org/project/zlib-ng/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(test)
BuildRequires: pkgconfig(zlib-ng)

%description
%summary

%prep
%setup

%build
export PYTHON_ZLIB_NG_LINK_DYNAMIC=true
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/zlib_ng
%python3_sitelibdir/zlib_ng-%version.dist-info

%changelog
* Fri Jul 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.3-alt1
- 0.4.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released
