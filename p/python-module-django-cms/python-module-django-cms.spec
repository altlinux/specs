%define git_commit efd039d

%define module_name django-cms

Name: python-module-%module_name
Version: 2.1.5
Release: alt2

Summary: An Advanced Django CMS

License: BSD
Group: Development/Python
Url: http://www.django-cms.org
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/divio/django-cms.git
Source: %module_name-%version.tar

BuildArch: noarch

Provides: %{name}2.1 = %EVR
Conflicts: python-module-django-mptt

# see docs/getting_started/installation.rst
Requires: python-module-django >= 1.2.3
Requires: python-module-django-classy-tags >= 0.2.2

BuildRequires: python-module-setuptools

%setup_python_module %module_name

%add_python_req_skip south tinymce dbgettext testapp

%description
An Advanced Django CMS.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc CHANGELOG.txt AUTHORS LICENSE
%python_sitelibdir/cms/
%python_sitelibdir/menus/
%python_sitelibdir/mptt/
%python_sitelibdir/publisher/
%python_sitelibdir/django_cms*egg-info/

%changelog
* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.5-alt2
- Fix conflicts

* Fri Feb 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.5-alt1
- Version 2.1.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1.git.6db7026.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1.git.6db7026
- Version 2.1.3

* Sun Nov 28 2010 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt3.git.1b5ea0a
- cleanup spec
- build for ALT Linux Sisyphus

* Thu Nov 18 2010 Devaev Maxim <mdevaev@etersoft.ru> 2.1.0-alt2.git.1b5ea0a
- fixed python-testapp requires

* Wed Nov 17 2010 Devaev Maxim <mdevaev@etersoft.ru> 2.1.0-alt1.git.1b5ea0a
- New version

* Sat Mar 27 2010 Denis Klimov <zver@altlinux.org> 2.0.2-alt1.git.b035f83
- Initial build for ALT Linux

