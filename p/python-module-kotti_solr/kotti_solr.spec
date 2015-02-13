%define oname kotti_solr
Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20150124
Summary: Extension for Kotti that provides integration with Solr search engine
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_solr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/teixas/kotti_solr.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-httplib2 python-module-lxml
BuildPreReq: python-module-sunburnt python-module-pytest-cov
BuildPreReq: python-module-SQLAlchemy

%py_provides %oname
%py_requires kotti httplib2 lxml sunburnt pyramid sqlalchemy

%description
This is an extension for Kotti that provides integration with Solr
search engine.

When this extension is active, it will automatically post updates to a
Solr instance when documents are added, modified, or deleted. It will
also make a search in Kotti query the Solr instance.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150124
- Initial build for Sisyphus

