%define module_name django-uni-form

Name: python-module-%module_name
Version: 0.9.0
Release: alt1

Summary: The best way to have Django_ DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML

License: BSD
Group: Development/Python
Url: https://github.com/pydanny/django-uni-form.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Django_ forms are easily rendered as tables, paragraphs, and unordered lists. 
However, elegantly rendered div based forms is something you have to do by hand. 
The purpose of this application is to provide a simple tag and/or filter that
lets you quickly render forms in a div format

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

%files
%doc README* CHANGELOG CONTRIBUTORS.txt LICENSE.txt docs
%python_sitelibdir/uni_form*
%python_sitelibdir/django_uni_form*

%changelog
* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
