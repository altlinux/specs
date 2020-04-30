%define _unpackaged_files_terminate_build 1
%define oname http-parser

%def_with check

Name: python-module-%oname
Version: 0.9.0
Release: alt1
Summary: http request/response parser
License: MIT
Group: Development/Python
Url: https://pypi.org/project/http-parser/

# https://github.com/benoitc/http-parser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(Cython)
BuildRequires: python3(Cython)

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif
%py_provides %oname

%description
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%package -n python3-module-%oname
Summary: http request/response parser
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%prep
%setup

# regenerate with cython later
rm -f http_parser/parser.c

# remove extra deps
for pkg in pytest-cov pytest-cache
do
    { grep -s -l "^[[:space:]]*${pkg}[[:space:]]*$" tox.ini | xargs \
        sed -i -e "/^[[:space:]]*${pkg}[[:space:]]*$/d"; } || exit 1
done

cp -fR . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py2: _PYTEST_BIN=%_bindir\/py.test\
    py3: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py2,py3
tox.py3 --sitepackages -vv -r

%files
%doc NOTICE *.rst *.md THANKS examples
%python_sitelibdir/*

%files -n python3-module-%oname
%doc NOTICE *.rst *.md THANKS examples
%python3_sitelibdir/*

%changelog
* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.3 -> 0.9.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.2
- Updated build spec

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20150514.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20150514.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150514
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20140925
- Initial build for Sisyphus

