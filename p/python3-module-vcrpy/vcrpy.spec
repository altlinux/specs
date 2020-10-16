%define _unpackaged_files_terminate_build 1
%define oname vcrpy

%def_with check

Name: python3-module-%oname
Version: 4.1.1
Release: alt1
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/vcrpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevin1024/vcrpy.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(wrapt)
BuildRequires: python3(yaml)
BuildRequires: python3(yarl)
%endif

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
whitelist_externals =
    /bin/cp
    /bin/sed
commands_pre =
    /bin/cp %_bindir/py.test3 {envbindir}/py.test
    /bin/sed -i '1c #!{envpython}' {envbindir}/py.test
commands =
    {envbindir}/py.test {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export REQUIRES_INTERNET=yes
export TOX_TESTENV_PASSENV='REQUIRES_INTERNET'
tox.py3 --sitepackages -vvr -- tests/unit

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
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

