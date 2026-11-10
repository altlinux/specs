%define _unpackaged_files_terminate_build 1
%define pypi_name playwright
%define mod_name %pypi_name
%define driver_version %version

%def_without check

Name: python3-module-%pypi_name
Version: 1.63.0
Release: alt1.1
Summary: Python library for browser automation

License: Apache-2.0
Group: Development/Python3
Url: https://playwright.dev/python/
VCS: https://github.com/microsoft/playwright-python
# System Chromium is unavailable on i586.
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch
Patch1: 0001-system-driver.patch
Patch2: 0002-no-auditwheel.patch

# The Python RPM generator cannot infer this cross-language protocol dependency.
Requires: node-playwright = %version

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: node
# Test dependencies are taken from the upstream requirement files:
# requirements.txt (runtime) and local-requirements.txt (test tooling).
%pyproject_builddeps_check
%pyproject_builddeps -- reqs
%endif

%description
Playwright is a Python library to automate Chromium, Firefox and WebKit
browsers with a single API. Playwright delivers automation that is
ever-green, capable, reliable and fast.

The driver is provided by node-playwright and runs on system Node.js.
The default Chromium browser is supplied by the system chromium package.

%prep
%setup
%autopatch -p1
# No .git in the source tarball: feed the version to setuptools-scm so that
# building project metadata below (and the wheel later) can determine it.
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile local-requirements.txt
%pyproject_deps_resync reqs pip_reqfile requirements.txt
%endif

%build
# No .git in the source tarball: feed the version to setuptools-scm directly.
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install --platlib
ln -sf %_licensedir/Apache-2.0 LICENSE

%check
%pyproject_run_pytest

%files
%doc --no-dereference LICENSE
%doc README.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.63.0-alt1.1
- Build with the separate source-built system Node.js driver.
- Build architecture-dependent packages; exclude i586.

* Tue Oct 06 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.63.0-alt1
- Initial build for Sisyphus.
