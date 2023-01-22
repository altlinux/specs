%define oname curtsies

Name: python3-module-curtsies
Version: 0.4.1
Release: alt1

Summary: Library for interacting with the terminal

License: MIT
Group: Development/Python3
Url: https://github.com/bpython/curtsies

BuildArch: noarch

# Source-url: https://github.com/bpython/curtsies/archive/refs/tags/v%version.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Curtsies is a library for interacting with the terminal.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt1
- build python3 new version seperately

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.19-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.19-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.19-alt1
- Initial build.
