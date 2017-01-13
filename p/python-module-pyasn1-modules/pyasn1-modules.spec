%define _unpackaged_files_terminate_build 1
%define oname pyasn1-modules

%def_with python3

Name: python-module-%oname
Version: 0.0.8
Release: alt1
Summary: ASN.1 modules for Python
License: BSD
Group: Development/Python
Url: http://sourceforge.net/projects/pyasn1/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/60/32/7703bccdba05998e4ff04db5038a6695a93bedc45dcf491724b85b5db76a/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyasn1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyasn1
%endif
%py_requires pyasn1

%description
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%if_with python3
%package -n python3-module-%oname
Summary: ASN.1 modules for Python 3
Group: Development/Python3
%py3_requires pyasn1

%description -n python3-module-%oname
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.
%endif

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build
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
python setup.py test -v
pushd tools
export PYTHONPATH=%buildroot%python_sitelibdir
for i in ../test/*; do
	sh $i ||exit 1
done
popd
%if_with python3
pushd ../python3
python3 setup.py test -v
pushd tools
export PYTHONPATH=%buildroot%python3_sitelibdir
for i in ../test/*; do
	sed -i 's|python |python3 |' $i
	sh $i ||exit 1
done
popd
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Version 0.0.7

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Version 0.0.5

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt2
- Version 0.0.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.4-alt1.rc0.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.rc0
- Initial build for Sisyphus

