%define module_name django-dilla

Name: python-module-%module_name
Version: 0.2
Release: alt1.beta

Summary: Dilla is a multi-purpose general testing tool

License: BSD
Group: Development/Python
Url: https://github.com/aerosol/django-dilla.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README LICENSE
%python_sitelibdir/dilla*
%python_sitelibdir/django_dilla*

%changelog
* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1.beta
- Initial build for ALT Linux
