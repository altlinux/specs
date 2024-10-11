%define _unpackaged_files_terminate_build 1
%define pypi_name ewmh
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.1.6
Release: alt4
Summary: An implementation of EWMH (Extended Window Manager Hints) for python, based on Xlib
License: GPLv3
Group: Development/Python3
Url: https://pypi.org/project/ewmh/
Vcs: https://github.com/parkouss/pyewmh
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
An implementation of EWMH (Extended Window Manager Hints) for python, based on
Xlib. It allows EWMH-compliant window managers (most modern WMs) to be queried
and controlled.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream doesn't have any tests

%files
%doc *.txt *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 11 2024 Stanislav Levin <slev@altlinux.org> 0.1.6-alt4
- Disabled check (see #50996).

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt3
- Build for python2 disabled.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux.
