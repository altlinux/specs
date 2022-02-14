%define _unpackaged_files_terminate_build 1
%define oname dirty-validators

%def_with check

Name: python3-module-%oname
Version: 0.5.4
Release: alt1
Summary: Validate library for python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dirty-validators/

# https://github.com/alfred82santa/dirty-validators.git
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(dirty_models)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(nose2)
%endif

# PEP503 normalized name
%py3_provides %oname

%description
Agnostic validators for python 3.

Features:

* Python 3 package.
* Easy to create a validator.
* Chained validations.
* Conditional validations.
* Specific error control messages.
* Dirty model integration
* No database dependent.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    nose2 -v
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
# requires aiounittest, nose2 doesn't support skip on module level
rm tests/dirty_validators/tests_async_complex.py
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/dirty_validators/
%python3_sitelibdir/dirty_validators-%version-py%_python3_version.egg-info/

%changelog
* Mon Feb 14 2022 Stanislav Levin <slev@altlinux.org> 0.5.4-alt1
- 0.3.2 -> 0.5.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150429.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150429
- Initial build for Sisyphus

