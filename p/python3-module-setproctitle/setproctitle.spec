%define oname setproctitle

%def_enable check

Name: python3-module-%oname
Version: 1.3.3
Release: alt1

Summary: A library to allow customization of the process title
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/setproctitle
VCS: https://github.com/dvarrazzo/py-setproctitle

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: /proc
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
The library allows a process to change its title (as displayed by system
tools such as ps and top).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -k "not embedded" -vra

%files
%doc COPYRIGHT *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Fri Sep 16 2022 Danil Shein <dshein@altlinux.org> 1.3.1-alt1
- new version 1.3.1
  + migrate to pyproject

* Thu Jun 23 2022 Danil Shein <dshein@altlinux.org> 1.2.3-alt1
- new version 1.2.3

* Tue May 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.10-alt3
- Deprecation warning fixed (Closes #38459).

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.10-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.10-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- New version 1.1.10
- Disable check

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.9-alt1.dev0.git20140903.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.dev0.git20140903
- Initial build for Sisyphus

