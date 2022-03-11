%define _unpackaged_files_terminate_build 1
%define oname vcrpy

%def_with check

Name: python3-module-%oname
Version: 4.1.1
Release: alt2
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/vcrpy/

# https://github.com/kevin1024/vcrpy.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(wrapt)
BuildRequires: python3(yaml)
BuildRequires: python3(yarl)
BuildRequires: python3(six)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%prep
%setup
%autopatch -p1

# don't package boto stubs, this code should be unreachable with boto3
rm vcr/stubs/boto_stubs.py

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export REQUIRES_INTERNET=yes
export TOX_TESTENV_PASSENV='REQUIRES_INTERNET'
tox.py3 --sitepackages --console-scripts -vvr --develop -- tests/unit

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 4.1.1-alt2
- Dropped dependency on unmaintained and unused boto.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.2.0 -> 4.1.1.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2.git20150108
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.git20150108.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150108.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150108.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150108
- Version 1.2.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141103
- Initial build for Sisyphus

