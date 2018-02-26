%define module_name django-command-extensions

%define git_commit 5e0582
Name: python-module-%module_name
Version: 0.7pre
Release: alt1.git%git_commit.1

Summary: Management extensions for the Django Framework

License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-command-extensions
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/django-extensions/django-extensions.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
Management extensions for the Django Framework.

%package tests
Summary: Tests for django-command-extensions
Group: Development/Python
Requires: %name = %version-%release

%description tests
Management extensions for the Django Framework.

This package contains tests for django-command-extensions.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7pre-alt1.git5e0582.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7pre-alt1.git5e0582
- Version 0.7pre
- Extracted tests into separate package

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.4.2pre-alt2.git9bf983
- fix inherit with alt gear-repo

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.4.2pre-alt1.git9bf983
- new version
- using rpm-build-python macros

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.gitee7c76.1
- Rebuilt with python 2.6

* Wed Oct 07 2009 Denis Klimov <zver@altlinux.org> 0.4.1-alt1.gitee7c76
- new version

* Thu Jan 22 2009 Denis Klimov <zver@altlinux.org> 0.3-alt1
- Initial build for ALT Linux

