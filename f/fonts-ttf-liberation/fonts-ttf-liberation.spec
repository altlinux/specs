%define priority 60
%define fontname liberation
%define fontconf %{priority}-%{fontname}
%define oldname liberation-fonts

Name: fonts-ttf-%fontname
Version: 2.1.5
Release: alt1

Summary: Fonts to replace commonly used Microsoft Windows Fonts

License: SIL Open Font License Version 1.1
Group: System/Fonts/True type
Url: https://github.com/liberationfonts/liberation-fonts

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/liberationfonts/liberation-fonts/archive/%version.tar.gz
Source: %name-%version.tar
Source2:          %{oldname}-mono.conf
Source3:          %{oldname}-sans.conf
Source4:          %{oldname}-serif.conf

BuildArch: noarch

Provides: fonts-ttf-core

# TODO: split into subpackages
Provides: fonts-ttf-liberation-mono = %version
Provides: fonts-ttf-liberation-sans = %version
Provides: fonts-ttf-liberation-serif = %version

# Additional font which used to be in this package (until 2.00.1-alt1); useful
# as a replacement for the popular Arial Narrow (found in many official forms).
Requires: %name-narrow

# To satisfy requirements of official Google Chrome RPM package
Provides: liberation-fonts

BuildRequires: rpm-build-fonts
BuildRequires: python3-module-fonttools fontforge fontpackages-devel

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup

%build

# Fedora fix for https://bugzilla.redhat.com/show_bug.cgi?id=1526510
sed -i 's/OS2_UseTypoMetrics: 1/OS2_UseTypoMetrics: 0/g' src/*.sfd

%make_build
mv liberation-fonts-ttf-%version/*.ttf ./

%install
%ttf_fonts_install %fontname

mkdir -p %{buildroot}%{_fontconfig_templatedir}/ %{buildroot}%{_fontconfig_confdir}/
# Repeat for every font family
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf

for fconf in %{fontconf}-mono.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-serif.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%files -f %fontname.files
%doc LICENSE README.md AUTHORS ChangeLog
%{_fontconfig_templatedir}/*-%{fontname}-*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-*.conf

%changelog
* Thu Apr 14 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- new version 2.1.5 (with rpmrb script) (ALT bug 42447)

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 2.00.4-alt3
- NMU: removed rpm-macros-fontpackages, use new rpm-macros-fonts

* Tue Nov 19 2019 Ivan Zakharyaschev <imz@altlinux.org> 2.00.4-alt2
- Made additional useful part of this font set (Liberation Narrow) be installed
  together with this package always, to make users happier. (By a Requires.
  It used to be part of this package until 2.00.1-alt1, but was separated into
  another package due to license, see https://lwn.net/Articles/502371/ ).
  This addition is a replacement for the Arial Narrow font, which is popular
  in official documents and helps LibreOffice render them nicer.

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 2.00.4-alt1
- new version 2.00.4 (with rpmrb script)

* Thu Oct 18 2018 Vladimir Didenko <cow@altlinux.ru> 2.00.3-alt2
- add provides to satisfy requirements of official Google Chrome RPM

* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.00.3-alt1
- new version 2.00.3 (with rpmrb script)
- build from source sfd with fontforge

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 2.00.1-alt2
- lowered priority to 60 (see ALT#30669 for details)

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.00.1-alt1
- new version (closes: #30161)
- new license
- old license liberation-narrow moved to separate package

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.06.0.20100721-alt1
- build new upstream release

* Wed Dec 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt2
- add fonts-ttf-core provides (ALT bug #22589)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt1
- new version 1.0.4
- removed License.txt as already included in sources

* Wed May 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt1
- new version (fix altbug #15355)
- update to Caius Chance <cchance@redhat.com> version of the project
  + Resolves: rhbz#251890 (Exchanged and incomplete glyphs.)
  + Resolves: rhbz#240525 (Alignment mismatch of dot accents.)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
