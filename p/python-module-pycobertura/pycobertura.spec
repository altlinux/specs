%define oname pycobertura

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150106.1
Summary: A Cobertura coverage report parser written in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycobertura/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SurveyMonkey/pycobertura.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-click-tests python-module-colorama
#BuildPreReq: python-module-tabulate python-module-mock
#BuildPreReq: python-module-pytest-cov python-module-jinja2
#BuildPreReq: python-module-lxml
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-click-tests python3-module-colorama
#BuildPreReq: python3-module-tabulate python3-module-mock
#BuildPreReq: python3-module-pytest-cov python3-module-jinja2
#BuildPreReq: python3-module-lxml
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-click python-module-coverage python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-lxml python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: python-module-click-tests python-module-colorama python-module-html5lib python-module-jinja2 python-module-mock python-module-pytest-cov python-module-setuptools-tests python-module-tabulate python3-module-html5lib python3-module-pbr python3-module-pytest-cov python3-module-setuptools-tests python3-module-tabulate python3-module-unittest2 rpm-build-python3 time

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
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
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

