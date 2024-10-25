%define _unpackaged_files_terminate_build 1
%define pypi_name netius
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.20.0
Release: alt1
Summary: Fast and readable async non-blocking network apps
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/netius/
Vcs: https://github.com/hivesolutions/netius
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
# link to system ca bundle, wheel resolves it and makes a copy
ln -sf /etc/pki/tls/certs/ca-bundle.crt \
    %buildroot/%python3_sitelibdir/%mod_name/base/extras/net.ca

%check
%pyproject_run_pytest -vra

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/examples

%changelog
* Thu Oct 24 2024 Stanislav Levin <slev@altlinux.org> 1.20.0-alt1
- 1.17.52 -> 1.20.0.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 1.17.52-alt2.1
- NMU: Added zombie-imp to BuildRequires.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.17.52-alt2
- Rename package, cleanup spec.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.52-alt1
- new version 1.17.52 (with rpmrb script)
- python3 only

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt1.git20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.3-alt1.git20150202.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.git20150202
- Initial build for Sisyphus

