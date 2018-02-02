%define oname ladon

%def_with python3

Name: python-module-%oname
Version: 0.9.40
Release: alt1.1
Summary: Several web service interfaces at once, including JSON-WSP, SOAP and JSON-RPC
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/ladon/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-jinja2 python2.7(sphinx_bootstrap_theme)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-jinja2 python3(sphinx_bootstrap_theme)
%endif

%py_provides %oname
%py_requires jinja2 json

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
%py3_requires jinja2 json

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

rm -rf %buildroot%python_sitelibdir/*/test.* ||:
%if_with python3
rm -rf %buildroot%python3_sitelibdir/*/test.* ||:
rm -rf %buildroot%python3_sitelibdir/*/*/test.* ||:
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.40-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.40-alt1
- Updated to upstream version 0.9.40.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.10-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.10-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus

