%define python_build CFLAGS="%optflags" %__python setup.py build
%define python_install %__python setup.py install --root %buildroot

Name: ibamtray
Version: 0.0.2
Release: alt1.1.1

Summary: Tray application for battery monitoring

License: GPLv3
Group: Monitoring
Url: http://www.tetonedge.net/code/ibamtray

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-module-pygtk-devel

%description
A python/gtk tray interface for ibam which is a intelligent battery monitoring. The code is based off of vubat, 
but has been exapnded to include libnotify support and wider range of status icons.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc LICENSE README
%_bindir/%name
%python_sitelibdir/*.py*
%python_sitelibdir/*.egg-info
%_pixmapsdir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.2-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.1
- Rebuilt with python 2.6

* Tue Mar 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.2-alt1
- Initial

