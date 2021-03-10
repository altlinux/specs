%define _hardened_build 1
Name:           bochs
Version:        2.6.11
Release:        alt1
Summary:        Portable x86 PC emulator
License:        LGPLv2+
Group: Emulators
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL:            http://bochs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}-0001_bx-qemu.patch
Patch3: %{name}-0008_qemu-bios-provide-gpe-_l0x-methods.patch
Patch4: %{name}-0009_qemu-bios-pci-hotplug-support.patch
Patch7: %{name}-nonet-build.patch
# Update configure for aarch64 (bz #925112)
Patch8: bochs-aarch64.patch
Patch10: bochs-usb.patch
Patch11: bochs-2.6.10-slirp-include.patch
Patch12: smp-debug.patch
Patch13: iasl-filename.patch

ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  libXt-devel libXpm-devel libSDL2-devel readline-devel byacc libncurses-devel 
BuildRequires:  docbook-utils
BuildRequires:  gtk2-devel
BuildRequires: make
%ifarch %{ix86} x86_64
BuildRequires:  dev86 iasl

Requires:       %{name}-bios = %{version}-%{release}
%endif
Requires:       seavgabios

%description
Bochs is a portable x86 PC emulation software package that emulates
enough of the x86 CPU, related AT hardware, and BIOS to run DOS,
Windows '95, Minix 2.0, and other OS's, all on your workstation.


%package        debugger
Summary:        Bochs with builtin debugger
Requires:       %{name} = %{version}-%{release}
Group: Emulators

%description    debugger
Special version of bochs compiled with the builtin debugger.


%package        gdb
Summary:        Bochs with support for debugging with gdb
Requires:       %{name} = %{version}-%{release}
Group: Emulators
%description    gdb
Special version of bochs compiled with a gdb stub so that the software running
inside the emulator can be debugged with gdb.

%ifarch %{ix86} x86_64
# building firmwares are quite tricky, because they often have to be built on
# their native architecture (or in a cross-capable compiler, that we lack in
# koji), and deployed everywhere. Recent koji builders support a feature
# that allow us to build packages in a single architecture, and create noarch
# subpackages that will be deployed everywhere. Because the package can only
# be built in certain architectures, the main package has to use
# BuildArch: <nativearch>, or something like that.
# Note that using ExclusiveArch is _wrong_, because it will prevent the noarch
# packages from getting into the excluded repositories.
%package	bios
Summary:        Bochs bios
#BuildArch:      noarch
Provides:       bochs-bios-data = 2.3.8.1
Obsoletes:      bochs-bios-data < 2.3.8.1
Group: Emulators

%description bios
Bochs BIOS is a free implementation of a x86 BIOS provided by the Bochs project.
It can also be used in other emulators, such as QEMU
%endif

%package        devel
Summary:        Bochs header and source files
Requires:       %{name} = %{version}-%{release}
Group: Emulators

%description    devel
Header and source files from bochs source.

%prep
%setup -q
%patch0 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p0 -z .nonet
%patch10 -p0
%patch11 -p0
%patch12 -p3
%patch13 -p1

# Fix up some man page paths.
sed -i -e 's|/usr/local/share/|%{_datadir}/|' doc/man/*.*

# remove executable bits from sources to make rpmlint happy with the debuginfo
chmod -x `find -name '*.cc' -o -name '*.h' -o -name '*.inc'`
# Fix CHANGES encoding
iconv -f ISO_8859-2 -t UTF8 CHANGES > CHANGES.tmp
mv CHANGES.tmp CHANGES


%build
# Note: the CPU level, MMX et al affect what the emulator will emulate, they
# are not properties of the build target architecture.
# Note2: passing --enable-pcidev will change bochs license from LGPLv2+ to
# LGPLv2 (and requires a kernel driver to be usefull)
CONFIGURE_FLAGS=" \
  --enable-ne2000 \
  --enable-pci \
  --enable-all-optimizations \
  --enable-clgd54xx \
  --enable-sb16=linux \
  --enable-3dnow \
  --with-x11 \
  --with-nogui \
  --with-term \
  --with-rfb \
  --with-sdl2 \
  --without-wx \
  --with-svga=no \
  --enable-cpu-level=6 \
  --enable-disasm \
  --enable-e1000 \
  --enable-x86-64 \
  --enable-smp"
export CXXFLAGS="$RPM_OPT_FLAGS -DPARANOID"

%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-debugger
make %{?_smp_mflags}
mv bochs bochs-debugger
#make dist-clean

%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-gdb-stub --enable-smp=no
make %{?_smp_mflags}
mv bochs bochs-gdb
#make dist-clean

%configure $CONFIGURE_FLAGS
make %{?_smp_mflags}

%ifarch %{ix86} x86_64
cd bios
make bios
cp BIOS-bochs-latest BIOS-bochs-kvm
%endif

%install
rm -rf $RPM_BUILD_ROOT _installed-docs
make install DESTDIR=$RPM_BUILD_ROOT
ln -s %{_prefix}/share/seavgabios/vgabios-cirrus.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-cirrus
ln -s %{_prefix}/share/seavgabios/vgabios-isavga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-isavga
ln -s %{_prefix}/share/seavgabios/vgabios-qxl.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-qxl
ln -s %{_prefix}/share/seavgabios/vgabios-stdvga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-stdvga
ln -s %{_prefix}/share/seavgabios/vgabios-vmware.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-vmware
%ifnarch %{ix86} x86_64
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/bochs/*{BIOS,bios}*
%endif
install -m 755 bochs-debugger bochs-gdb $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_docdir}/bochs _installed-docs
rm $RPM_BUILD_ROOT%{_mandir}/man1/bochs-dlx.1*

mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm
cp -pr disasm/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
cp -pr disasm/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
cp -pr disasm/*.inc $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
cp -pr config.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu
cp -pr cpu/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
cp -pr cpu/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder
cp -pr cpu/decoder/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
cp -pr cpu/decoder/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
# Install osdep.h BZ 1786771
cp -pr osdep.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/

%files
%doc _installed-docs/* README-*
%{_bindir}/bochs
%{_bindir}/bximage
%{_bindir}/bxhub
# Note: must include *.la in %%{_libdir}/bochs/plugins/
#%%{_libdir}/bochs/
%{_mandir}/man1/bochs.1*
%{_mandir}/man1/bximage.1*
%{_mandir}/man5/bochsrc.5*
%dir %{_datadir}/bochs/
%{_datadir}/bochs/keymaps/

%ifarch %{ix86} x86_64
%files bios
%{_datadir}/bochs/BIOS*
%{_datadir}/bochs/vgabios*
%{_datadir}/bochs/VGABIOS*
%{_datadir}/bochs/bios.bin-1.13.0
%{_datadir}/bochs/SeaBIOS-README
%endif


%files debugger
%{_bindir}/bochs-debugger

%files gdb
%{_bindir}/bochs-gdb

%files devel
%{_prefix}/include/bochs/

%changelog
* Wed Mar 10 2021 Ilya Mashkin <oddity@altlinux.ru> 2.6.11-alt1
- 2.6.11

* Sat Jul 27 2013 Ilya Mashkin <oddity@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Apr 21 2013 Ilya Mashkin <oddity@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Oct 11 2012 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt1
- 2.6

* Thu Jan 12 2012 Ilya Mashkin <oddity@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Dec 04 2011 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- 2.5

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.6-alt1.qa1
- NMU: converted menu to desktop file

* Mon Feb 28 2011 Ilya Mashkin <oddity@altlinux.ru> 2.4.6-alt1
- 2.4.6
- Update requires

* Sun May 02 2010 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Wed Mar 10 2010 Ilya Mashkin <oddity@altlinux.ru> 2.4.2-alt2
- rebuild with current wxGTK

* Sun Nov 15 2009 Ilya Mashkin <oddity@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for bochs
  * postclean-05-filetriggers for spec file

* Mon May 11 2009 Ilya Mashkin <oddity@altlinux.ru> 2.4-alt1
- 2.4

* Thu Jul 03 2008 Ilya Mashkin <oddity at altlinux.ru> 2.3.7-alt1
- 2.3.7

* Wed Dec 26 2007 Ilya Mashkin <oddity at altlinux.ru> 2.3.6-alt1
- New version 2.3.6
+ More than 25%% emulation speedup vs Bochs 2.3.5 release
+ Up to 40%% speedup vs Bochs 2.3.5 release with trace cache optimization
+ Added emulation of Intel SSE4.2 instruction set
+ Bochs benchmarking support

* Tue Sep 18 2007 Ilya Mashkin <oddity at altlinux.ru> 2.3.5-alt1
- New version  2.3.5 
- Brief summary :
- Critical problems fixed for x86-64 support in CPU and Bochs internal debugger
- ACPI support
- The release compiled with x86-64 and ACPI
- Hard disk emulation supports ATA-6 (LBA48 addressing, UDMA modes)
- Added emulation of Intel SSE4.1 instruction set

* Sat Dec 23 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt3
- rebuild with wxGTK2u

* Tue Nov 07 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt2
- fix build

* Fri Sep 15 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt1
- New version 2.3

* Mon Feb 06 2006 Ilya Mashkin <oddity at altlinux.ru> 2.2.6-alt1
- New version 2.2.6

* Wed Jan 18 2006 Ilya Mashkin <oddity at altlinux.ru> 2.2.5-alt1
- New version 2.2.5

* Sat Nov 20 2005 Ilya Mashkin <oddity at altlinux.ru> 2.2.1-alt1
- New version 2.2.1

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt2.1.1
- Rebuilt with libstdc++.so.6.

* Tue Jun 22 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt2.1
- move to Applications/Emulators menu section

* Sun Jun 20 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt2
- rebuild
- add icon

* Wed Feb 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version
- build with --enable-vbe --enable-pci --enable-usb --enable-mmx

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt0.1pre3
- CVS version
- build with gcc 3.3

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt2.1
- really rebuild with new wxGTK

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 2.0.2-alt2
- rebuilt with new wxGTK

* Mon Apr 07 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version
- fixed bug #2489 (condrestart for xfs)
- build with wxWindows support
- add menu entry
- add shell wrapper for start from menu
- update buildreq

* Fri Jan 10 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- cleanup spec
- new version
- add buildrequires

* Fri Nov 02 2002 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- first build for Sisyphus
- spec adapted
- dlxlinux disabled

* Sat Aug 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4.1-2mdk
- rebuild

* Wed Jul 24 2002 Sylvestre Taburet <staburet@mandrakesoft.com> 1.4.1-1mdk
- upgraded to 1.4.1 (service release)

* Tue May 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-3mdk
- rebuild against new libstdc++

* Mon Apr 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-2mdk
- fix %post & %pre by adding %version to cure problem when
  version changes ( thx Quel Qun )

* Sat Mar 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4

* Tue Feb 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- new



