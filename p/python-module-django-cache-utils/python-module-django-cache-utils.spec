%define module_name django-cache-utils

Name: python-module-%module_name
Version: 0.7.2
Release: alt1

Summary: Caching decorator and django cache backend with advanced invalidation ability and dog-pile effect prevention

License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/django-cache-utils

Source: %module_name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
django-cache-utils provides some utils for make cache-related work easier

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/django_cache_utils-*
%python_sitelibdir/cache_utils*


%changelog
* Wed Aug 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- Initial build for ALT Linux
