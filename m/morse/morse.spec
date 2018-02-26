Name: morse
Summary: Morse Classic morse trainer program
Version: 2.4
Release: alt1
License: BSD
Group: Communications
Url: http://catb.org/~esr/morse/
Source0: %name-%version.tar.gz
Patch: morse2.4-nosound.patch

%define Backends X11 OSS Linux PA ALSA

PreReq: alternatives

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
sed -i '/\$(X11LIBS)/s/\(\$(X11LIBS) \)\(.*\)/\2 \1/g' morse.d/Makefile
%patch

%build
rm -f morse.1
make DEVICE=ALSA QSO morse.1
for DEVICE in %Backends; do
rm -f morse.d/morse
make -C morse.d DEVICE=$DEVICE morse
done

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -s morse.d/%name[^.]* %buildroot%_bindir/
install -s QSO %buildroot%_bindir/
install %name.1 %buildroot%_man1dir/
mkdir -p %buildroot/%_altdir
N=10
for B in %Backends; do
echo "%_bindir/%name	%_bindir/%{name}$B	$N" > %buildroot/%_altdir/%{name}$B
N=$((N+10))
done

%files
%doc README HISTORY

%_man1dir/%name.1*
%_bindir/%{name}*
%_bindir/QSO
%_altdir/%{name}*

%changelog
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

