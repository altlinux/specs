Name: google-chrome-preinstall
Version: 0.1
Release: alt1

Summary: Set correct environment for Google Chrome
License: GPL
Group: Networking/WWW

Url: https://chrome.google.com/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: google-chrome

%description
Set correct environment for Google Chrome

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/google-chrome

%files
%_sysconfdir/default/google-chrome

%changelog
* Mon Apr 07 2014 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux
