%define sname retrying

Name: python3-module-%sname
Version: 1.3.4
Release: alt1
Summary: Retrying library
Group: Development/Python3
License: Apache-2.0
Url:  https://github.com/rholder/retrying
Source: %sname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Simplify the task of adding retry behavior to just about anything.

%prep
%setup -n %sname-%version

# Remove bundled egg-info
rm -rf %sname.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE AUTHORS.rst
%python3_sitelibdir/*

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.3-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- initial build
