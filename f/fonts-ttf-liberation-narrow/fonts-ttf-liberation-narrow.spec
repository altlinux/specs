%global priority 60
%global fontname liberation-narrow
%global fontconf %priority-%fontname.conf

Name: fonts-ttf-%fontname
Version: 1.07.6
Release: alt1

# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License: Liberation
Summary: Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Group: System/Fonts/True type
URL: http://github.com/liberationfonts/liberation-sans-narrow
VCS: http://github.com/liberationfonts/liberation-sans-narrow

Source0: %name-%version.tar
Source1: liberation-fonts-narrow.conf
Source2: import.info

BuildArch: noarch

BuildRequires(pre): rpm-macros-fonts
BuildRequires: rpm-build-fonts
BuildRequires: fontpackages-devel >= 1.13
BuildRequires: xorg-x11-font-utils
BuildRequires: fontforge

Conflicts: fonts-ttf-liberation < 1.07

%description
The Liberation Fonts are intended to be replacements
for the three most commonly used fonts on Microsoft systems:
Times New Roman, Arial, and Courier New.

This is Sans-Serif Narrow TrueType fonts
that replaced commonly used Microsoft Arial Narrow.

%prep
%setup

%build
%make_build

%install
pushd %fontname-fonts-ttf-%version
%ttf_fonts_install %fontname
popd

install -pD -m644 %SOURCE1 %buildroot%_fontconfig_templatedir/%fontconf

install -d %buildroot%_fontconfig_confdir
ln -s {%_fontconfig_templatedir,%buildroot%_fontconfig_confdir}/%fontconf

%files -f %fontname-fonts-ttf-%version/%fontname.files
%doc License.txt COPYING README.rst AUTHORS ChangeLog
%_fontconfig_templatedir/*-%fontname.conf
%config(noreplace) %_fontconfig_confdir/*-%fontname.conf

%changelog
* Wed Nov 18 2026 Valery Zabrovsky <brow@altlinux.org> 1.07.6-alt1
- New version 1.07.6 (closes: 37508).
- Switch to build from Gear tags.
- Remove font files duplicated by fonts-ttf-liberation.

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.07.4-alt2
- lowered priority to 60 (closes: #30669)

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.07.4-alt1
- as of 2.00 liberation-narrow is not included in liberation fonts 
  due to license incompatibilities. Use release 1.07.4

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
