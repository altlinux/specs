%define allow_dir %_sysconfdir/appinstall/allow.d/

Name: appinstall-allowlist-kworkstation
Version: 1.0.0
Release: alt1

Group: System/Configuration/Other
Summary: Allow list for appinstall
License: MIT
URL: http://altlinux.org/gears/a/appinstall-allowlist-kworkstation.git

BuildArch: noarch

Requires: appinstall

Source: kworkstation.list


%description
Allow list for appinstall application.

%prep
%setup -Tc

%install
mkdir -p %buildroot/%allow_dir/
ls -al `dirname %SOURCE0`
install -m 0644 %SOURCE0 %buildroot/%allow_dir/

%files
%config(noreplace) %allow_dir/*

%changelog
* Wed May 10 2023 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- initial build
