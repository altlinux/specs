%define _unpackaged_files_terminate_build 1
%define oname repeated_test

%def_with check

Name: python3-module-%oname
Version: 2.1.3
Release: alt1

Summary: A quick unittest-compatible framework for repeating a test function over many fixtures

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/repeated-test/

# Source-url: https://pypi.io/packages/source/r/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(tox)
%endif

# PEP503 normalized name
%py3_provides repeated-test
Provides: python3-module-repeated-test = %EVR

%description
A quick unittest-compatible framework for repeating a test function over many fixtures.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# strip tests
rm -r %buildroot%python3_sitelibdir/%oname/tests/

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m unittest -v
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --develop

%files
%doc *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Mar 29 2022 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 1.0.1 -> 2.1.3.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

