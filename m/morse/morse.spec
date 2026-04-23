Name: morse
Summary: Morse Classic morse trainer program
Version: 2.7
Release: alt2
License: BSD
Group: Communications
Url: http://catb.org/~esr/morse/
Vcs: https://gitlab.com/esr/morse-classic.git
Source0: %name-%version.tar
Patch1: 01-morsexml.patch
Patch2: 02-makefile.patch
Patch3: 03-fix-pa_simple_write-with-mono-output.patch
Patch4: 04-gcc-14.patch
Patch5: 05-fix_-X_handling.patch

%define Backends X11 OSS Linux PA ALSA

# Automatically added by buildreq on Tue Jun 28 2011
# optimized out: alternatives docbook-dtds docbook-style-xsl libgpg-error pkg-config xml-common xml-utils xorg-xproto-devel xsltproc
BuildRequires: libX11-devel libalsa-devel libpulseaudio-devel xmlto

BuildRequires: xsltproc docbook-dtds docbook-style-xsl

%description
Morse Classic is a Morse-code training program for aspiring radio hams.  It
can generate random tests or simulated QSOs resembling those used in
the ARRL test (a QSO generator is included).  There are a plethora of
options to vary the training method.  In one of the simpler modes,
this program will take text from standard input and render it as
Morse-code beeps.

%prep
%setup
%autopatch -p1
sed -i -e 's!-Wno-unused-parameter!-Wno-unused-parameter -Wno-error=old-style-definition -std=gnu17!' */Makefile

%build
rm -f morse.1
make DEVICE=ALSA QSO morse.1
for DEVICE in %Backends; do
make -C morse.d DEVICE=$DEVICE morse
done

%install
install -D QSO %buildroot%_bindir/QSO
install morse.d/%name[^.]* %buildroot%_bindir/
ln -s morseALSA %buildroot%_bindir/morse
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc README HISTORY

%_man1dir/%name.1*
%_bindir/%{name}*
%_bindir/QSO

%changelog
* Thu Apr 23 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.7-alt2
- fix FTBFS with gcc15

* Tue Mar 17 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.7-alt1
- 2.7

* Tue Jul 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 2.6-alt1
- 2.6

* Fri Nov 13 2020 Fr. Br. George <george@altlinux.ru> 2.5-alt2
- Drop alternatives (Closes: #39257)

* Sun Dec 16 2012 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5

* Tue Jun 28 2011 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4
- Various backends provided

* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Initial build for ALT
- Getopt bug fixed (X instead of X:)
- Nosound patch applied (for text conversion)

* Tue Jan 25 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.1-1
- Patched to use termios(3) rather than ioctls() and sigaction rather
  than sigset(3).  This should allow it to run under Mac OS X.

* Mon Jan 24 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.0-1
- Initial build.  See HISTORY file in the distribution for prior history.

