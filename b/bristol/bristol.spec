
Name: bristol
Version: 0.60.11
Release: alt3
Summary: Synthesizer emulator
Group: Sound
License: GPLv2+
Url: http://bristol.sourceforge.net
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name.desktop
Patch: bristol-0.60.9-CVE-2010-3351.patch
Patch1: bristol-0.60.11-alt-build-without-alsa-iatomic.patch

BuildRequires: libXext-devel libpulseaudio-devel pkgconfig(liblo) xorg-xproto-devel
BuildRequires: libX11-devel libalsa-devel jackit-devel desktop-file-utils
Source44: import.info

%description
Bristol is an emulation package for a number of different 'classic'
synthesizers including additive and subtractive and a few organs.
The application consists of the engine, which is called bristol,
and its own GUI library called brighton that represents all the emulations.

%package devel
Summary: %summary
Group: Sound
Requires: %name = %version

%description devel
This package contains the development libraries for Bristol.

%prep
%setup

%patch0 -p0 -b .libpath
%patch1 -p2

find . -type f | xargs chmod -x
chmod +x config* *sh depcomp


# Only x86_64 is optimised for SSE, non x86 platforms don't have SSE
%ifnarch x86_64
sed -i 's/-msse -mfpmath=sse //g' bristol/Makefile.am
sed -i 's/-msse -mfpmath=sse //g' bristol/Makefile.in
%endif

%build
%configure --enable-static=no --disable-version-check
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std INSTALL='install -p'
rm -f %buildroot%_libdir/*.la
rm INSTALL
mkdir -p -m 0755 %buildroot%_pixmapsdir
mkdir -p -m 0755 %buildroot%_desktopdir
install -p -m 0644 bitmaps/bicon.svg %buildroot%_pixmapsdir/bristol.svg
desktop-file-install \
    --mode 0644 \
    --dir %buildroot%_desktopdir/ \
    %SOURCE1

%files
%doc AUTHORS ChangeLog COPYING* NEWS README
%_bindir/*
%_datadir/bristol
%_pixmapsdir/*
%_desktopdir/bristol.desktop
%_libdir/lib*.so.*
%_man1dir/*

%files devel
%_libdir/lib*.so

%changelog
* Sun Jan 13 2019 Ivan A. Melnikov <iv@altlinux.org> 0.60.11-alt3
- fix build with recent alsa
- minor spec cleanup

* Sat Mar 07 2015 Ilya Mashkin <oddity@altlinux.ru> 0.60.11-alt2
- Build for Sisyphus

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_2
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_1
- initial fc import

