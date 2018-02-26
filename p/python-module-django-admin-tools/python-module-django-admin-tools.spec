%define module_name django-admin-tools

Name: python-module-%module_name
Version: 0.4.1
Release: alt1

Summary: A collection of tools for the django administration interface

License: MIT License
Group: Development/Python
Url: http://www.bitbucket.org/izi/django-admin-tools

Source: %module_name-%version.tar.gz

BuildArch: noarch

%setup_python_module %module_name

%description
django-admin-tools is a collection of extensions/tools for the default django
administration interface, it includes:

 * a full featured and customizable dashboard,
 * a customizable menu bar,
 * tools to make admin theming easier.

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS CHANGELOG LICENSE README docs
%python_sitelibdir/django_admin_tools-*
%python_sitelibdir/admin_tools


%changelog
* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- Initial build for ALT Linux
