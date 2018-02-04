%define oname pycobertura

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1.1
Summary: A Cobertura coverage report parser written in Python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pycobertura/

# https://github.com/SurveyMonkey/pycobertura.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-click-tests python-module-colorama
BuildRequires: python-module-tabulate python-module-mock
BuildRequires: python-module-pytest-cov python-module-jinja2
BuildRequires: python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-click-tests python3-module-colorama
BuildRequires: python3-module-mock
BuildRequires: python3-module-tabulate python3-module-unittest2
BuildRequires: python3-module-pytest-cov python3-module-jinja2
BuildRequires: python3-module-html5lib python3-module-pbr
%endif

%py_provides %oname

%description
A Cobertura coverage report parser written in Python.

%if_with python3
%package -n python3-module-%oname
Summary: A Cobertura coverage report parser written in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Cobertura coverage report parser written in Python.
%endif

%prep
%setup

sed -i -e 's|setuptools_git|setuptools|g' setup.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
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

