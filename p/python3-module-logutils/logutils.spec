%global modname logutils

Name:               python3-module-%{modname}
Version:            0.3.5
Release:            alt2
Summary:            Logging utilities

Group:              Development/Python3
License:            BSD
URL:                http://pypi.python.org/pypi/logutils
Source0:            %{modname}-%{version}.tar
Patch:              set-default-log-level.patch

BuildArch:          noarch

BuildRequires:      rpm-build-python3

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and so
they are packaged here. Others are updated versions which have appeared in
recent Python releases, but are usable with older versions of Python and so
are packaged here.

%prep
%setup -n %{modname}-%{version}
%patch -p1

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

%files
%doc README.rst LICENSE.txt NEWS.txt doc/
%{python3_sitelibdir}/%{modname}/
%{python3_sitelibdir}/%{modname}-%{version}-*

%changelog
* Mon Feb 27 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.5-alt2
- Fixed FTBFS.

* Wed May 25 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.5-alt1
- Build new version.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.3-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.3-alt1
- First build for ALT (based on Fedora 0.3.3-3.fc21.src)

