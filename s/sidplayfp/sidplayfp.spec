Name: sidplayfp
Version: 1.4.3
Release: alt1
Summary: SID chip music module player
Group: Sound
License: GPLv2+
Url: http://sourceforge.net/projects/sidplay-residfp/
Source: http://downloads.sourceforge.net/sidplay-residfp/%name-%version.tar.gz
Source44: %name.watch

BuildRequires: libsidplayfp-devel >= 1.0
# Automatically added by buildreq on Fri Oct 13 2017
# optimized out: glibc-kernheaders-x86 gnu-config libgpg-error libstdc++-devel pkg-config python-base python-modules
BuildRequires: gcc-c++ glibc-kernheaders-generic libalsa-devel libpulseaudio-devel libsidplayfp-devel

%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README TODO
%_bindir/sidplayfp
%_bindir/stilview
%_mandir/man?/sidplayfp.*
%_man1dir/stilview.1*

%changelog
* Fri Oct 13 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.4.3-alt1
- initial build for ALT Linux Sisyphus
