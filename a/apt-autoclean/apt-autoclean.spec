Name: apt-autoclean
Version: 0.1
Release: alt1

Summary: regularly prune stale part of apt's cache
License: Public domain
Group: System/Configuration/Packaging

Url: https://bugzilla.altlinux.org/show_bug.cgi?id=918
Source: apt-autoclean.sh
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package contains a cronjob to regularly perform
"apt-get autoclean" which cleans up apt's cache but only removes
package files that can no longer be downloaded, and are largely
useless.  This allows a cache to be maintained over a long period
without it growing out of control.

The configuration option APT::Clean-Installed will prevent
installed packages from being erased if it is set to off.

%install
install -pDm644 %SOURCE0 %buildroot%_sysconfdir/cron.weekly/%name

%files
%attr(750,root,root) %config(noreplace) %_sysconfdir/cron.weekly/*

%changelog
* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- created for ALT Linux (closes: #918)
  + based on makewhatis weekly job script
