%define _unpackaged_files_terminate_build 1
%define pypi_name memphis-py
%define mod_name memphis

Name: python3-module-%pypi_name
Version: 1.1.3
Release: alt1

Summary: Python client for Memphis. Memphis is an event processing platform
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/memphis-py/
Vcs: https://github.com/memphisdev/memphis.py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%set_pyproject_deps_check_filter types-
%add_pyproject_deps_check_filter wemake-python-styleguide
%add_pyproject_deps_check_filter yesqa
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A simple, robust, and durable cloud-native message broker wrapped with
an entire ecosystem that enables cost-effective, fast, and reliable
development of modern queue-based use cases.

Memphis enables the building of modern queue-based applications that
require large volumes of streamed and enriched data, modern protocols,
zero ops, rapid development, extreme cost reduction, and a
significantly lower amount of dev time for data-oriented developers
and data engineers.

%prep
%setup

# that's funny
sed -i 's/"asyncio", //' setup.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.

