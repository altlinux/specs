%global srcname ConfigArgParse

Name: python-module-configargparse
Version: 0.11.0
Release: alt1

Summary: A Python module with support for argparse, config files, and env variables

License: MIT
Group: Development/Python
Url: https://github.com/bw2/ConfigArgParse

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.io/packages/source/C/%srcname/%srcname-%version.tar.gz
Buildarch: noarch

BuildRequires: python-devel
BuildRequires: python-module-distribute

#if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%package -n python3-module-configargparse
Group: Development/Python
Summary: %summary

%description -n python3-module-configargparse
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%prep
%setup -n %srcname-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%doc README.rst
%doc LICENSE
%python_sitelibdir/configargparse.py*
%python_sitelibdir/%{srcname}*.egg-info

%files -n python3-module-configargparse
%doc README.rst
%doc LICENSE
%python3_sitelibdir/configargparse.py*
%python3_sitelibdir/%{srcname}*.egg-info
%python3_sitelibdir/__pycache__/configargparse*

%changelog
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
