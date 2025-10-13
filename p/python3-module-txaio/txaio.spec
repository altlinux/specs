%define _unpackaged_files_terminate_build 1

%define oname txaio

%def_with check

Name: python3-module-%oname
Version: 25.9.2
Release: alt1

Summary: Compatibility API between asyncio/Twisted/Trollius
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/txaio
VCS: https://github.com/crossbario/txaio

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-twisted-core
BuildRequires: python3-module-pytest
BuildRequires: python3-test
%endif

%py3_requires asyncio

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/test/util.py

%description
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

Note that, with this approach, user code runs under the native event
loop of either Twisted or asyncio. This is different from attaching
either one's event loop to the other using some event loop adapter.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
txaio is a helper library for writing code that runs unmodified on both
Twisted and asyncio.

This is like six, but for wrapping over differences between Twisted and
asyncio so one can write code that runs unmodified on both (aka "source
code compatibility"). In other words: your users can choose if they want
asyncio or Twisted as a dependency.

This package contains tests for %oname.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

cp -fR test/ %buildroot%python3_sitelibdir/%oname/

%check
%tox_check_pyproject

%files
%doc LICENSE examples/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test/

%files tests
%python3_sitelibdir/%oname/test/


%changelog
* Mon Oct 13 2025 Grigory Ustinov <grenka@altlinux.org> 25.9.2-alt1
- Automatically updated to 25.9.2.

* Mon Jun 30 2025 Anton Vyatkin <toni@altlinux.org> 25.6.1-alt1
- New version 25.6.1.

* Fri Mar 28 2025 Anton Vyatkin <toni@altlinux.org> 23.1.1-alt2
- Fixed FTBFS.

* Tue Aug 01 2023 Grigory Ustinov <grenka@altlinux.org> 23.1.1-alt1
- Automatically updated to 23.1.1.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 18.8.1-alt3.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 18.8.1-alt3
- Build for python2 disabled.

* Sat Jun 01 2019 Stanislav Levin <slev@altlinux.org> 18.8.1-alt2
- Fixed Pytest4.x compatibility errors.

* Sun Apr 28 2019 Anton Midyukov <antohami@altlinux.org> 18.8.1-alt1
- Updated to upstream version 18.8.1.

* Mon Aug 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.7.1-alt1
- Updated to upstream version 18.7.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.1-alt1
- Updated to upstream version 2.8.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150407.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20150407.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150407
- Initial build for Sisyphus

