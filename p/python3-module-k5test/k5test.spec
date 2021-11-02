%define _unpackaged_files_terminate_build 1
%define mname k5test

Name: python3-module-%mname
Version: 0.10.1
Release: alt1
Summary: Library for setting up self-contained Kerberos 5 environments

Group: Development/Python3
License: ISC and MIT
# Source git: https://github.com/pythongssapi/k5test.git
Url: https://pypi.python.org/pypi/k5test

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

BuildArch: noarch

Requires: /usr/bin/krb5-config
Requires: krb5-kdc
Requires: krb5-kinit

%description
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info

%changelog
* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.

* Wed Sep 01 2021 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.2 -> 0.10.0.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.2-alt5
- Drop python2 support.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 0.9.2-alt4
- Added dependency on krb5 stuff.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2
- NMU: remove %%ubt from release

* Fri Mar 30 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2

* Mon Nov 20 2017 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- Initial build

