%define oname rcssmin

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1
Summary: CSS Minifier
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/%oname

# https://github.com/ndparker/rcssmin.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
rCSSmin is a CSS minifier written in python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%python3_sitelibdir/%oname.py
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%python3_sitelibdir/__pycache__
%python3_sitelibdir/_%oname.*.so

%changelog
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

