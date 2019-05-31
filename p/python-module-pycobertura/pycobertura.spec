%define _unpackaged_files_terminate_build 1
%define oname pycobertura

%def_with check

Name: python-module-%oname
Version: 0.10.5
Release: alt1
Summary: A Cobertura coverage report parser written in Python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pycobertura/

# https://github.com/SurveyMonkey/pycobertura.git
Source: %name-%version.tar
Patch: pycobertura-0.10.5-Fix-Pytest4.x-compatibility-error.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(click.testing)
BuildRequires: python2.7(colorama)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(pytest_cov)
BuildRequires: python2.7(tabulate)
BuildRequires: python3(click.testing)
BuildRequires: python3(colorama)
BuildRequires: python3(mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tabulate)
BuildRequires: python3(tox)
%endif

%py_provides %oname

%description
A Cobertura coverage report parser written in Python.

%package -n python3-module-%oname
Summary: A Cobertura coverage report parser written in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Cobertura coverage report parser written in Python.

%prep
%setup
%patch -p1
# unpin test requirements
sed -i 's/,\?<.*//g' test-requirements.txt

grep -qsF 'setuptools_git' setup.py || exit 1
sed -i -e 's|setuptools_git|setuptools|g' setup.py

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%check
export LC_ALL=en_US.UTF-8
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/py.test\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.md
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
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

