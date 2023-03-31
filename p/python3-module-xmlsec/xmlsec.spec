%define oname xmlsec

%def_without check

Name: python3-module-%oname
Version: 1.3.13
Release: alt1

Summary: Python bindings for the XML Security Library

License: MIT
Group: Development/Python3
Url: https://github.com/mehcode/python-xmlsec

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-lxml

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README* LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Mar 29 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.13-alt1
- Build new version.

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.6-alt2
- build for python2 disabled

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- NMU: Add URL (Closes: #34693).

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3
- Introduce documentation

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Fresh build from Pypi
- Thanks real@ for old python-module-mehcode-xmlsec

