%define _unpackaged_files_terminate_build 1
%define pypi_name Eve
%define pypi_nname eve
%define mod_name %pypi_nname

Name: python3-module-%pypi_nname
Version: 2.1.0
Release: alt1
Summary: Python REST API for Humans
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/Eve/
Vcs: https://github.com/pyeve/eve
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%pypi_name is an open source Python REST API framework designed for human beings. It
allows to effortlessly build and deploy highly customizable, fully featured
RESTful Web Services. Eve offers native support for MongoDB, and SQL backends
via community extensions.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# requires running mongodb and redis

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*/tests

%changelog
* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 0.7.8 -> 2.1.0.

* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.8-alt1
- Build new version.
- Build without python2.
- Build without docs, because they use too old api.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150112
- Version 0.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140620
- Initial build for Sisyphus

