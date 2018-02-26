%define module_name django-reversion

%define git_rev 91bd6b
Name: python-module-%module_name
Version: 1.5.1
Release: alt1.git%git_rev

Summary: Comprehensive version control facilities for Django

License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-reversion
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/etianen/django-reversion.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

%package tests
Summary: Tests for Django Reversion
Group: Development/Python
Requires: %name = %version-%release

%description tests
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

This package contains tests for Django Reversion.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.markdown
%python_sitelibdir/django_reversion-*
%python_sitelibdir/reversion
%exclude %python_sitelibdir/reversion/tests.*
%exclude %python_sitelibdir/reversion/tests_deprecated.py*

%files tests
%python_sitelibdir/reversion/tests.*
%python_sitelibdir/reversion/tests_deprecated.py*

%changelog
* Sun Jan 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git91bd6b
- Version 1.5.1 (ALT #26818)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.alpha.gitd9655b.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.alpha.gitd9655b
- Version 1.4 alpha

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git64bd63
- Version 1.3.2
- Extracted tests into separate package

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2.1-alt1.svn273
- Initial build for ALT Linux

