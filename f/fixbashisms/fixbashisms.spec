Name: fixbashisms
Version: 0.1
Release: alt1

Summary: Fix bashisms in shell code

License: AGPLv3
Group: Development/Other
Url: https://github.com/vitlav/fixbashisms

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/vitlav/fixbashisms.git
Source: %name-%version.tar

BuildArchitectures: noarch

%description
Fix bashisms in shell code.

Recommended tools: checkbashisms, shellcheck.

%prep
%setup

%install
install -D -m0755 fixbashisms.sh %buildroot%_bindir/fixbashisms

%files
%_bindir/%name
#%_man1dir/*

%changelog
* Thu Nov 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
