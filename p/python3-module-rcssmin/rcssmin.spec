%define oname rcssmin

Name: python3-module-%oname
Version: 1.0.6
Release: alt3
Summary: CSS Minifier
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/%oname

# https://github.com/ndparker/rcssmin.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
rCSSmin is a CSS minifier written in python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc %_docdir/%oname
%python3_sitelibdir/*

%changelog
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

