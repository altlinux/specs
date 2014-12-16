%define oname rdflib_jsonld

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20141130
Summary: rdflib extension adding JSON-LD parser and serializer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rdflib-jsonld/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RDFLib/rdflib-jsonld.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-rdflib python-module-flake8
BuildPreReq: python-module-nose python-module-simplejson
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-rdflib python3-module-flake8
BuildPreReq: python3-module-nose python3-module-simplejson
%endif

%py_provides %oname

%description
This parser/serialiser will

* read in an JSON-LD formatted document and create an RDF graph
* serialize an RDF graph to JSON-LD formatted output

%package -n python3-module-%oname
Summary: rdflib extension adding JSON-LD parser and serializer
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This parser/serialiser will

* read in an JSON-LD formatted document and create an RDF graph
* serialize an RDF graph to JSON-LD formatted output

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20141130
- Initial build for Sisyphus

