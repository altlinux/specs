%define _unpackaged_files_terminate_build 1
%define pypi_name httpbin

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.1
Release: alt1

Summary: HTTP Request and Response Service
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/httpbin/
Vcs: https://github.com/psf/httpbin

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc AUTHORS README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- Updated to 0.10.1.
- Changed upstream to PSF (Python Software Foundation).

* Mon Sep 26 2022 Danil Shein <dshein@altlinux.org> 0.7.0-alt3
- NMU: Fix Werkzeug 2.1.x compatibility
  + enable tests

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt2
- Fixed FTBFS.
- Fixed packaging.

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.7.0
- built without python-2.7 support

* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1.1
- Fixed requires

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1
- Updated version to 0.6.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140826.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140826.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140826
- Initial build for Sisyphus
