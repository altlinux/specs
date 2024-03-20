%define _unpackaged_files_terminate_build 1
%define pypi_name k5test

Name: python3-module-%pypi_name
Version: 0.10.4
Release: alt1
Summary: Library for setting up self-contained Kerberos 5 environments
License: ISC and MIT
Group: Development/Python3
Url: https://pypi.org/project/k5test/
VCS: https://github.com/pythongssapi/k5test
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
Requires: /usr/bin/krb5-config
Requires: krb5-kdc
Requires: krb5-kinit
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# there is no upstream tests (.github/workflows/ci.yml)

%files
%python3_sitelibdir/k5test/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 0.10.4-alt1
- 0.10.3 -> 0.10.4.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 0.10.3-alt1
- 0.10.2 -> 0.10.3.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- 0.10.1 -> 0.10.2.

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

