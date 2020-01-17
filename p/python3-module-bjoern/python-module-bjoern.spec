%define oname bjoern

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: A screamingly fast Python WSGI server written in C.
License: BSD
Group: Development/Python
URL: https://github.com/jonashaag/bjoern

Source0: %oname.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libev-devel


%description
%summary

%prep
%setup -q -n %oname

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG LICENSE README.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/*.so
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/__pycache__/


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.0-alt1
- Version updated to 3.1.0
- porting on python3.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Thu Jun 09 2011 Sergey Alembekov <rt@altlinux.ru> 1.2-alt1
- initial build for ALTLinux.
