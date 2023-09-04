%define _unpackaged_files_terminate_build 1
%define oname RestrictedPython

%def_with check

Name: python3-module-%oname
Version: 6.1
Release: alt1
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/RestrictedPython/
#Git: https://github.com/zopefoundation/RestrictedPython.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

%prep
%setup

%build
%python3_build

%install
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files
%doc *.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Sun Aug 27 2023 Nikolai Kostrigin <nickel@altlinux.org> 6.1-alt1
- 5.2 -> 6.1

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- 5.1 -> 5.2.

* Sun Feb 28 2021 Nikolai Kostrigin <nickel@altlinux.org> 5.1-alt1
- 5.0 -> 5.1

* Thu Jan 16 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0 -> 5.0
- Remove python2 module build
- Rearrange unittests execution
- Remove tests subpackage
- Fix license

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0-alt1.a3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0-alt1.a3
- Updated to upstream version 4.0a3.
- Enabled build with python-3.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.dev.git20130312
- Added tests

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.dev.git20130312
- Version 3.6.1dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1.1
- Rebuild with Python-2.7

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

