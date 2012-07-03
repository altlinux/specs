%global vernumber 086

Name: bsnes
Version: 0.%vernumber
Release: alt1
Summary: SNES emulator focused on accuracy

License: GPLv3
Group: Emulators
Url: http://byuu.org/bsnes/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://bsnes.googlecode.com/files/%{name}_v%vernumber-source.tar.bz2
Source2: README.bsnes
Patch1: bsnes-0.086-systemwide.patch

#bsnes does not use system snes_ntsc because the modified video processing
#filter algorithm calls back into bsnes specific c++ colortable code, that
#isn't available when the library is built stand alone
BuildRequires: desktop-file-utils
BuildRequires: libalut-devel
BuildRequires: libgtk+2-devel
BuildRequires: libao-devel
BuildRequires: libXv-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libSDL-devel gcc-c++ libalsa-devel

%description
bsnes is an emulator that began development on 2004-10-14. The purpose of the
emulator is a bit different from other emulators: it focuses on accuracy,
debugging functionality, and clean code.
The emulator does not focus on things that would hinder accuracy. This
includes speed and game-specific hacks for compatibility. As a result, the
minimum system requirements for bsnes are quite high.

%prep
%setup -n %{name}_v%vernumber-source
%patch1 -p1 -b .systemwide

#fix permissions
find . -type f -not -name \*.sh -exec chmod 644 {} \;

#use system optflags
sed -i "s/-O3/$RPM_OPT_FLAGS/" bsnes/Makefile
sed -i "s/-O3/$RPM_OPT_FLAGS -fPIC/" snesfilter/Makefile
sed -i "s/-O3/$RPM_OPT_FLAGS/" snespurify/cc-gtk.sh

#don't strip the binaries prematurely
sed -i "s/link += -s/link +=/" bsnes/Makefile
sed -i "s/link    := -s/link    :=/" snesfilter/Makefile
sed -i "s/-s //" snespurify/cc-gtk.sh

#use the proper compiler and moc commands
sed -i "s/g++-4.5/g++/" snespurify/cc-gtk.sh

#install fedora-specific readme
install -pm 644 %SOURCE2 README.bsnes

#use proper system-wide path for filters
sed -i 's@/usr/lib@%_libdir@' bsnes/ui/general/main-window.cpp

%build
#prepare for building compatibity and accuracy profile, as well as the debugger
cp -pR bsnes bsnes-accuracy
cp -pR bsnes laevateinn

pushd bsnes
make %{?_smp_mflags} compiler=gcc profile=compatibility phoenix=gtk
popd
pushd bsnes-accuracy
make %{?_smp_mflags} compiler=gcc profile=accuracy phoenix=gtk
popd
pushd laevateinn
make %{?_smp_mflags} compiler=gcc ui=ui-debugger phoenix=gtk
popd
pushd snesfilter
make %{?_smp_mflags} compiler=gcc
popd
pushd snespurify
./cc-gtk.sh
popd

%install
pushd bsnes
sed -i 's/Name=bsnes/Name=bsnes (Compatibility profile)/' data/bsnes.desktop
make install DESTDIR=$RPM_BUILD_ROOT prefix=%prefix
desktop-file-install --vendor=altlinux \
        --delete-original --dir $RPM_BUILD_ROOT%_datadir/applications \
        $RPM_BUILD_ROOT%_datadir/applications/bsnes.desktop
popd
pushd bsnes-accuracy
sed -i 's/Name=bsnes/Name=bsnes (Accuracy profile)/' data/bsnes.desktop
sed -i 's/Exec=bsnes/Exec=bsnes-accuracy/' data/bsnes.desktop
install -pm 755 out/bsnes $RPM_BUILD_ROOT%_bindir/bsnes-accuracy
desktop-file-install --dir $RPM_BUILD_ROOT%_datadir/applications \
         data/bsnes.desktop
popd
pushd laevateinn
install -pm 755 out/laevateinn $RPM_BUILD_ROOT%_bindir
popd
install -d $RPM_BUILD_ROOT%_datadir/%name
install -pm 644 bsnes/data/cheats.xml $RPM_BUILD_ROOT%_datadir/%name
install -d $RPM_BUILD_ROOT%_libdir/%name/filters
install -pm 755 snesfilter/out/*.filter $RPM_BUILD_ROOT%_libdir/%name/filters
install -pm 755 snespurify/snespurify-gtk $RPM_BUILD_ROOT%_bindir
install -d $RPM_BUILD_ROOT%_datadir/%name/shaders
install -pm 644 snesshader/*.shader $RPM_BUILD_ROOT%_datadir/%name/shaders

%files
%doc README.bsnes
%_bindir/bsnes
%_bindir/bsnes-accuracy
%_bindir/laevateinn
%_bindir/snespurify-gtk
%_libdir/bsnes
%_datadir/bsnes
%_datadir/pixmaps/bsnes.png
%_datadir/applications/bsnes.desktop
%_datadir/applications/altlinux-bsnes.desktop

%changelog
* Thu May 31 2012 Ilya Mashkin <oddity@altlinux.ru> 0.086-alt1
- Build for Sisyphus

* Tue Feb 14 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.086-1
- Updated to 0.086
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Updated the systemlibs patch
- Build Compatibility and Accuracy profiles, as well as the laevateinn debugger

* Tue Jan 03 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.085-1
- Updated to 0.085
- Updated the systemwide patch
- cheats.bml cheats.xml

* Wed Nov 09 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.084-1
- Updated to 0.084
- License is now GPLv3
- Updated the systemwide patch
- cheats.xml cheats.bml
- Apply the change enabling system-wide cheats as a patch

* Tue Aug 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.082-1
- Updated to 0.082
- Dropped unneeded patches

* Sun Jul 03 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.080-1
- Updated to 0.080
- Updated the gcc-4.6 patch

* Tue Jun 21 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.079-1
- Updated to 0.079
- Dropped subpackages, they are too small to be worth it
- Updated the Fedora readme
- Added gcc-4.6 and systemwide patches by Themaister
- Try to handle system-wide cheats, filters and shaders properly
- Switched to accuracy profile (slower)
- Switched to gtk ui

* Sun Nov 21 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.072-1
- Updated to 0.072
- Dropped gconf patch, added cheats one

* Wed Sep 29 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.070-1
- Updated to 0.070
- Don't change the way menus look
- Updated the qt folder path again
- Removed the executable suffix

* Mon Aug 23 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.068-1
- Updated to 0.068
- Updated both ppc elf patches
- Adapted to new source structure

* Sun Aug 01 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.067-1
- Updated to 0.067

* Sat Jul 03 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.065-1
- Updated to 0.065
- Updated Source0 to reflect new host (Google Code)

* Wed May 19 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.064-2
- Enabled snesreader unconditionally (#1214). Credit goes to Chris Moeller.

* Sat Apr 17 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.064-1
- Updated to 0.064
- Rediffed the patches
- Dropped pixelshaders subpackage since upstream did not ship it

* Sun Mar 28 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.063-1
- Updated to 0.063
- Dropped upstreamed dso patch

* Sun Feb 21 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.060-1
- Updated to 0.060
- Use sed to prevent premature binaries stripping
- Included supergameboy, snesfilter, pixelshaders and optionally snesreader
- Added patch to explicitly link against libdl

* Thu Jan 07 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.059-1
- Updated to 0.059
- Updated the strip patch
- Disabled the better pulseaudio driver on everything below Fedora 12

* Sat Dec 12 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.058-1
- Updated to 0.058

* Sat Nov 28 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.057-1
- Updated to 0.057

* Mon Nov 02 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.055-1
- Updated to 0.055

* Wed Oct 28 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.054-2
- Fixed the ppc-elf issue properly

* Wed Oct 21 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.054-1
- Updated to 0.054
- Disabled ppc-elf.c until we figure out why it does not build

* Mon Oct 19 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.053-1
- Updated to 0.053

* Tue Sep 29 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.052-1
- Updated to 0.052
- Given that bsnes is GPL now, the Qt requirement can be unversioned
- Cleaned up the make line
- Use %%global instead of %%define
- Dropped minizip-devel from BuildRequires

* Sun Sep 27 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.051-1
- Updated to 0.051
- Updated the strip patch
- Updated the license tag
- Dropped the system zlib patch, not needed anymore
- Updated the sed optflags line to catch all -O3 occurrences

* Sun Aug 29 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.050-1
- Updated to 0.050

* Mon Aug 24 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.049-1
- Updated to 0.049

* Tue Jul 14 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.048-1
- Updated to 0.048
- Updated the Fedora readme

* Sun Jun 07 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.047-1
- Updated to 0.047
- Updated the strip patch
- Dropped the line endings fix and updated the patches accordingly
- Dropped the no longer required profiler fix

* Sun May 10 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.046-1
- Updated to 0.046
- Dropped libXtst-devel BuildRequires
- Updated the strip patch again
- Updated the zlib patch again
- Updated the optflags fix
- Disabled profiling

* Mon Apr 20 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.045-1
- Updated to 0.045

* Tue Mar 31 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.042-1
- Updated to 0.042
- Use Qt build on all branches, hiro ui is no more
- Updated the strip patch
- Updated the URL and Source0 addresses

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.041-2
- rebuild for new F11 features

* Sun Mar 15 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.041-1
- Updated to 0.041
- Re-added documentation

* Mon Mar 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.040-1
- Updated to 0.040
- The desktop file now comes with the tarball
- Icon is now installed to %%{_datadir}/pixmaps
- The Qt ui is only built when it is legal to do so
- Updated the strip patch
- Fixed the last %%changelog entry

* Sun Feb 22 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.039-2
- Dropped the ExclusiveArch, libco has a C fallback
- Use macros consistently

* Tue Jan 20 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.039-1
- Updated to 0.039

* Wed Dec 17 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.038-1
- Updated to 0.038
- Updated system zlib patch (.h → .hpp)
- License and readme are now accessible through the executable
- Added pulseaudio-libs-devel to BuildRequires, dropped yasm
- Updated README.Fedora (PulseAudio driver)

* Fri Dec  5 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.037a-5
- Explained why system snes_ntsc is not used
- Explained why ExclusiveArch is used

* Sun Nov 30 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.037a-4
- Fixed README.Fedora permissions
- Added information concerning pulseaudio issues

* Sat Nov 29 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.037a-3
- Keep -fomit-frame-pointer
- $(strip) can stay
- Re-added system zlib patch

* Thu Nov 27 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.037a-2
- Patched the Makefile not to strip the binaries

* Sun Nov 23 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.037a-1
- Updated to 0.037a
- Dropped system zlib patch since bsnes uses zlib modified to support non-ansi filenames
- Added libXtst-devel to BuildRequires
- s/%%{ix86}/i386 to work around plague problem

* Tue Sep 16 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.036-1
- Updated to 0.036

* Mon Aug 25 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.035-1
- Updated to 0.035

* Sun Aug 10 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.033-1
- Updated to 0.033

* Wed May 28 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.032a-1
- Updated to 0.032a

* Sun May 25 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.032-1
- Updated to 0.032

* Mon Apr 14 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.031-1
- Updated to 0.031

* Thu Mar 27 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.030-1
- Updated to 0.030

* Mon Mar 17 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.029-1
- Updated to 0.029
- Dropped usleep patch
- Dropped destdir patch
- Updated system zlib patch
- Included patch approval

* Fri Feb 15 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.028.01-2
- Patched to fix CPU usage when idle
- Patched to use system zlib
- Dropped hicolor-icon-theme from Requires

* Sun Feb 10 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.028.01-1
- Updated to 0.028.01
- Updated the Makefile patch
- Added freealut-devel and SDL-devel to BuildRequires

* Tue Dec 25 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.027-1
- Updated to 0.027
- Updated the Makefile patch
- Switched to yasm for all supported architectures

* Sun Nov 18 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.026-1
- Updated to 0.026
- Dropped icon conversion, PNG is now shipped in the tarball
- Icon is now installed to %%{_datadir}/pixmaps
- Dropped the icon cache scriptlets
- Dropped the wrapper, it is no longer necessary
- Added zip/gzip and jma support

* Mon Nov  5 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.025-4
- Fixed permissions and line endings of source files as well
- Fixed cart.db permissions, got missing in previous release
- Fixed date in %%changelog

* Mon Nov  5 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.025-3
- Updated the scriptlets to be in par with current guidelines
- Changed to convert the icon at build time
- Use the wrapper to avoid putting cart.db into %%{_bindir}

* Sun Nov  4 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.025-2
- Install cart.db
- Use system optflags
- Adjusted the License tag

* Sun Nov  4 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.025-1
- Initial RPM release
