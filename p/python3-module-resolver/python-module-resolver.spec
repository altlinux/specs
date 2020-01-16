%define oname resolver

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Resolve specially formated statements to Python objects.

License: LGPL
Group: Development/Python3
URL: http://lukearno.com/projects/resolver/
BuildArch: noarch
Packager: Sergey Alembekov <rt@altlinux.ru>

Source0: %oname.tar

BuildRequires(pre): rpm-build-python3


%description
%summary

%prep
%setup -q -n %oname

%build
%__python3 setup.py build

%install
%__python3 setup.py install --root=%buildroot --optimize=2

%files
%defattr(-,root,root)
%python3_sitelibdir/*


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- porting on python3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.2.1-alt1
- initial build for ALTLinux
