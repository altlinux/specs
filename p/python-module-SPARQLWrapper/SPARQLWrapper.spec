%define oname SPARQLWrapper

%def_without python3

Name: python-module-%oname
Version: 1.8.0
Release: alt2.1
Summary: SPARQL Endpoint interface to Python
License: W3C SOFTWARE NOTICE AND LICENSE
Group: Development/Python
Url: https://pypi.python.org/pypi/SPARQLWrapper/

# https://github.com/RDFLib/sparqlwrapper.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-rdflib python-module-rdflib_jsonld
BuildRequires: python-module-nose python-module-html5lib
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-rdflib python3-module-rdflib_jsonld
BuildRequires: python3-module-nose python3-module-html5lib
BuildRequires: python3-module-six
%endif

%py_provides %oname
%py_requires rdflib_jsonld

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%if_with python3
%package -n python3-module-%oname
Summary: SPARQL Endpoint interface to Python
Group: Development/Python3
%py3_provides %oname
%py3_requires rdflib_jsonld

%description -n python3-module-%oname
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.
%endif

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

%check
nosetests

%if_with python3
pushd ../python3
nosetests3
popd
%endif

%files
%doc *.md ChangeLog.txt LICENSE.txt scripts
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md ChangeLog.txt LICENSE.txt scripts
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt2
- Fixed build without python-3.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1
- Updated to upstream version 1.8.0.
- Disabled build for python-3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.dev.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.dev.git20140925
- Initial build for Sisyphus

