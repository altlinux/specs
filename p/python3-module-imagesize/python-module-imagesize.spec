%define oname imagesize

Name: python3-module-imagesize
Version: 1.2.0
Release: alt1

Summary: Getting image size from png/jpeg/jpeg2000/gif file in pure Python

License: MIT
Group: Development/Python3
Url: https://github.com/shibukawa/imagesize_py

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

# For %%check:
BuildRequires: python3-module-nose

%description
 It parses image files' header and return image size.

* PNG
* JPEG
* JPEG2000
* GIF

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cd test

# Just in case:
# make sure we test the installed modules from %%buildroot,
#rm imagesize.py

[ -n "$NOSE_PROCESSES" ] || NOSE_PROCESSES=%__nprocs; export NOSE_PROCESSES # like in %%make_build
PYTHONPATH=%buildroot%python3_sitelibdir nosetests3 test

%files
%doc LICENSE.rst README.rst
%python3_sitelibdir/*

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- build python3 module separately, rewrite spec
- new version (1.2.0) with rpmgs script

* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- Rebuild with python3.7.

* Sat Apr 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1
- upstream release 0.7.1 (no changes)

* Thu Apr 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1
- Initial build for ALT Sisyphus. (Needed for sphinx-1.4.1.) (ALT#31976)
- The same source is used for both Python{2,3} with a commit from:
  https://github.com/xantares/imagesize_py/tree/py2a3
