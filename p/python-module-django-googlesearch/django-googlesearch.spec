%define oname django-googlesearch

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20130114.1
Summary: Django Google linked custom search engine app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-googlesearch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-googlesearch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django Google linked custom search engine app
Group: Development/Python3

%description -n python3-module-%oname
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

This package contains tests for %oname.

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20130114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20130114
- Initial build for Sisyphus

