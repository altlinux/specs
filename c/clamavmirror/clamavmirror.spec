Name: clamavmirror
Version: 0.0.5
Release: alt1

Summary: ClamAV Signature Mirroring Tool

Group: File tools
License: MPL-2.0
Url: https://github.com/akissa/clamavmirror

# Source-git: https://github.com/akissa/clamavmirror.git
Source: %name-%version.tar

BuildArch: noarch

AutoProv: no

BuildRequires(pre): rpm-build-python3

# use sigtool from it
Requires: clamav

%description
ClamAV Signature Mirroring Tool.

%prep
%setup
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 0.0.5-alt1
- initial build for ALT Sisyphus
