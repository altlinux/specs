%define _unpackaged_files_terminate_build 1
%define oname pytest-benchmark

%def_with docs
%def_with check

Name: python-module-%oname
Version: 3.2.2
Release: alt5
Summary: pytest fixture for benchmarking code
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-benchmark/

# https://github.com/ionelmc/pytest-benchmark.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-objects.inv
BuildRequires: python-module-sphinx_py3doc_enhanced_theme
%endif

%if_with check
BuildRequires: git-core
BuildRequires: python3(tox)

BuildRequires: python3(aspectlib)
BuildRequires: python3(cpuinfo)
BuildRequires: python3(elasticsearch)
BuildRequires: python3(freezegun)
BuildRequires: python3(pygal)
BuildRequires: python3(pytest-xdist)
%endif

%py_requires cpuinfo

%description
A pytest fixture for benchmarking code.

%package -n python3-module-%oname
Summary: pytest fixture for benchmarking code
Group: Development/Python3
%py3_requires cpuinfo

%description -n python3-module-%oname
A pytest fixture for benchmarking code.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A pytest fixture for benchmarking code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pytest fixture for benchmarking code.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch -p1

grep -qsF ' seconds ======*' tests/test_benchmark.py || exit 1
sed -i 's/\( seconds\)\( =====*\)/\2/g' tests/test_benchmark.py

# unpin or remove unpackaged testing deps
grep -qsF 'pytest-instafail' tox.ini || exit 1
grep -qsF 'pytest-travis-fold' tox.ini || exit 1
grep -qsF 'pygaljs' tox.ini || exit 1
grep -qsF 'hunter' tox.ini || exit 1
sed -i \
-e '/pytest-instafail/d' \
-e '/pytest-travis-fold/d' \
-e '/pygaljs/d' \
-e '/hunter/d' \
-e 's/elasticsearch==.*$/elasticsearch/g' \
-e 's/==/>=/g' \
tox.ini

rm -rf ../python3
cp -fR . ../python3

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done
popd

%python_install

%if_with docs
export PYTHONPATH="$(pwd)"/src
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -a docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
sed -i -e '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' \
-e '/^setenv[ ]*=$/a\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3' \
tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}-nocov
tox.py3 --sitepackages -rv

%files
%doc README.rst CHANGELOG.rst
%_bindir/py.test-benchmark
%_bindir/pytest-benchmark
%python_sitelibdir/pytest_benchmark/
%python_sitelibdir/pytest_benchmark-*.egg-info/

%files -n python3-module-%oname
%doc README.rst CHANGELOG.rst
%_bindir/py.test-benchmark.py3
%_bindir/pytest-benchmark.py3
%python3_sitelibdir/pytest_benchmark/
%python3_sitelibdir/pytest_benchmark-*.egg-info/

%if_with docs
%files pickles
%python_sitelibdir/pytest-benchmark/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Tue Dec 17 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt5
- Fixed testing against Pytest 5.3.2.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt4
- Fixed testing against Pytest 5.2.

* Thu Aug 22 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt3
- Fixed testing against Pytest 5.1.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt2
- Fixed testing against Pytest 5.

* Wed May 29 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt1
- 3.1.1 -> 3.2.2.

* Thu Dec 20 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt2
- Fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.git20141219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.git20141219.1
- NMU: Use buildreq for BR.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141219
- Initial build for Sisyphus

