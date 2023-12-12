%define oname click-plugins
%def_with check

Name: python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: Register CLI commands via setuptools entry-points
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/click-plugins

BuildArch: noarch

# https://github.com/click-contrib/click-plugins.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
An extension module for click to enable registering CLI commands via
setuptools entry-points.

%package examples
Summary: Examples for %oname
Group: Development/Documentation
BuildArch: noarch

%description examples
An extension module for click to enable registering CLI commands via
setuptools entry-points.

This package contains examples for %oname.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%files examples
%doc example/*

%changelog
* Sat Dec 02 2023 Mikhail Chernonog <snowmix@altlinux.org> 1.1.1-alt1
- 1.0.2 -> 1.1.1
- Delete patch.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- replace BR python3-module-click-tests with python3-module-click

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- Build for python2 disabled.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Fixed testing against Click 7.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20150720
- Initial build for Sisyphus

