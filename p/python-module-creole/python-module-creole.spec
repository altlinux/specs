
Name: python-module-creole
Version: 0.3.3
Release: alt1.1

Summary: python-creole is an open-source creole2html and html2creole converter in pure Python.
License: GPLv3+
Group: Development/Python
BuildArch: noarch

Url: http://code.google.com/p/python-creole
# sourcecode: http://github.com/jedie/python-creole
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

%description
Python lib for:
 - creole markup -> html
 - html -> creole markup
python-creole is pure python. No external libs needed.
The creole2html part based on the creole markup parser and emitter from the MoinMoin project by Radomir Dopieralski and Thomas Waldmann.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/creole
%python_sitelibdir/tests
%python_sitelibdir/python_creole-*.egg-info
%doc AUTHORS README LICENSE

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- first build for Sisyphus
