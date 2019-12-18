%define _unpackaged_files_terminate_build 1
%define oname django-googlesearch

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Django Google linked custom search engine app
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-googlesearch/
BuildArch: noarch

# https://github.com/praekelt/django-googlesearch.git
Source0: https://pypi.python.org/packages/65/06/d83f6345d84be4b3bf101cab18c928e22b3a3a48141df1530a66450d3aac/%{oname}-%{version}.tar.gz
Patch0: porting-on-python3.patch

BuildRequires(pre): rpm-build-python3


%description
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Provides a simple tag rendering a Google Custom Search Engine input
field and a view displaying search results. The product is an
implementation of http://www.google.com/cse/docs/cref.html. The custom
search engine definition is stored on your site, not by Google. This
allows you to define a search engine in version controlled code.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- porting on python3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20130114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20130114
- Initial build for Sisyphus

