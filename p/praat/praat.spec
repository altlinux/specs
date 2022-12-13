Name: praat
Version: 6.3.02
Release: alt1

Summary: A program for speech analysis and synthesis
License: GPLv2
Group: Sound

Url: http://www.praat.org

# https://github.com/praat/praat.git
Source: %name-%version.tar.gz
Patch0: %name-6.0.46-gcc8-fix.patch

# PATCH-FIX-OPENSUSE praat-use_system_libs.patch -- replace some embedded libs with system ones
Patch1:         praat-use_system_libs.patch
# PATCH-FIX-OPENSUSE praat-no-return-in-nonvoid.patch -- make the compiler happy
Patch2:         praat-no-return-in-nonvoid.patch
# PATCH-FEATURE-OPENSUSE praat-allow-system-flags.patch badshah400@gmail.com -- Allow compilation and linker flags to incorporate appropriate env flags
Patch3:         praat-allow-system-flags.patch


Requires: fonts-bitmap-75dpi

# Automatically added by buildreq on Mon Aug 24 2020
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libstdc++-devel pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: gcc-c++ libalsa-devel libgtk+2-devel libjack-devel libpulseaudio-devel libstdc++-devel-static libglpk-devel libopus-devel libopusfile-devel  libopusurl-devel

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)


%description
According to its authors, praat is "doing phonetics by computer".
Through its graphical interface, several speech analysis functionalities
are available: spectrograms, cochleograms, and pitch and formant
extraction.  Articulatory synthesis, as well as synthesis from pitch,
formant, and intensity are also available.  Other features are
segmentation, labelling using the phonetic alphabet, and computation
of statistics.  Praat is configurable and extensible through its own
scripting language and has provisions for communicating with other
programs.

* Make sure you have read the Intro from Praat's Help menu.
* If that does not help, use the Search button in Praat's manual window.
* Or consult the Frequently Asked Questions on the website.

Recommends: fonts-bitmap-100dpi fonts-bitmap-75dpi

%prep
%setup
#patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch5 -p1

%build
cp -a makefiles/makefile.defs.linux.pulse makefile.defs


sed -e '/^CFLAGS/s/$/\ %{optflags}/' \
    -e '/^CXXFLAGS/s/$/\ %{optflags}/' \
    -e '/^CC/s/?=/=/' -e '/^CXX/s/?=/=/' \
    -e '/^LINK/s/?=/=/' -i makefile.defs

#    -e '/^CC/s/=/?=/' -e '/^CXX/s/=/?=/' \
#    -e '/^LINK/s/=/?=/' -i makefile.defs



%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%_bindir/*

# TODO:
# - FLAC/ and audio/ are patched
# - GSL/ *seems* just bundled?
# - watch file:
# version=3
#opts="uversionmangle=s/\.0?(\d+)/\.$1/g" \
#  http://www.fon.hum.uva.nl/praat/download_sources.html praat(\d)(\d)(\d+)_sources.tar.gz debian

%changelog
* Tue Dec 13 2022 Ilya Mashkin <oddity@altlinux.ru> 6.3.02-alt1
- 6.3.02

* Wed Sep 07 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.22-alt1
- 6.2.22 (6.2.18 released as 6.2.22)

* Tue Aug 23 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.16-alt1
- 6.2.16

* Sat May 28 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.14-alt1
- 6.2.14

* Sun Apr 24 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.12-alt1
- 6.2.12

* Sat Apr 09 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.11-alt1
- 6.2.11

* Sat Feb 19 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.09-alt1
- 6.2.09

* Tue Feb 01 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.07-alt1
- 6.2.07

* Sun Jan 16 2022 Ilya Mashkin <oddity@altlinux.ru> 6.2.05-alt1
- 6.2.05

* Fri Nov 19 2021 Ilya Mashkin <oddity@altlinux.ru> 6.2.01-alt1
- 6.2.01

* Sat Oct 16 2021 Ilya Mashkin <oddity@altlinux.ru> 6.1.54-alt1
- 6.1.54

* Thu Oct 14 2021 Ilya Mashkin <oddity@altlinux.ru> 6.1.48-alt1
- 6.1.48
- add more regs
- fix build with gcc11 etc.

* Mon Aug 24 2020 Fr. Br. George <george@altlinux.ru> 6.1.16-alt1
- Autobuild version bump to 6.1.16

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 6.1.08-alt1
- Autobuild version bump to 6.1.08

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 6.1.05-alt1
- Autobuild version bump to 6.1.05

* Wed Feb 13 2019 Pavel Moseev <mars@altlinux.org> 6.0.46-alt2
- no return statement in the non-void function fixed (according g++8)

* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 6.0.46-alt1
- Autobuild version bump to 6.0.46

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.36-alt1
- Updated to upstream version 6.0.36.

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.13-alt1.1
- Fixed build

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 5.3.13-alt1
- 5.3.13

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 5.2.44-alt1
- 5.2.44
- buildreq

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 5.2.11-alt1
- 5.2.11 (thanks force@)
- buildreq

* Wed Dec 08 2010 Michael Shigorin <mike@altlinux.org> 5.2.05-alt1
- 5.2.05

* Wed Dec 08 2010 Michael Shigorin <mike@altlinux.org> 5.1.25-alt2
- fixated font dependency as it's in need indeed
  (thanks Renata Pojidaeva)

* Sun Feb 21 2010 Michael Shigorin <mike@altlinux.org> 5.1.25-alt1
- 5.1.25
  + Many problems can be solved by upgrading to version 5.1.25 of Praat.

* Sun Sep 20 2009 Michael Shigorin <mike@altlinux.org> 5.1.16-alt1
- built for ALT Linux (closes: #19876)
