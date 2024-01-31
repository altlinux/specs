%define _unpackaged_files_terminate_build 1
%define oname tokenlib

%def_with check

Name: python3-module-%oname
Version: 2.0.0
Release: alt2

Summary: Generic support library for signed-token-based auth schemes
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/tokenlib/
# https://github.com/mozilla-services/tokenlib.git
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

%prep
%setup
%autopatch -p1

# hotfix for python3.12
sed -i 's/assertEquals/assertEqual/' tokenlib/tests/test_utils.py tokenlib/tests/test_tokens.py
sed -i 's/assertNotEquals/assertNotEqual/' tokenlib/tests/test_tokens.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/%oname/tests/

%changelog
* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Moved on modern pyproject macros.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 0.3.1 -> 2.0.0.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt2.git20140108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.git20140108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.1-alt2.git20140108
- cleanup buildreq

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140108
- Initial build for Sisyphus

