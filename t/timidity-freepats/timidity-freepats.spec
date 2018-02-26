%define origname freepats

Name: timidity-%origname
Version: 20060219
Release: alt2

Summary: A set of sound fonts for use in audio synths
License: GPLv2+
Group: Sound

Url: http://freepats.zenvoid.org
Source: %url/%origname-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define timidir %_datadir/timidity
%define patchdir %timidir/%origname

%description
FreePats is a set of sound fonts for use in audio synths.

FreePats project is to create a free and open set of GUS compatible
patches that can be used with softsynths such as TiMidity and WildMidi.

%prep
%setup -n %origname

%build

%install
mkdir -p %buildroot%patchdir
mv Drum_* Tone_* %buildroot%patchdir

cat - freepats.cfg > %buildroot%timidir/freepats.cfg << _EOF_
dir %patchdir

_EOF_

%files
%doc COPYING README
%timidir/freepats.cfg
%patchdir

# TODO:
# - consider Gentoo/Arch-like automated timidity config treating

%changelog
* Sun Apr 17 2011 Michael Shigorin <mike@altlinux.org> 20060219-alt2
- fixed silly thinko spotted by shadowsbrother/gmail.com

* Sat Apr 16 2011 Michael Shigorin <mike@altlinux.org> 20060219-alt1
- initial build for ALT Linux Sisyphus (closes: #25449)
  + based on Gentoo, Debian, MeeGo packages to some extent
