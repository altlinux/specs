Name: blktop
Version: 0.1
Release: alt1

Summary: top-like monitoring block devices metrics (latency, IOPS and so on)

Group: File tools
License: Public domain
Url: https://github.com/amarao/blktop

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/amarao/blktop
Source: %name-%version.tar

BuildArch: noarch

# manually removed: BuildRequires: libdb4-devel python3 ruby ruby-stdlibs
# Automatically added by buildreq on Thu Sep 25 2014
# optimized out: python3-base


%description
top-like monitoring block devices metrics (latency, IOPS and so on)

%prep
%setup

%install
install -m0755 -D %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Thu Sep 25 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
