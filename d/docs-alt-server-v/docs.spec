%define variant alt-server-v
%define Variant ALT Server V

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.1
Release: alt5

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
