%define _unpackaged_files_terminate_build 1
%define oname natsort

# m2r2 is not ready for new mistune
%def_without docs
%def_with check

Name: python3-module-%oname
Version: 8.3.0
Release: alt1

Summary: Sort lists naturally
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/natsort/
BuildArch: noarch

# https://github.com/SethMMorton/natsort.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(hypothesis)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(tox)
BuildRequires: python3(coverage)
BuildRequires: python3(semver)
%endif

%if_with docs
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-m2r2
BuildRequires: python3(sphinx_rtd_theme)
%endif

%description
Natural sorting for python.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Natural sorting for python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Natural sorting for python.

This package contains documentation for %oname.
%endif # docs

%prep
%setup

echo '' > dev/requirements.txt

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD
pushd docs
sphinx-build-3 -b pickle -d build/doctrees . build/pickle
sphinx-build-3 -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -rv

%files
%doc *.rst
%_bindir/natsort
%python3_sitelibdir/natsort/
%python3_sitelibdir/*.egg-info/

%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*
%endif


%changelog
* Tue Feb 28 2023 Grigory Ustinov <grenka@altlinux.org> 8.3.0-alt1
- Automatically updated to 8.3.0.
- Build withoutt docs.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 8.2.0-alt1
- 7.1.1 -> 8.2.0.

* Fri Apr 02 2021 Grigory Ustinov <grenka@altlinux.org> 7.1.1-alt1
- Automatically updated to 7.1.1.
- Build with docs.

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 7.0.1-alt1
- Version updated to 7.0.1.

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt3
- Build for python2 disabled.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 6.0.0-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 6.0.0-alt1
- 3.5.1 -> 6.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1.git20140925.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt1.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.git20140925
- Initial build for Sisyphus

