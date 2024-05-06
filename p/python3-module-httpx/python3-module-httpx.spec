Name:    python3-module-httpx
Version: 0.27.0
Release: alt1

Summary: A next generation HTTP client for Python
License: BSD-3-Clause
Group:   Development/Python
URL:     https://www.python-httpx.org/

# Source-url: https://github.com/encode/httpx/archive/%version.tar.gz
Source0: httpx-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
HTTPX is a fully featured HTTP client for Python 3,
which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

Note: HTTPX should be considered in beta.
We believe we've got the public API to a stable point now,
but would strongly recommend pinning your dependencies to the 0.13.* release,
so that you're able to properly review API changes between package updates.
A 1.0 release is expected to be issued sometime around mid-2020.

%prep
%setup -n httpx-%version

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/httpx
%python3_sitelibdir/httpx-%version.dist-info

%changelog
* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.27.0-alt1
- 0.27.0 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.26.0-alt1
- 0.26.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24.0-alt1
- 0.24.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.0-alt2
- 0.23.0

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt2
- drop upper bound on httpcore version

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.2-alt1
- 0.18.2

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.17.1-alt1
- new version 0.17.1 (with rpmrb script)

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 1.16.1

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13.2-alt1
- initial build for Sisyphus
