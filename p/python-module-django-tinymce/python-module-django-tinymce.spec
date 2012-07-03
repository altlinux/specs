%define module_name django-tinymce

Name: python-module-%module_name
Version: 1.5
Release: alt1.1

Summary: A Django app for render a form field as a TinyMCE editor


License: MIT
Group: Development/Python
Url: http://code.google.com/p/django-tinymce/

Source: %module_name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%setup_python_module %module_name


%description
A Django application that contains a widget to render a form field as
a TinyMCE editor.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE.txt README.txt
%python_sitelibdir/tinymce
%python_sitelibdir/django_tinymce*


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1.1
- Rebuild with Python-2.7

* Wed Mar 31 2010 Denis Klimov <zver@altlinux.org> 1.5-alt1
- Initial build for ALT Linux

