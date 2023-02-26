%define oname keyring

%def_with check

Name: python3-module-%oname
Version: 23.14.0
Release: alt1

Summary: Keyring provides an easy way to access the system keyring service

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/keyring

Vcs: https://github.com/jaraco/keyring
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-secretstorage
BuildRequires: python3-module-jaraco.classes
%endif

%description
The Python keyring lib provides an easy way to access the system
keyring service from python. It can be used in any application
that needs safe password storage.

%prep
%setup

# Drop redundant shebang
sed -i '1{\@^#!/usr/bin/env python@d}' keyring/cli.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst LICENSE
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sun Feb 26 2023 Grigory Ustinov <grenka@altlinux.org> 23.14.0-alt1
- Build new version (Closes: #45387).

* Thu Sep 23 2021 Michael Shigorin <mike@altlinux.org> 21.8.0-alt2
- fix build --without check (no pytest => no toml then)
- minor spec cleanup

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 21.8.0-alt1
- new version (21.8.0) with rpmgs script
- drop subpackage tests

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 12.0.0-alt6
- Fixed BuildRequires.

* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 12.0.0-alt5
- Drop python2 support.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 12.0.0-alt4
- Made dependency on Pytest and its plugins optional.

* Thu Dec 13 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt3
- Updated deps for Python2.7

* Thu Dec 06 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt2
- Updated deps (ALT #35655)

* Mon Apr 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 12.0.0-alt1
- Updated version to 12.0.0
  Fixed deps

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt2
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt1.2
- Updated build spec

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4-alt1
- Version 5.4

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.1-alt1
- Version 5.2.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
