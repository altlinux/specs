%define oname closure-soy

%def_with python3

Name: python-module-%oname
Version: 20121221
Release: alt1.git20130118.1.1
Summary: Google Closure's Soy templates packaged for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/closure-soy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Emsu/python-soy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-closure
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-closure
%endif

%py_provides closure_soy
%py_requires closure

%description
Closure Templates is a client and server side templating system for
building reusable HTML and UI elements. Closure's templating system is
also commonly known as Soy templates.

This is a Java-based tool. This package, based on the Closure Compiler
package, provides a simple way to install and use the the Closure
Template compiler from Python, bundling the soy.jar with the Python
package.

%package -n python3-module-%oname
Summary: Google Closure's Soy templates packaged for Python
Group: Development/Python3
%py3_provides closure_soy
%py3_requires closure

%description -n python3-module-%oname
Closure Templates is a client and server side templating system for
building reusable HTML and UI elements. Closure's templating system is
also commonly known as Soy templates.

This is a Java-based tool. This package, based on the Closure Compiler
package, provides a simple way to install and use the the Closure
Template compiler from Python, bundling the soy.jar with the Python
package.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 20121221-alt1.git20130118.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20121221-alt1.git20130118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20121221-alt1.git20130118
- Initial build for Sisyphus

