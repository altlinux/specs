%define _unpackaged_files_terminate_build 1
%define oname RestrictedPython

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/RestrictedPython/
#Git: https://github.com/zopefoundation/RestrictedPython.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mock
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
# no need to keep constraint for pytest<5 as we drop Python2 module
sed -i 's|pytest < 5|pytest|' constraints.txt
# rename pytest executable
sed -i 's|pytest --|py.test3 --|g' tox.ini
# no need for html report and dependecy on pytest-html
sed -i 's|--html=_build\/pytest\/report-{envname}\.html --self-contained-html||' tox.ini
sed -i 's|pytest-html||' tox.ini
# cancel coverage execution during unit testing
sed -i 's|coverage run [ -a]\{0,\}-m||g' tox.ini
sed -i 's|[[:space:]]coverage|#coverage|g' tox.ini
# cancel docbuild tests
sed -i 's|sphinx|#py3_sphinx|g' tox.ini
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test3' tox.ini
sed -i '/setenv =$/a \
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
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

