%define module_name daemon

Name: python-module-%module_name
Version: 1.5.5
Release: alt2.1

Summary: Library to implement a well-behaved Unix daemon process


License: PSF-2
Group: Development/Python
Url: http://pypi.python.org/pypi/python-daemon/

Source: python-%module_name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%setup_python_module %module_name


%description
Library to implement a well-behaved Unix daemon process.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc ChangeLog LICENSE.PSF-2
%python_sitelibdir/daemon
%python_sitelibdir/python_daemon*


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.5-alt2
- pidlockfile.py: add checking for stale {pid,lock}file

* Sun Apr 04 2010 Denis Klimov <zver@altlinux.org> 1.5.5-alt1
- Initial build for ALT Linux


