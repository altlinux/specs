%define oname SPARQLWrapper

%def_with python3

Name: python-module-%oname
Version: 1.7.0
Release: alt1.dev.git20140925.1
Summary: SPARQL Endpoint interface to Python
License: W3C SOFTWARE NOTICE AND LICENSE
Group: Development/Python
Url: https://pypi.python.org/pypi/SPARQLWrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RDFLib/sparqlwrapper.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-rdflib python-module-rdflib_jsonld
BuildPreReq: python-module-nose python-module-html5lib
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-rdflib python3-module-rdflib_jsonld
BuildPreReq: python3-module-nose python3-module-html5lib
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires rdflib_jsonld

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%package -n python3-module-%oname
Summary: SPARQL Endpoint interface to Python
Group: Development/Python3
%py3_provides %oname
%py3_requires rdflib_jsonld

%description -n python3-module-%oname
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|urllib2|urllib.request|g' \
	../python3/%oname/*.py ../python3/test/*.py
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

rm -f requirements.txt

%check
python setup.py test
./tests.sh
%if_with python3
pushd ../python3
python3 setup.py test
./run_tests_py3.sh
popd
%endif

%files
%doc *.txt *.txt scripts
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.txt scripts
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.dev.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.dev.git20140925
- Initial build for Sisyphus

