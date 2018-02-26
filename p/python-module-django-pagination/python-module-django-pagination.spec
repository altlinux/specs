%define module_name django-pagination

Name: python-module-%module_name
Version: 1.0.7
Release: alt1

Summary: django-pagination allows for easy Digg-style pagination without modifying your views

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-pagination

Source: %module_name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
django-pagination allows for easy Digg-style pagination without modifying your views

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/django_pagination-*
%python_sitelibdir/pagination*


%changelog
* Fri Apr 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- Initial build for ALT Linux
