%define _altdata_dir %_datadir/alterator

Name: installer-alterator-livecd
Version: 0.1.2
Release: alt1

Summary: Special steps for run installer in LiveCD desktop
License: GPL-3.0-or-later
Group: System/Configuration/Other

Url: https://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator
BuildRequires: alterator

BuildArch: noarch

Conflicts: alterator-livecd
Requires: alterator-notes

%description
%summary.
Fork alterator-livecd.

%package stage2
Summary: %summary
Group: System/Configuration/Other
BuildArch: noarch

%description stage2
%summary.
This package contains common installer stage2 files and dependencies.

%package stage3
Summary: %summary
Group: System/Configuration/Other
BuildArch: noarch
Requires: rootfs-installer-features

%description stage3
%summary.
This package contains common installer stage3 files and dependencies.

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/alterator/steps/*
%_datadir/alterator/ui/livecd/start
%_datadir/install2/preinstall.d/*
%_libexecdir/alterator/hooks/*
%_alterator_backend3dir/livecd-start

%files stage3
%_datadir/alterator/ui/livecd/finish
%_alterator_backend3dir/livecd-finish

%changelog
* Mon Apr 07 2025 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt1
- backend3/livecd-start: fix run $livecd_initinstall_dir/*
- livecd-finish: make the log more informative
- fix for run postinstall scripts, which use $datadir

* Sun Apr 06 2025 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- livecd-finish: do not use chroot to root
- add preinstall scritpt for copy postinstall to $destdir/run/
- split into two subpackages stage2 and stage3

* Thu Apr 03 2025 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- initial fork
