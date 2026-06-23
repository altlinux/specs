%define variant alt-education
%define Variant ALT Education

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

Name: docs-%variant
Version: 11.2
Release: alt1

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
%_documentationdir	%_docsinstalldir	53
EOF

%files
%_docsinstalldir
%_altdir/%name

%changelog
* Tue Jun 23 2026 Elena Mishina <lepata@altlinux.org> 11.2-alt1
- update to ALT Education 11.2BETA
- fix typo (closes #58453)
- veyon: add integration with FreeIPA (closes #48453)

* Mon Mar 30 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt5
- desktop-software: add surguch, delete alt-csp-cryptopro
- fix some typos (closes #58432, #58435, #58430)
- small improvements

* Fri Mar 20 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt4
- update to ALT Education 11.1RC2
- fix error mediawiki (closes #57849)

* Thu Feb 05 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt3
- fix some typos
- update screen

* Mon Feb 02 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt2
- update to ALT Education 11.1RC1
- educational-resources: add jitsi-meet
- the spec file has been rewritten to support alternatives

* Wed Nov 19 2025 Elena Mishina <lepata@altlinux.org> 11.1-alt1
- update to ALT Education 11.1Beta

* Wed Jun 25 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- update install-distro screen
- fix some typos (closes: #54896, #54931)
- small improvements (closes: #54900, #54905, #54928)

* Sat Jun 21 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- update to ALT Education 11.0rc

* Wed Feb 26 2025 Elena Mishina <lepata@altlinux.org> 10.4-alt4
- fix some typos (closes: #53085)

* Thu Feb 13 2025 Elena Mishina <lepata@altlinux.org> 10.4-alt3
- update mediawiki, moodle (closes: #53008, #53009)
- small improvements

* Mon Jan 27 2025 Elena Mishina <lepata@altlinux.org> 10.4-alt2
- update to latest public distr
- educational-resources: add mediawiki; update moodle, nextcloud

* Fri Oct 25 2024 Elena Mishina <lepata@altlinux.org> 10.4-alt1
- update to ALT Education 10.4
- fix some typos (closes: #50840, #50847)

* Tue Jun 18 2024 Elena Mishina <lepata@altlinux.org> 10.3-alt1
- update to ALT Education 10.3

* Thu Apr 18 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt5
- small improvements
- fix some typos (closes: 48145)
- fix name partition (closes: 48207)
- update screen

* Thu Oct 12 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt4
- update educational-resources: nextcloud, veyon, moodle (closes: 47958)
- fix typo

* Wed Oct 04 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- update support
- update screen

* Sun Oct 01 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- update recoll

* Fri Sep 22 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Education 10.2

* Mon Nov 07 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Education 10.1

* Tue Sep 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- update to ALT Education 10.1rc

* Fri May 06 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Education 10.1Beta

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt4
- update documentation
- add geany, idle3

* Wed Dec 08 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- update to ALT Education 10.0

* Mon Nov 15 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Education 10.0rc
- reduce package size

* Wed Oct 13 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Education 10.0Beta

* Wed Apr 28 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt2
- update to latest public distr
- add alterator-update-kernel, synfigstudio

* Thu Apr 15 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Education 9.2Beta
- educational-resources: add veyon, trik-studio
- system-management: add group-policy, network configuration
- install-packages-advanced: add epm

* Thu Oct 15 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update thunderbird
- added recoll settings

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Education 9.1

* Tue Jun 30 2020 Elena Mishina <lepata@altlinux.org>9.0-alt3
Beta version of ALT Education 9.1
- added jitsi-meet
- added grub-customizer

* Mon Oct 21 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- added recoll
- fix typo

* Tue Oct 15 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Education 9.0

* Wed Jul 31 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
Beta version of ALT Education 9.0

* Tue Jun 25 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
Alpha version of ALT Education 9.0

* Wed Feb 13 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt5
- added moodle, mediawiki, owncloud, rujel
- added install fonts (closes: 35820)

* Tue Jan 15 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- added kde
- added boot option

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Dec 4 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to 8.2

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update documentation

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Fri Oct 28 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt1
- updated to 8.1
- added 'guest session' description

* Sun Aug 07 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt2
- removed obsolete stuff

* Thu Aug 04 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt1
- initial build for Sisyphus
