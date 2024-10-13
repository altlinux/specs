%define oname rcssmin

%def_with check

Name: python3-module-%oname
Version: 1.1.3
Release: alt1

Summary: CSS Minifier

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/rcssmin
VCS: https://github.com/ndparker/rcssmin

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
rCSSmin is a CSS minifier written in python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%python3_sitelibdir/%oname.py
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/__pycache__
%python3_sitelibdir/_%oname.*.so

%changelog
* Sun Oct 13 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Automatically updated to 1.1.3.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1
- Automatically updated to 1.1.2.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt3
- Fixed BuildRequires.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- Initial build for Sisyphus

