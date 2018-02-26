%define module_name django-piston

Name: python-module-%module_name
Version: 0.2.3
Release: alt1

Summary: Piston is a Django mini-framework creating APIs

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-piston

Source: %module_name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Piston is a Django mini-framework creating APIs

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install
cp piston/__init__.py %buildroot%python_sitelibdir/piston/

%files
%python_sitelibdir/django_piston-*
%python_sitelibdir/piston*


%changelog
* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.3-alt1
- Initial build for ALT Linux
