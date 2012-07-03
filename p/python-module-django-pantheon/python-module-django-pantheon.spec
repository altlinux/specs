%define version 0.0.0
%define release alt2.svn1916.1
%setup_python_module django-pantheon

Name: %packagename
Version: %version
Release: %release.1

Summary: Pantheon django modules

License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://webnewage.org/projects/p/django-pantheon
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildRequires: python-module-setuptools

%description
Pantheon django modules

%prep
%setup -n %modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.0-alt2.svn1916.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt2.svn1916.1
- Rebuilt with python 2.6

* Sat Feb 14 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt2.svn1916
- critical fix wrong call invalidate function

* Fri Feb 13 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.svn1916
- Initial build for ALT Linux

