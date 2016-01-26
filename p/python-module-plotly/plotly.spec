%define oname plotly

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6.6
Release: alt2
Summary: Python plotting library for collaborative, interactive, publication-quality graphs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/plotly/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-html5lib python-module-notebook python-module-pytest

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-six
#BuildPreReq: python-module-pytz python-module-numpy
#BuildPreReq: python-module-matplotlib python-module-zmq ipython
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-six
#BuildPreReq: python3-module-pytz python3-module-numpy
#BuildPreReq: python3-module-matplotlib python3-module-zmq ipython3
BuildRequires: python3-module-html5lib python3-module-notebook
%endif

%py_provides %oname
#%py_requires requests six pytz json numpy matplotlib zmq IPython.html

%description
Use this package to make collaborative, interactive, publication-quality
graphs from Python.

%package -n python3-module-%oname
Summary: Python plotting library for collaborative, interactive, publication-quality graphs
Group: Development/Python3
%py3_provides %oname
#%py3_requires requests six pytz numpy matplotlib zmq IPython.html

%description -n python3-module-%oname
Use this package to make collaborative, interactive, publication-quality
graphs from Python.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
for i in $(find %oname -name '*.py'); do
	py.test $i -vv || exit 1
done
%if_with python3
pushd ../python3
python3 setup.py test
for i in $(find %oname -name '*.py'); do
	py.test-%_python3_version $i -vv || exit 1
done
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.6.6-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Version 1.6.4

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

