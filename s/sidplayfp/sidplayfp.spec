Name: sidplayfp
Version: 2.2.1
Release: alt1
Summary: SID chip music module player
Group: Sound
License: GPLv2+
Url: http://sourceforge.net/projects/sidplay-residfp/
Source: http://downloads.sourceforge.net/sidplay-residfp/%name-%version.tar.gz
Source44: %name.watch
Patch0: %name-g++8.patch

BuildRequires: libsidplayfp-devel >= 2.2.0
# Automatically added by buildreq on Fri Oct 13 2017
# optimized out: glibc-kernheaders-x86 gnu-config libgpg-error libstdc++-devel pkg-config python-base python-modules
BuildRequires: gcc-c++ glibc-kernheaders-generic libalsa-devel libpulseaudio-devel libsidplayfp-devel

%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.

%prep
%setup
# #%patch0 -p2

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
* Tue Aug 31 2021 Motsyo Gennadi <drool@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Fri Feb 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- no return statement in the non-void function fixed (according g++8)

* Fri Oct 13 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.4.3-alt1
- initial build for ALT Linux Sisyphus
