%define sname anyjson
Summary: Get the best JSON encoder/decoder available on this system
Name: python-module-%sname
Version: 0.3.1
Release: alt1
Source0: %name-%version.tar
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/anyjson/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
Convenience module to import the best available json serialize/deserializer installed.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc README LICENSE CHANGELOG
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%changelog
* Thu May 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.4-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.2.4-alt1
- initial build
