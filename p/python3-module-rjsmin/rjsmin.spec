%define _unpackaged_files_terminate_build 1
%define oname rjsmin

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1
Summary: Javascript Minifier
License: Apache-2.0
Group: Development/Python3
Url: http://opensource.perlig.de/rjsmin/

# https://github.com/ndparker/rjsmin.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
rJSmin is a javascript minifier written in python.

%prep
%setup
%autopatch -p1

%python3_build_debug

%install
%python3_install

%check
sed -i -e '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' \
-e '/^setenv[ ]*=/a\
    py3: _PYTEST_BIN=%_bindir\/py.test3' \
test.ini

export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vv -r -c test.ini

%files
%doc README.md
%python3_sitelibdir/_rjsmin.cpython-*.so
%python3_sitelibdir/rjsmin.py
%python3_sitelibdir/__pycache__/rjsmin.cpython-*.*
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Jul 02 2020 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.12 -> 1.1.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt3.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 1.0.10-alt3.git20141116
- Python compilation for 3.5.

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.10-alt2.git20141116
- Documentation creation disabled

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20141116
- Initial build for Sisyphus

