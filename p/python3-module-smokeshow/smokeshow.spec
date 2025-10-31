%define _unpackaged_files_terminate_build 1
%define pypi_name smokeshow
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: CLI to deploy ephemeral websites
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/smokeshow/
Vcs: https://github.com/samuelcolvin/smokeshow
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-aiohttp-tests
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Deploy ephemeral websites via HTTP or a CLI.

If you need to do any of the following:
* preview a site before launch
* view the HTML version of coverage reports
* create a quick website to show someone something

smokeshow is here to help. It lets you create a static website, 1 year
after the site is created, it vanishes like smoke in the wind.

What's great about smokeshow:
* It's free
* You don't need to sign up, just create a key using the instructions
  below
* It's super fast around the world, smokeshow uses CloudFlare's 280+
  edge locations to store files meaning they're next to your users
  wherever they are

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 31 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.5.0-alt1
- Initial build for ALT Sisyphus.
