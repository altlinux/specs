%define oname dockerpty

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: Use the pseudo-tty of a docker container.

License: %asl
Group: Development/Python3
Url: https://github.com/d11wtq/dockerpty

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
Python library to use the pseudo-tty of a docker container.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Sep 8 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.1-alt2
- build Python3 version as separate package

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.1-alt1.3
- rebuild with python3.8

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.3.4-alt1
- 0.3.4
