%define variant alt-workstation
%define Variant ALT Workstation

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

Name: docs-%variant
Version: 11.2
Release: alt2

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-macros-alternatives
BuildRequires(pre): rpm-build-licenses
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
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

# Set alternative to doc
mkdir -p -- %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_documentationdir	%_docsinstalldir	56
EOF

%files
%_docsinstalldir
%_altdir/%name

%changelog
* Tue May 05 2026 Elena Mishina <lepata@altlinux.org> 11.2-alt2
- update to ALT Workstation 11.2BETA3

* Thu Feb 19 2026 Elena Mishina <lepata@altlinux.org> 11.2-alt1
- update to ALT Workstation 11.2BETA
- minor improvements (ALT #56831)
- the spec file has been rewritten to support alternatives

* Thu Nov 06 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt5
- update surguch, kopidel
- minor improvements (ALT #56432)

* Wed Oct 08 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt4
- add etcnet
- update loupe, foldy, surguch
- minor improvements (ALT #56263, #56277)

* Tue Sep 02 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt3
- add GSConnect, Session Keeper, VPN GOST
- fix some typos (ALT #55556)

* Wed Aug 06 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt2
- update to ALT Workstation 11.1RC1
- add gearlever, alien, gnome-boxes
- fix some typos (ALT #55253, #53717)

* Mon Jul 07 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt1
- update to ALT Workstation 11.1BETA
- add tuner, hardinfo2, hashsum, userpasswd

* Mon Jun 09 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt5
- fix some typos (ALT #54479)
- add luks2, VPN/Wi-Fi settings

* Sun Apr 20 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt4
- update to ALT Workstation 11.0RC3

* Tue Apr 15 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt3
- update to ALT Workstation 11.0RC2
- add gtkhash, foldy
- whatis-alt: updated text about platform p11 (thx Anton Abramov)

* Sun Mar 30 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- fix some typos
- add remote-desktop
- update gnome-desktop

* Fri Mar 21 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- update to ALT Workstation 11.0RC
- add alterator-kopidel, surguch
- delete synaptic

* Mon Oct 21 2024 Elena Mishina <lepata@altlinux.org> 10.4-alt1
- add alterator-usbguard, alterator-usbmount
- update to ALT Workstation 10.4

* Tue Feb 27 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- update to ALT Workstation 10.2
- fix some typos

* Tue Feb 20 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- fix some typos (ALT #49343, #49390, #49388, #49273)
- update Timeshift (ALT #49364, #49360)
- update install-distro (ALT #49272, #49338, #49408, #49411)
- update group policy (ALT #49330, #49332, #49341)

* Tue Jan 23 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Workstation 10.2rc

* Wed Dec 21 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt8
- update to latest public distr of ALT Workstation 10.1

* Sun Dec 18 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt7
- fix some typos (ALT #44664, #44665)

* Fri Dec 02 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt6
- update documentation

* Fri Oct 28 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update to ALT Workstation 10.1

* Mon Oct 24 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- fix some typos (ALT #43731)
- update documentation

* Mon Sep 05 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Workstation 10.1rc

* Wed Aug 03 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix some typos (ALT 43358, 43369, 43398, 43400, 43394)
- update documentation

* Wed Jul 20 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to beta version of ALT Workstation 10.1

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt4
- fix some typos
- update documentation

* Tue Dec 07 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- update to ALT Workstation 10.0

* Tue Nov 30 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Workstation 10.0rc
- reduce package size

* Tue Nov 09 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to beta version of ALT Workstation 10.0

* Wed Jul 07 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Workstation 9.2

* Tue Apr 06 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt4
- fix some typos
- update screenshots
- update info: network-configuration

* Mon Mar 15 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- system-management: add group policy
- functional: add alt-csp-cryptopro, luks password
- install-packages-advanced: add epm
- fix typo

* Mon Nov 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update thunderbird
- add recoll settings
- add ALT Media Writer

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Workstation 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Workstation 9.0

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
- update to beta verson of ALT Workstation 9.0
- fix pam_mount options (ALT #37031)

* Mon Jul 01 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to alpha verson of ALT Workstation 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Nov 27 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- fix typo
- update doc

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update doc

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 8.1-alt1
- update for 8.1 release

* Tue Jun 21 2016 Michael Shigorin <mike@altlinux.org> 8.0-alt3
- renamed to docs-alt-workstation

* Tue Apr 19 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update to alpha verson (18/04/2016)

* Mon Apr 4 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
