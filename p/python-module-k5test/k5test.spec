%define _unpackaged_files_terminate_build 1
%define mname k5test

Name: python-module-%mname
Version: 0.9.2
Release: alt4
Summary: Library for setting up self-contained Kerberos 5 environments

Group: Development/Python
License: ISC
# Source git: https://github.com/pythongssapi/k5test.git
Url: https://pypi.python.org/pypi/k5test

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-six
BuildRequires: python-module-setuptools
BuildRequires: python3-module-six
BuildRequires: python3-module-setuptools

BuildArch: noarch

Requires: libkrb5-devel
Requires: krb5-kdc
Requires: krb5-kinit

%description
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%package -n python3-module-%mname
Summary: Library for setting up self-contained Kerberos 5 environments
Group: Development/Python3
Requires: libkrb5-devel
Requires: krb5-kdc
Requires: krb5-kinit

%description -n python3-module-%mname
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%prep
%setup
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd


%install
%python_install
pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-*.egg-info

%files -n python3-module-%mname
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info

%changelog
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

