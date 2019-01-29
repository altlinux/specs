%define _unpackaged_files_terminate_build 1
%define oname path.py

%def_with check

Name: python-module-%oname
Version: 11.5.0
Release: alt1

Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://github.com/jaraco/path.py

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python2.7(appdirs)
BuildRequires: python2.7(backports.os)
BuildRequires: python2.7(importlib_metadata)
BuildRequires: python2.7(packaging)
BuildRequires: python2.7(pytest_flake8)
BuildRequires: python3(appdirs)
BuildRequires: python3(importlib_metadata)
BuildRequires: python3(packaging)
BuildRequires: python3(pytest_flake8)
BuildRequires: python3(tox)
%endif

%py_requires importlib_metadata
%py_requires backports.os
%py_provides %oname
Provides: python-module-path = %EVR
Obsoletes: python-module-path < %EVR

%description
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%package -n python3-module-%oname
Summary: A module wrapper for os.path
Group: Development/Python3

%py3_requires importlib_metadata
%py3_provides %oname
Provides: python3-module-path = %EVR
Obsoletes: python3-module-path < %EVR

%description -n python3-module-%oname
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%prep
%setup
%patch -p1
# currently disable PEP517/518
rm -f pyproject.toml

rm -rf ../python3
cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

# don't package tests
rm -f %buildroot%python_sitelibdir/test_path.py
rm -f %buildroot%python3_sitelibdir/test_path.py

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
sed -i -e '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/python setup.py checkdocs/d' \
tox.ini

# dependencies which are needed to check docs
sed -i -e '/pytest-sugar/d' \
-e '/collective.checkdocs/d' \
-e '/pygments/d' \
setup.py

export LC_ALL=C.UTF-8
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='LC_ALL'
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/path.py*
%python_sitelibdir/path.py-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/path.py
%python3_sitelibdir/__pycache__/path.cpython-*.py*
%python3_sitelibdir/path.py-%version-py%_python3_version.egg-info/

%changelog
* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 11.5.0-alt1
- 7.2 -> 11.5.0.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 7.2-alt1.git20150122.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.2-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.git20150122
- Version 7.2

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.git20140823
- Version 5.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
