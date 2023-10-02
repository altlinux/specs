%global oname ConfigArgParse

Name: python3-module-configargparse
Version: 1.7
Release: alt1

Summary: A Python module with support for argparse, config files, and env variables

License: MIT
Group: Development/Python3
Url: https://github.com/bw2/ConfigArgParse

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools

%description
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%doc LICENSE
%python3_sitelibdir/configargparse.py*
%python3_sitelibdir/%{oname}*.egg-info
%python3_sitelibdir/__pycache__/configargparse*

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version 1.7 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version 1.5.3 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt2
- build python3 module separately

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt1
- new version 0.14.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0 for Let's Encrypt dep

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-3
- Remove old parts

* Fri Oct 30 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-2
- Update macros

* Thu Feb 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Initial package
