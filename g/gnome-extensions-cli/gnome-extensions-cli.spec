%define oname gnome_extensions_cli

Name: gnome-extensions-cli
Version: 0.11.0
Release: alt1

Summary: Command line tool to manage your Gnome Shell extensions
License: Apache-2.0
Group: System/Configuration/Other

Url: https://github.com/essembeh/gnome-extensions-cli
Vcs: https://github.com/essembeh/gnome-extensions-cli

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry python3-module-wheel

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
%doc LICENSE README.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Mar 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.0-alt1
- Initial build for Alt Linux (git.73837d99).

