%define _unpackaged_files_terminate_build 1
%define oname wcwidth

%def_with check

Name: python-module-%oname
Version: 0.1.9
Release: alt1
Summary: Measures number of Terminal column cells of wide-character codes
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wcwidth/

# https://github.com/jquast/wcwidth.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%package -n python3-module-%oname
Summary: Measures number of Terminal column cells of wide-character codes
Group: Development/Python3

%description -n python3-module-%oname
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install
rm -r %buildroot%python_sitelibdir/%oname/tests

pushd ../python3
%python3_install
popd
rm -r %buildroot/%python3_sitelibdir/%oname/tests

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py2: _PYTEST_BIN=%_bindir\/py.test\
    py3: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py2,py3
tox.py3 --sitepackages -p auto -o -vv -r

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%python_sitelibdir/%oname/

%files -n python3-module-%oname
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/

%changelog
* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 0.1.9-alt1
- 0.1.7 -> 0.1.9.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt2
- Fixed tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150413.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150413
- New snapshot

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150125
- Initial build for Sisyphus

