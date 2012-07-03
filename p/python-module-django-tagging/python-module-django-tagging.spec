%define module_name django-tagging

Name: python-module-%module_name
Version: 0.3.1
Release: alt1.1

Summary: Generic tagging application for Django

License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-tagging

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
A generic tagging application for Django projects, which allows association of a number of tags
with any Model instance and makes retrieval of tags simple.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc CHANGELOG.txt  docs  INSTALL.txt  LICENSE.txt  README.txt
%python_sitelibdir/django_tagging-*
%python_sitelibdir/tagging


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 20 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux


