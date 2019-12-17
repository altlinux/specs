%define oname django-redis

Name: python3-module-%oname
Version: 4.6.0
Release: alt2

Summary: Full featured redis cache backend for Django
License: BSD
Group: Development/Python3
Url: https://github.com/niwibe/django-redis
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-redis-py


%description
Full featured redis cache backend for Django.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS.rst LICENSE README.rst
%python3_sitelibdir/*


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.0-alt2
- build for python2 disabled

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1
- Initial build for ALT Linux


