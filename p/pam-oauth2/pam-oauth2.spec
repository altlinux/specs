Name:    pam-oauth2
Version: 1.0.1
Release: alt1

Summary: OAuth2 pam module
License: MIT
Group:   System/Configuration/Networking
Url:     https://github.com/CyberDem0n/pam-oauth2

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: submodules.tar

BuildRequires(pre): libpam0-devel
BuildRequires: libcurl-devel

%description
This PAM module enables login with OAuth2 token instead of password.

%prep
%setup
tar xf %SOURCE1

%build
%make_build

%install
%makeinstall_std PAM_DIR=%_pam_modules_dir

%files
%doc README.md MAINTAINERS
%_pam_modules_dir/*

%changelog
* Mon Mar 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
