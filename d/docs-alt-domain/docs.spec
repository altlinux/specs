%define variant alt-domain
%define Variant ALT Domain

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v docs-alt-domain docs-alt-virtualization-one docs-alt-virtualization-pve docs-alt-mobile docs-alt-platform

Name: docs-%variant
Version: 11.0
Release: alt3

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
* Thu Nov 27 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt3
- fix dhcp script (closes #56174)
- fix sssd settings (closes #56177)
- update: ADMC
- add: gMSA, usershares, troubleshooting

* Fri Sep 26 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- fix typos (closes #56055, #56054, #56053, #56052, #56051, #56162, #56179)
- small improvements (closes #56164, #56165, #56166, #56167, #56176)
- fix command samba-tool (#56163, #56170, #56171, #56172 #56175)

* Fri Aug 22 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- initial build for Sisyphus
