%define tarname footnotemacro
Name: python-module-trac-footnotemacro
%define r_minor r9436
Version: 1.03
Release: alt1.%r_minor.1

Summary: The FootNoteMacro automatically collates and generates footnotes

Group: Development/Python
# FIXME: unknown?
License: BSD
Url: http://trac-hacks.org/wiki/FootNoteMacro

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
The FootNoteMacro automatically collates1 and generates footnotes

%prep
%setup -q -n %tarname/0.11

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

chmod -R a+r %buildroot%python_sitelibdir/%tarname

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.03-alt1.r9436.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.03-alt1.r9436
- New version

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.02-alt2.r7916
- Fix URL

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.02-alt1.r7916
- Build for ALT
