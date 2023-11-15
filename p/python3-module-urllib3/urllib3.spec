%define _unpackaged_files_terminate_build 1
%define pypi_name urllib3
%define mod_name %pypi_name

# tests suite is very unstable (freezes or crashes) on arches different from
# x86_64
%if %_arch == x86_64
%def_with check
%else
%def_without check
%endif

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Epoch: 2
Summary: HTTP library with thread-safe connection pooling, file post, and more
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/urllib3/
Vcs: https://github.com/urllib3/urllib3
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter memray
%add_pyproject_deps_check_filter pytest-memray
%add_pyproject_deps_check_filter towncrier
%add_pyproject_deps_check_filter brotli
%pyproject_builddeps_metadata_extra socks
%pyproject_builddeps_metadata_extra brotli
%pyproject_builddeps_metadata_extra zstd
%pyproject_builddeps_check
%endif

%description
urllib3 is a powerful, user-friendly HTTP client for Python.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# to adjust timeouts: test.LONG_TIMEOUT
export CI=yes
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 14 2023 Stanislav Levin <slev@altlinux.org> 2:2.1.0-alt1
- 2.0.7 -> 2.1.0.

* Thu Oct 19 2023 Stanislav Levin <slev@altlinux.org> 2:2.0.7-alt1
- 2.0.6 -> 2.0.7.

* Tue Oct 03 2023 Stanislav Levin <slev@altlinux.org> 2:2.0.6-alt1
- 2.0.5 -> 2.0.6.

* Wed Sep 20 2023 Stanislav Levin <slev@altlinux.org> 2:2.0.5-alt1
- 2.0.4 -> 2.0.5.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 2:2.0.4-alt1
- 2.0.3 -> 2.0.4.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 2:2.0.3-alt1
- 1.26.14 -> 2.0.3.

* Tue Apr 11 2023 Anton Vyatkin <toni@altlinux.org> 2:1.26.14-alt2
- Fix BuildRequires

* Thu Jan 12 2023 Vladimir Didenko <cow@altlinux.org> 2:1.26.14-alt1
- 1.26.6 -> 1.26.14 (fixes compatibility with cryptography >= 39)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2:1.26.6-alt3
- drop deprecated ntlm support

* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 2:1.26.6-alt2
- drop circle requires python3-module-ndg-httpsclient

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 2:1.26.6-alt1
- 1.26.5 -> 1.26.6.

* Fri Jun 11 2021 Grigory Ustinov <grenka@altlinux.org> 2:1.26.5-alt1
- 1.25.10 -> 1.26.5 (Closes: #40197)
- Build without python2 support.
- Build without docs.

* Fri Jul 24 2020 Anton Farygin <rider@altlinux.ru> 2:1.25.10-alt1
- 1.25.6 -> 1.25.10

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 2:1.25.6-alt1
- 1.24.3 -> 1.25.6

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.3-alt1
- 1.24.2 -> 1.24.3 (fixes: CVE-2019-9740).

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.2-alt1
- 1.24.1 -> 1.24.2 (fixes: CVE-2019-11324).

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt2
- fixed import system six

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt1
- 1.24.1

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2:1.21.1-alt1
- 1.21.1
- Add optional test check

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2:1.15.1-alt1
- 1.15.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:20150503-alt1.1
- NMU: Use buildreq for BR.

* Fri Sep 18 2015 Lenar Shakirov <snejok@altlinux.ru> 1:20150503-alt1
- Build old snapshot - 20150503 (1.10.4)
  * Problem between python-requests and urllib3
  * Epoch: 1

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150729-alt1
- New snapshot

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150222-alt1
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150210-alt1
- New snapshot

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141214-alt1
- New snapshot

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140810-alt2
- New snapshot

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 20140708-alt2
- Unbundle ssl_match_hostname, ordereddict and six package
- Use system python-module-{six,backports.ssl_match_hostname,ordereddict}

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140708-alt1
- New snapshot
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20131126-alt1
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130915-alt1
- New snapshot

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130204-alt1
- Initial build for Sisyphus

