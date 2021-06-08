%global pypi_name testrepository

Name:           python3-module-%{pypi_name}
Version:        0.0.20
Release:        alt3

Summary:        A repository of test results
Group:          Development/Python3
License:        Apache-2.0
URL:            https://launchpad.net/testrepository
BuildArch:      noarch

Source0:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-mimeparse
BuildPreReq: python3-module-pbr python3-module-unittest2
BuildPreReq: python3-module-fixtures python3-module-subunit
BuildPreReq: python3-module-testtools python3-module-extras

Conflicts: python-module-%pypi_name
Obsoletes: python-module-%pypi_name

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.txt Apache-2.0
%{_bindir}/testr
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.0.20-alt3
- Drop python2 support.

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.20-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.20-alt1.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20-alt1
- Version 0.0.20

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt3
- Enable python3

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt1
- First build for ALT (based on Fedora 0.0.18-1.fc21.src)

