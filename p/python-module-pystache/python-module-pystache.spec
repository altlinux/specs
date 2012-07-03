%define sname pystache
Summary: Mustache in Python 
Name: python-module-%sname
Version: 0.3.1
Release: alt1.1
Source0: %name-%version.tar
License: BSD
Group: Development/Python
URL: https://github.com/defunkt/pystache
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

BuildRequires: python-devel >= 2.6
BuildRequires: python-module-setuptools

%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to render logic-free views.
Pystache is a Python implementation of Mustache.

%prep
%setup -q
rm -rf tests

%build
%python_build

%install
%python_install

%files
%doc LICENSE HISTORY.rst README.rst
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.3.1-alt1
- initial build



