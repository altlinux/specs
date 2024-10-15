%define variant alt-virtualization-pve
%define Variant ALT Virtualization PVE Edition

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 11.0
Release: alt0.2

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

%files
%_docsinstalldir
%_documentationdir

%changelog
* Tue Oct 15 2024 Alexey Shabalin <shaba@altlinux.org> 11.0-alt0.2
- drop docs about container and basic virtualization

* Mon Oct 14 2024 Alexey Shabalin <shaba@altlinux.org> 11.0-alt0.1
- package PVE only docs; drop OpenNebula docs

* Tue Aug 27 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt5
- fix some typos (ALT 51175, 51218, 51228, 51254, 51258, 51266, 51276, 51279, 51286)
- small improvements (ALT 51219, 51200, 51213, 51232, 51263, 51291)

* Wed Aug 14 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt4
- update documentation PVE

* Thu Aug 01 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- update documentation PVE
- fix some typos

* Thu May 02 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- fix some typos (ALT 50208, 50199, 50157, 50155, 50154)
- small improvements (ALT 50153, 50152, 50215, 50156)

* Thu Apr 18 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Server V 10.2

* Tue Sep 12 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt8
- fix some typos (ALT 47501, 47502)
- small improvements

* Fri Aug 25 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt7
- update documentation PVE
- fix some typos

* Fri Jul 14 2023 Artem Zolochevskiy <azol@altlinux.org> 10.1-alt6
- fix typo (Closes 45284)

* Thu Jan 26 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update documentation PVE
- fixed PVE (ALT 45021, 45023, 45024, 45025, 45027, 45028)
- fix some typos (ALT 45045, 45034, 45022, 45020, 45026)

* Mon Dec 26 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- update to ALT Server V 10.1
- update documentation PVE (ALT 44318)
- fix opennebula (ALT 44264, 44282, 44283, 44319, 44320)

* Mon Oct 24 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update documentation

* Fri Jul 29 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix some typos (ALT 43353, 43354, 43310, 43352, 43382, 43383, 43385, 43391, 43392)

* Fri Jul 15 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Server V 10.1rc

* Tue Dec 28 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Server V 10.0beta
- reduce package size

* Mon Aug 02 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Server V 9.2

* Mon Nov 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- fix to create bootable flash disk
- fix some typos (ALT #38985)

* Wed Sep 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update to latest public distr
- fix some typos

* Mon Sep 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr

* Mon Dec 16 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- fix screen

* Thu Dec 05 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- initial build
