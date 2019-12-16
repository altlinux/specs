%define _unpackaged_files_terminate_build 1
%define oname pycobertura

%def_with check

Name: python3-module-%oname
Version: 0.10.5
Release: alt3

Summary: A Cobertura coverage report parser written in Python
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pycobertura/

# https://github.com/SurveyMonkey/pycobertura.git
Source: %name-%version.tar
Patch: pycobertura-0.10.5-Fix-Pytest4.x-compatibility-error.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(click.testing)
BuildRequires: python3(colorama)
BuildRequires: python3(mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tabulate)
BuildRequires: python3(tox)
%endif

%py3_provides %oname


%description
A Cobertura coverage report parser written in Python.

%prep
%setup
%patch -p1
# unpin test requirements
sed -i 's/,\?<.*//g' test-requirements.txt

grep -qsF 'setuptools_git' setup.py || exit 1
sed -i -e 's|setuptools_git|setuptools|g' setup.py

%build
%python3_build_debug

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.5-alt3
- build for python2 disabled

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.10.5-alt2
- Fixed testing against Pytest 5.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 0.10.5-alt1
- 0.10.0 -> 0.10.5.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.0-alt1
- Updated to upstream version 0.10.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150106.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.git20150106.1
- NMU: Use buildreq for BR.

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150106
- Version 0.4.1

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141223
- Version 0.3.0

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141210
- Version 0.2.1

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141127
- Initial build for Sisyphus

