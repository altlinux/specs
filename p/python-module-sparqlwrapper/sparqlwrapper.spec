%define oname sparqlwrapper

%def_without python3

Name:           python-module-%oname
Version:        1.8.0
Release:        alt1
Summary:        A wrapper for a remote SPARQL endpoint
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/SPARQLWrapper
BuildArch:      noarch

# https://github.com/RDFLib/sparqlwrapper.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(rdflib) python2.7(urllib2)
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(rdflib)
BuildRequires: python3-module-nose
%endif

%description
SPARQLWrapper is a simple Python wrapper around a SPARQL service to remotelly execute your queries.
It helps in creating the query invokation and, possibly, convert the result into a more manageable format.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        A wrapper for a remote SPARQL endpoint

%description -n python3-module-%oname
SPARQLWrapper is a simple Python wrapper around a SPARQL service to remotelly execute your queries.
It helps in creating the query invokation and, possibly, convert the result into a more manageable format.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
%if_with python3
pushd ../python3
nosetests3
popd
%endif

nosetests

%files
%doc README.md LICENSE.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md LICENSE.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1
- Initial build for ALT.
