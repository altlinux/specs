%define _name configobj

Name: python-module-%_name
Version: 4.7.2
Release: alt1.1

Summary: a Python module for easy reading and writing of config files
License: BSD
Group: Development/Python
Url: http://www.voidspace.org.uk/python/configobj.html
Packager: Yuri N. Sedunov <aris@altlinux.org>

Source: http://downloads.sourceforge.net/%_name/%_name-%version.zip

BuildArch: noarch

BuildPreReq: unzip rpm-build-python rpm-build-compat
BuildRequires: python-devel python-module-setuptools

%description
ConfigObj - a Python module for easy reading and writing of config
files.

%prep
%setup -q -n %_name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%_name-*.egg-info/
%python_sitelibdir/%_name.*
%python_sitelibdir/validate.*
%doc docs/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.2-alt1.1
- Rebuild with Python-2.7

* Sat Oct 30 2010 Yuri N. Sedunov <aris@altlinux.org> 4.7.2-alt1
- new version (ALT #24462)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.3-alt1.1
- Rebuilt with python 2.6

* Wed Oct 29 2008 Yuri N. Sedunov <aris@altlinux.org> 4.5.3-alt1
- first build for Sisyphus

