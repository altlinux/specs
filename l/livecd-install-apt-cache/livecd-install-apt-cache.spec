Name: livecd-install-apt-cache
Version: 0.1
Release: alt1

Summary: copy over apt's cache
License: public domain
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name.sh

BuildArch: noarch

%define hook %_libexecdir/alterator/hooks/livecd-preinstall.d/50-apt-cache.sh

%description
%summary during installation from LiveCD.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%hook

%files
%hook

%changelog
* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (closes: #29192)

