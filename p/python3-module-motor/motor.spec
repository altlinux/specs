%define oname motor

# requires mockupdb
%def_without check

Name: python3-module-%oname
Version: 3.5.1
Release: alt1

Summary: Non-blocking MongoDB driver for Tornado

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/motor
VCS: https://github.com/mongodb/motor

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-requirements-txt
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pymongo python3-module-gridfs
BuildRequires: python3(aiohttp)

%py3_provides %oname
%py3_requires tornado pymongo gridfs

BuildArch: noarch

%description
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Jul 11 2024 Grigory Ustinov <grenka@altlinux.org> 3.5.1-alt1
- Automatically updated to 3.5.1.

* Fri Jun 28 2024 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Automatically updated to 3.4.0.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 3.3.2-alt1
- Automatically updated to 3.3.2.

* Thu Sep 07 2023 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Wed Jul 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.

* Fri Apr 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt1
- New version 3.1.2.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2
- disable python2, enable python3

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version (2.0.0) with rpmgs script
- switch to build from tarball

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Updated to upstream version 1.2.0.

* Thu Oct 27 2016 Vladimir Didenko <cow@altlinux.org> 0.7-alt1.git20161010
- New version (closes: #31269)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140705
- Initial build for Sisyphus
