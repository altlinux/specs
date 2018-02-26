%define module_name django-country-dialcode

Name: python-module-%module_name
Version: 0.1.0
Release: alt1
Summary: Application providing Dialcode and Countries code
License: MIT
Group: Development/Python
Url: https://github.com/aerosol/django-dilla.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Application providing Dialcode and Countries code

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc HACKING README.rst MIT-LICENSE.txt
%python_sitelibdir/country_dialcode*
%python_sitelibdir/django_country_dialcode*

%changelog
* Sat May 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux
