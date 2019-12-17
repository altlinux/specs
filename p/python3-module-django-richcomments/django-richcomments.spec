%define oname django-richcomments

%def_with bootstrap

Name: python3-module-%oname
Version: 0.0.2
Release: alt3

Summary: Django app extending the builtin comments framework for AJAX style commenting
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-richcomments/
BuildArch: noarch

# https://github.com/praekelt/django-richcomments.git
Source: %name-%version.tar
Patch0: fix-deprecated-import.patch

BuildRequires(pre): rpm-build-python3

%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults
%endif


%description
django-richcomments wraps the Django's comments frameworks existing
render_comment_list and render_comment_form template tags to make them
behave AJAXy.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-richcomments wraps the Django's comments frameworks existing
render_comment_list and render_comment_form template tags to make them
behave AJAXy.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

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
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt3
- build for python2 disabled

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20110915.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20110915
- Initial build for Sisyphus

