%define  oname precis_i18n

Name:    python3-module-%oname
Version: 1.0.5
Release: alt1

Summary: Python3 implementation of PRECIS framework (RFC 8264, RFC 8265, RFC 8266)

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/precis-i18n
# https://github.com/byllyfish/precis_i18n
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
If you want your application to accept unicode user names and passwords,
you must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform unicode strings into a canonical form,
suitable for comparison.

This module implements the PRECIS Framework as described in:

- PRECIS Framework: Preparation, Enforcement, and Comparison of
Internationalized Strings in Application Protocols (RFC 8264)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Usernames and Passwords (RFC 8265)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Nicknames (RFC 8266)

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Sat Jan 07 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Automatically updated to 1.0.5.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt1
- Automatically updated to 1.0.4.
- Build with check.

* Wed Mar 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Automatically updated to 1.0.3.

* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Automatically updated to 1.0.2.

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Build new version.

* Thu Jun 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus (Closes: #36707).
