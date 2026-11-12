%define _unpackaged_files_terminate_build 1
%define pypi_name aiomisc
%define mod_name %pypi_name

# Very unstable tests.
%def_without check

Name: python3-module-%pypi_name
Version: 18.0.40
Release: alt1

Summary: Miscellaneous utils for asyncio
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiomisc/
Vcs: https://github.com/aiokitchen/aiomisc

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: python3-module-pytest-timeout
%pyproject_configure_with_check_filter autodoc collective-checkdocs grpcio-tools
%pyproject_configure_with_check_filter grpcio-reflection pytest-rst
%endif
%pyproject_configure_pypi_package

%description
Miscellaneous utils for asyncio.

As a programmer, you are no stranger to the challenges that come with
building and maintaining software applications. One area that can be
particularly difficult is making architecture of the software that
using asynchronous I/O.

This is where aiomisc comes in. aiomisc is a Python library that
provides a collection of utility functions and classes for working
with asynchronous I/O in a more intuitive and efficient way. It is
built on top of the asyncio library and is designed to make it easier
for developers to write asynchronous code that is both reliable and
scalable.

With aiomisc, you can take advantage of powerful features like worker
pools, connection pools, circuit breaker pattern, and retry mechanisms
such as asyncbackoff and asyncretry to make your asyncio code more
robust and easier to maintain.

%pyproject_configure_pypi_subpackage aiohttp
%pyproject_configure_pypi_subpackage asgi
%pyproject_configure_pypi_subpackage carbon
%pyproject_configure_pypi_subpackage cron
%pyproject_configure_pypi_subpackage dns
%pyproject_configure_pypi_subpackage raven
%pyproject_configure_pypi_subpackage rich
%pyproject_configure_pypi_subpackage uvicorn
%pyproject_configure_pypi_subpackage uvloop

%prep
%setup
%autopatch -p1

# fix version in aiomisc/version.py
TRIPLE=`python3 -c "print(tuple(map(int, '%version'.split('.'))))"`
sed -i "/^version_info/s/= .*$/= $TRIPLE/" aiomisc/version.py
sed -i '/^__version__/s/= .*$/= "%version"/' aiomisc/version.py

export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_setup_deps

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --session-timeout=600 -vra

%files
%doc COPYING README.rst CHANGELOG.md
%python3_sitelibdir/%{mod_name}*/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.40-alt1
- Updated to 18.0.40.

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.37-alt1
- Updated to 18.0.37.

* Wed Sep 30 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.33-alt1
- Updated to 18.0.33.

* Fri Sep 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.28-alt1
- Updated to 18.0.28.

* Fri Jul 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.26-alt1
- Updated to 18.0.26.

* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.24-alt1
- Updated to 18.0.24.

* Thu Mar 26 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.19-alt1
- Updated to 18.0.19.

* Mon Mar 23 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.17-alt1
- Updated to 18.0.17.

* Tue Mar 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 18.0.6-alt1
- Updated to 18.0.6.

* Tue Jan 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 17.10.3-alt1
- Updated to 17.10.3.

* Tue Dec 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.9.9-alt1
- Updated to 17.9.9.

* Tue Nov 11 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.9.6-alt1
- Updated to 17.9.6.

* Wed Sep 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.9.4-alt1
- Updated to 17.9.4.

* Thu Jul 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.8.1-alt1
- Updated to 17.8.1.

* Wed Jul 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.7.8-alt1
- Updated to 17.7.8.

* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 17.7.7-alt1
- Updated to 17.7.7.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 17.5.4-alt1
- Updated to 17.5.4.

* Wed Feb 07 2024 Anton Zhukharev <ancieg@altlinux.org> 17.3.41-alt1
- Updated to 17.3.41.

* Mon Oct 02 2023 Anton Zhukharev <ancieg@altlinux.org> 17.3.23-alt1
- Updated to 17.3.23.

* Thu Aug 03 2023 Anton Zhukharev <ancieg@altlinux.org> 17.3.21-alt1
- Updated to 17.3.21.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 17.2-alt1
- Initial build for ALT Sisyphus.

