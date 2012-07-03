Name: python-module-hotqueue
Version: 0.2.3
Release: alt1.1
Summary: Simple library that allows to use Redis as a message queue.
Group: Development/Python
License: MIT
Url: https://github.com/richardhenry/hotqueue
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version-%release.tar
BuildArch:      noarch
BuildRequires:  python-devel

%description
HotQueue is a Python library that allows you to use Redis as a message queue within your Python programs.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc REQUIREMENTS LICENSE README.rst
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Mikhail Pokidko <pma@altlinux.org> 0.2.3-alt1
- initial build

