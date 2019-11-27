%global pypi_name xvfbwrapper
%define version 0.2.9

Name:           python3-module-%{pypi_name}
Version:        %{version}
Release:        alt2
Group:          Development/Python3
Summary:        run headless display inside X virtual framebuffer (Xvfb)

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        %{name}-%{version}.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3


%description
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/__pycache__/%{pypi_name}.*
%{python3_sitelibdir}/%{pypi_name}-%{version}-py%{_python3_version}.egg-info


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.9-alt2
- python2 disabled

* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt1.2
- Rebuild with python3.7.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 0.2.4-alt1
- First build for ALT (based on Fedora 0.2.4-2.fc24.src)
