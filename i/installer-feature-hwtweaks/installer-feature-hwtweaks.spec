Name: installer-feature-hwtweaks
Version: 0.2
Release: alt1

Summary: Install-time hardware tweaks
License: GPL
Group: System/Configuration/Other

Url: http://www.freesource.info/wiki/TZ/AltLinux/WhiteLabel
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
%summary

%package stage2
Summary: %summary
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Conflicts: installer-ltsp-school-stage2 <= 0.4-alt4.4
Conflicts: installer-ltsp-stage2 <= 0.1-alt2.5.7
Conflicts: installer-junior-school-stage2 <= 0.4-alt5
Conflicts: installer-junior-stage2 <= 0.4-alt4

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*
%_datadir/install2/hw.d/*

%changelog
* Tue Apr 22 2008 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- errorlevel-happy

* Mon Mar 31 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- noarch (scripts _are_ x86-specific; if there's need to
  distinguish some day, rename the package to %%name-x86)

* Tue Mar 11 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release based on installer-junior-0.4-alt4

