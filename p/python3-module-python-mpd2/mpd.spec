Name: python3-module-python-mpd2
Version: 3.1.2
Release: alt1

Summary: Client interface for the Music Player Daemon
License: LGPL-3.0
Group: Development/Python
URL: https://pypi.org/project/python-mpd2
VCS: https://github.com/mic92/python-mpd2

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreqprov: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest mpd/tests.py

%files
%python3_sitelibdir/mpd
%python3_sitelibdir/python_mpd2-%version.dist-info

%changelog
* Tue Oct 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.2-alt1
- 3.1.2 released

