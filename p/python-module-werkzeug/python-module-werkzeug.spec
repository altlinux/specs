%define version 0.6.2
%define release alt1
%setup_python_module werkzeug

Summary: Werkzeug is one of the most advanced WSGI utility modules
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename.tar
License: MIT
Group: Development/Python
BuildArch: noarch
URL: http://werkzeug.pocoo.org/
Packager: Sergey Alembekov <rt@altlinux.ru>

BuildRequires: python-module-setuptools

%description
%summary

%prep
%setup -q -n %modulename

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
