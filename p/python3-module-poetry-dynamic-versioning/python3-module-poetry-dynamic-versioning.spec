%define _unpackaged_files_terminate_build 1
%define pypi_name poetry-dynamic-versioning
%define srcname poetry_dynamic_versioning

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: Plugin for Poetry to enable dynamic versioning based on VCS tags
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/poetry-dynamic-versioning/
Vcs: https://github.com/mtkennerly/poetry-dynamic-versioning
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Python plugin for Poetry 1.2.0+ and Poetry Core 1.0.0+ to enable dynamic
versioning based on tags in your version control system. Many different version
control systems are supported, including Git and Mercurial.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
#every test reaches out to the internet

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%srcname
%python3_sitelibdir/%{pyproject_distinfo %srcname}

%changelog
* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Thu May 02 2024 Anton Kurachenko <srebrov@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Mar 09 2024 Anton Kurachenko <srebrov@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
