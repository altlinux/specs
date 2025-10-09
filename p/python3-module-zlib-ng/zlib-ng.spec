Name: python3-module-zlib-ng
Version: 0.4.3
Release: alt2

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

# Hot fix for python3.13
# https://github.com/musicinmybrain/python-zlib-ng/commit/15ca0b99dc428d3d6b0fab999caa315019952624#diff-c2df034c4f580c134fed2f9e064b5ad831c069deefc4536c046fe99e90f52b81
sed -i 's/READ, WRITE = 1, 2/READ, WRITE = gzip.READ, gzip.WRITE/' src/zlib_ng/gzip_ng.py

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
* Wed Sep 10 2025 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt2
- Fixed build with python3.13.

* Fri Jul 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.3-alt1
- 0.4.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released
