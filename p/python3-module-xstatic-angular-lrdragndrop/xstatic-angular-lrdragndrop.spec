%define mname xstatic
%define oname %mname-angular-lrdragndrop
%define pypi_name XStatic-Angular-lrdragndrop

Name: python3-module-%oname
Version: 1.0.2.2
Release: alt3

Summary: Angular-lrdragndrop (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-%mname

%py3_provides %mname.pkg.angular_lrdragndrop
%py3_requires %mname.pkg


%description
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2.2-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.2.2-alt2
- rebuild

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.2.2-alt1
- First build for ALT (based on Fedora 1.0.2.2-2.fc23.src)
