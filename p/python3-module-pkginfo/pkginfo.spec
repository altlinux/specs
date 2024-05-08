%define _unpackaged_files_terminate_build 1
%define pypi_name pkginfo
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.10.0
Release: alt1
Summary: Query metadatdata from sdists / bdists / installed packages
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pkginfo/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/pkginfo{,.py3}

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/pkginfo.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests

%changelog
* Tue May 07 2024 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.6 -> 1.10.0.

* Wed Jan 24 2024 Anton Vyatkin <toni@altlinux.org> 1.9.6-alt2
- (NMU) Fixed FTBFS.

* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 1.9.6-alt1
- (NMU) New version 1.9.6
- Fix BuildRequires
- Enable check

* Tue Aug 10 2021 Grigory Ustinov <grenka@altlinux.org> 1.2-alt3
- Build without docs.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2.b1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt2.b1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.2-alt2.b1
- cleanup buildreq

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b1
- Initial build for Sisyphus

