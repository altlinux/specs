%define fname liberation
%define oname liberation-fonts-ttf

Name: fonts-ttf-%fname
Version: 1.06.0.20100721
Release: alt1

Summary: Fonts to replace commonly used Microsoft Windows Fonts

# The license of the Liberation Fonts is a EULA that contains
# GPLv2 and two exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like
# the one in GPLv3. This license is Free, but GPLv2 and GPLv3
# incompatible.
License: Liberation
Group: System/Fonts/True type
Url: http://fedorahosted.org/liberation-fonts/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://fedorahosted.org/releases/l/i/%oname/%oname-%version.tar

BuildArch: noarch

Provides: fonts-ttf-core

BuildRequires: rpm-build-fonts

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -n %oname-%version

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc License.txt README AUTHORS ChangeLog

%changelog
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
