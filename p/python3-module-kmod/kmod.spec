%global pypi_name kmod

Name:           python3-module-%{pypi_name}
License:        LGPLv2+
Group:          Development/Python3
Summary:        Python module to work with kernel modules
Version:        0.9.2
Release:        alt1
# Old upstream
# URL:            https://github.com/agrover/python-kmod/
# Fork
URL:            https://github.com/maurizio-lombardi/python-kmod.git
Packager:       Python Development Team <python@packages.altlinux.org>
Source:         %{pypi_name}-%{version}.tar
BuildRequires:  libkmod-devel

BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-Cython

%description
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install

%files
%doc COPYING.LESSER README
%{python3_sitelibdir}/kmod/*
%{python3_sitelibdir}/kmod*.egg-info

%changelog
* Tue Dec 19 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.9.2-alt1
- Changed upstream to fork
- Updated to 0.9.2

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.9-alt3
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9-alt2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9-alt1
- First build for ALT (based on Fedora 0.9-4.fc21.src)
