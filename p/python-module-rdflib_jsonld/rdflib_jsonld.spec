%define _unpackaged_files_terminate_build 1
%define oname rdflib_jsonld

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: rdflib extension adding JSON-LD parser and serializer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rdflib-jsonld/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RDFLib/rdflib-jsonld.git
Source0: https://pypi.python.org/packages/ba/48/edaad22fc9de34500699f0c7fc9124385dd425fd18857244f126a6f7df66/rdflib-jsonld-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-rdflib python-module-flake8
#BuildPreReq: python-module-nose python-module-simplejson
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-rdflib python3-module-flake8
#BuildPreReq: python3-module-nose python3-module-simplejson
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-mccabe python-module-pyparsing python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-mccabe python3-module-pyparsing python3-module-pytest python3-module-setuptools python3-pyflakes python3-tools-pep8
BuildRequires: python-module-flake8 python-module-nose python-module-pytest python-module-rdflib python3-module-flake8 python3-module-nose python3-module-rdflib rpm-build-python3

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
%setup -q -n rdflib-jsonld-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.dev.git20141130.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.dev.git20141130.1
- NMU: Use buildreq for BR.

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20141130
- Initial build for Sisyphus

