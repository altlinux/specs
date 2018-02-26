Name: python-module-redis
Version: 2.2.2
Release: alt1.1
Summary: Python client for Redis key-value store
Group: Development/Python
License: MIT
Url: https://github.com/andymccurdy/redis-py
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version-%release.tar
BuildArch:      noarch
BuildRequires:  python-devel

%description
This is the Python interface to the Redis key-value store.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc CHANGES INSTALL LICENSE README.md 
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Mikhail Pokidko <pma@altlinux.org> 2.2.2-alt1
- initial build

