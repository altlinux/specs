%define oname pyxb

%def_with python3

Name: python-module-%oname
Version: 1.2.4
Release: alt1.git20141019.1.1
Summary: Python XML Schema Bindings
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/PyXB/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pabigot/pyxb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
PyXB is a pure Python package that generates Python code for classes
that correspond to data structures defined by XMLSchema. In concept it
is similar to JAXB for Java and CodeSynthesis XSD for C++.

%package -n python3-module-%oname
Summary: Python XML Schema Bindings
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip pyxb.bundles.wssplat.wsdl11
%add_python3_req_skip pyxb.utils.six.moves
%add_python3_req_skip pyxb.utils.six.moves.urllib
%add_python3_req_skip pyxb.utils.six.moves.urllib.request

%description -n python3-module-%oname
PyXB is a pure Python package that generates Python code for classes
that correspond to data structures defined by XMLSchema. In concept it
is similar to JAXB for Java and CodeSynthesis XSD for C++.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyXB is a pure Python package that generates Python code for classes
that correspond to data structures defined by XMLSchema. In concept it
is similar to JAXB for Java and CodeSynthesis XSD for C++.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc html

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc NOTICE *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc doc/html examples

%if_with python3
%files -n python3-module-%oname
%doc NOTICE *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1.git20141019.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.4-alt1.git20141019.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20141019
- Initial build for Sisyphus

