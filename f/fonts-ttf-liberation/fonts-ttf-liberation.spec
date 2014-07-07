%define priority  59
%define fontname liberation
%define fontconf %{priority}-%{fontname}
%define oldname liberation-fonts

Name: fonts-ttf-%fontname
Version: 2.00.1
Release: alt1

Summary: Fonts to replace commonly used Microsoft Windows Fonts

License: SIL Open Font License Version 1.1
Group: System/Fonts/True type
Url: http://fedorahosted.org/liberation-fonts/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://fedorahosted.org/releases/l/i/%oldname/%oldname-ttf-%version.tar
Source2:          %{oldname}-mono.conf
Source3:          %{oldname}-sans.conf
Source4:          %{oldname}-serif.conf

BuildArch: noarch

Provides: fonts-ttf-core

# TODO: split into subpackages
Provides: fonts-ttf-liberation-mono = %version
Provides: fonts-ttf-liberation-sans = %version
Provides: fonts-ttf-liberation-serif = %version

BuildRequires: rpm-build-fonts rpm-macros-fontpackages

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -n %oldname-ttf-%version

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
%doc LICENSE README AUTHORS ChangeLog
%{_fontconfig_templatedir}/*-%{fontname}-*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-*.conf

%changelog
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
