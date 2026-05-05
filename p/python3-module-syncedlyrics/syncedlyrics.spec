%define pypi_name syncedlyrics

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: Get an LRC format (synchronized) lyrics for your music
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/syncedlyrics
Vcs: https://github.com/moehmeni/syncedlyrics

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue May 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux.

