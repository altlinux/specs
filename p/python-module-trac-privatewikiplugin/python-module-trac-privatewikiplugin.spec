%define tarname privatewikiplugin
Name: python-module-trac-privatewikiplugin
%define r_minor r7916
Version: 1.0.0
Release: alt1.%r_minor.1

Summary: Allows you to protect wiki pages against access.

Group: Development/Python
License: BSD
Url: http://trac-hacks.org/wiki/privatewikiplugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
Allows you to protect wiki pages against access

%prep
%setup -q -n %tarname/0.11

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1.r7916
- Build for ALT
