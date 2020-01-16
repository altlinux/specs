%define oname selector

Name: python3-module-%oname
Version: 0.8.11
Release: alt2

Summary: WSGI delegation based on URL path and method.

License: LGPL
Group: Development/Python
URL: http://lukearno.com/projects/selector/
Packager: Sergey Alembekov <rt@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-resolver


%description
%summary

%prep
%setup

%build
%__python3 setup.py build

%install
%__python3 setup.py install --root=%buildroot --optimize=2

%files
%defattr(-,root,root)
%doc COPYING README
%python3_sitelibdir/*


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.11-alt2
- porting on python3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.11-alt1.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.11-alt1
- initial build for ALTLinux
