%define _unpackaged_files_terminate_build 1
%define pypi_name playwright
%define mod_name %pypi_name
# The client works only with the playwright-core build that upstream pins in
# DRIVER_VERSION, as a microsoft/playwright commit; npm publishes this one as
# driver_version.
%define driver_commit a1f35e1955976e84411f9c10358228a80b763ebe
%define driver_version 1.65.0

# The tests launch Chromium, Firefox and WebKit, but ALT has no WebKit
# build of Playwright.
%def_without check

Name: python3-module-%pypi_name
Version: 1.65.0
Release: alt1

Summary: Python library to automate Chromium and Firefox browsers with a single API
License: Apache-2.0
Group: Development/Python3
Url: https://playwright.dev/python/
Vcs: https://github.com/microsoft/playwright-python
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
# Drops the upstream sdist and bdist_wheel commands: they build the driver
# from a microsoft/playwright checkout and download the Node.js binary.
# The driver comes from node-playwright instead.
Patch: %name-%version-alt.patch

Requires: node-playwright = %driver_version
# driver/node links to the system Node.js. Upstream supports Node.js 22, 24
# and 26; PLAYWRIGHT_NODEJS_PATH selects another one, e.g. /usr/bin/node24.
Requires: node >= 22
# The PyInstaller hooks only run inside PyInstaller, which imports them
# itself; playwright never imports them.
%add_python3_req_skip PyInstaller.utils.hooks

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-macros-pyproject
# auditwheel is used only by the upstream bdist_wheel command that the ALT
# patch drops; setup.py imports it optionally.
%add_pyproject_deps_build_filter 'auditwheel$'
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
Playwright is a Python library to automate Chromium and Firefox
browsers with a single API. Playwright delivers automation that is
ever-green, capable, reliable and fast.

The JavaScript driver comes from the node-playwright package and
runs on the system Node.js. It runs the system browsers: install
node-playwright-chromium, node-playwright-firefox or both, and
node-playwright-ffmpeg for video recording. Browser downloads with
"playwright install" are disabled, and WebKit is not available.

%prep
%setup
%autopatch -p1
# node-playwright %driver_version must be the build that upstream pins.
test "$(cat DRIVER_VERSION)" = %driver_commit
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
%pyproject_install
# The client runs driver/node driver/package/cli.js from its own directory.
mkdir %buildroot%python3_sitelibdir/%mod_name/driver
ln -s %nodejs_sitelib/playwright-core \
	%buildroot%python3_sitelibdir/%mod_name/driver/package
ln -s %_bindir/node %buildroot%python3_sitelibdir/%mod_name/driver/node

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 13 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.65.0-alt1
- Updated to 1.65.0.
- Built as noarch, available on i586 too. Browsers are no longer
  required: install node-playwright-chromium, node-playwright-firefox
  or both.

* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.63.0-alt1.1
- Build with the separate source-built system Node.js driver.
- Build architecture-dependent packages; exclude i586.

* Tue Oct 06 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.63.0-alt1
- Initial build for Sisyphus.
