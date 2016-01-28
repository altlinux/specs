%define oname ladon

%def_with python3

Name: python-module-%oname
Version: 0.9.10
Release: alt1.1
Summary: Several web service interfaces at once, including JSON-WSP, SOAP and JSON-RPC
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/ladon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jinja2
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jinja2
%endif

%py_provides %oname
%py_requires jinja2 json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-jinja2 python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
Ladon is a framework for exposing python methods to several internet
service protocols. Once a method is ladonized it is automatically served
through all the interfaces that your ladon installation contains. Ladon
is easily extendable. Adding a new service interface is as easy as
adding a single module containing a class inheriting the BaseInterface
class.

%package -n python3-module-%oname
Summary: Several web service interfaces at once, including JSON-WSP, SOAP and JSON-RPC
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2

%description -n python3-module-%oname
Ladon is a framework for exposing python methods to several internet
service protocols. Once a method is ladonized it is automatically served
through all the interfaces that your ladon installation contains. Ladon
is easily extendable. Adding a new service interface is as easy as
adding a single module containing a class inheriting the BaseInterface
class.

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
%doc *.rst docs/html examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/html examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.10-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus

