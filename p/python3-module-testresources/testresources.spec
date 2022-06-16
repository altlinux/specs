%global pypi_name testresources
%def_disable check

Name:           python3-module-%{pypi_name}
Version:        2.0.1
Release:        alt3
Summary:        Testresources, a pyunit extension for managing expensive test resources

Group:          Development/Python3
License:        Apache-2.0 and BSD and GPLv2+
# file testresources/tests/TestUtil.py is GPLv2+
URL:            https://launchpad.net/testresources
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-testtools
BuildRequires: python3-module-fixtures

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%prep
%setup
# Remove bundled egg-info
rm -rf lib/%{pypi_name}.egg-info

%build
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

%files
%doc README.rst NEWS doc
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py%_python3_version.egg-info

%changelog
* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt3
- Fixed FTBFS.

* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Drop python2 support.

* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.7-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.7-alt1
- First build for ALT (based on Fedora 0.2.7-6.fc21.src)

