Name: gpresult
Version: 0.0.1
Release: alt2

Summary: Display applied policies
License: GPLv3+
Group: Other
Url: https://gitlab.basealt.space/alt/gpresult
BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3(wheel), python3(hatchling)
Requires: libgvdb-gir

Source0: %name-%version.tar

%description
gpresult is used to get the result set of Group Policies that apply to a user and/or computer in domain.
The utility allows you to display a list of domain  (GPO) policies that apply to the computer and user.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%name
%python3_sitelibdir/%name/locales
%python3_sitelibdir/%name-%version.dist-info
%_bindir/%name

%changelog
* Mon Sep 02 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt2
- Initial build for Sisyphus

* Mon Aug 19 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- First build

