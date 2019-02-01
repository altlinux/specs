# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%set_verify_elf_method textrel=relaxed
%global major   4
%global minor   10
%global patch   2
%global rev     2614
%global vmver   %{major}.%{minor}.%{patch}.%{rev}
%global vmver2   %{major}.%{minor}.%{patch}-%{rev}
%global source  Squeak-%{vmver}-src

Name:           squeak-vm
Version:        %{vmver}
Release:        alt3_9
Summary:        The Squeak virtual machine

Group:          Development/Other
License:        MIT
URL:            http://squeakvm.org/unix
Source0:        http://squeakvm.org/unix/release/%{source}.tar.gz
Source1:        inisqueak
Source2:        squeak-desktop-files.tar.gz
Patch0:         squeak-vm-dprintf.patch
Patch1:         alsa-fixes.patch
Patch2:         squeak-vm-4.10.2-fix-cmake.patch
Patch3:         squeak-vm-4.10.2-squeak-init-fix.patch

# For clean upgrade path, could be probably dropped in F20 or later

Requires(post): shared-mime-info
Requires(postun): shared-mime-info

BuildRequires: ctest cmake
BuildRequires:  libX11-devel libXt-devel libvorbis-devel libtheora-devel libspeex-devel
BuildRequires:  libdbus-devel libalsa-devel pango-devel gstreamer-devel libGL-devel
BuildRequires:  libICE-devel libSM-devel libXext-devel libuuid-devel
BuildRequires:  libffi-devel libaudio-devel libpulseaudio-devel libxml2-devel glib2-devel
BuildRequires:  libcairo-devel libv4l-devel
Source44: import.info

%description
Squeak is a full-featured implementation of the Smalltalk programming
language and environment based on (and largely compatible with) the original
Smalltalk-80 system.

This package contains just the Squeak virtual machine.

%prep
%setup -q -n %{source} -a 2

%patch0 -p1 -b .dprintf
%patch1 -p2 -b .alsa-fixes
%patch2 -p1 -b .fix-cmake
%patch3 -p1 -b .squeak-init-fix

# Fix libdir
sed -i 's|libdir="${prefix}/lib/squeak"|libdir="%{_libdir}/squeak"|' unix/cmake/squeak.in

%build
mkdir -p bld
cd bld

export CFLAGS="-std=gnu89"

%{fedora_cmake} ../unix -DCMAKE_VERBOSE_MAKEFILE=ON -DVM_HOST="%{_host}" -DVM_VERSION="%{vmver2}" -DPLATFORM_SOURCE_VERSION="%{rev}"

make %{?_smp_mflags}

%install
make -C bld install DESTDIR=%{buildroot}

# these files will be put in std RPM doc location
rm -rf %{buildroot}%{_prefix}/doc/squeak

# install the desktop stuff
install -D --mode=u=rw,go=r squeak.xml %{buildroot}%{_datadir}/mime/packages/squeak.xml
install -D --mode=u=rw,go=r squeak.png %{buildroot}%{_datadir}/pixmaps/squeak.png

%global icons_dir %{buildroot}%{_datadir}/icons/gnome
for size in 16 24 32 48 64 72 96
do
  mkdir -p %{icons_dir}/${size}x${size}/mimetypes
  install -m0644 squeak${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-image.png
  install -m0644 squeaksource${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-source.png
done

# Remove squeak.sh & mysqueak, obsoleted
rm -f %{buildroot}%{_bindir}/squeak.sh

# Install own version of inisqueak
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/inisqueak
#ln -s %{vmver2} %buildroot%_libdir/squeak/current
mkdir -p %buildroot/usr/lib/rpm/
cat > %buildroot/usr/lib/rpm/squeak-vm.req << 'EOF'
#!/bin/sh -efu
echo squeak-vm = %{version}
'EOF'
cat > %buildroot/usr/lib/rpm/squeak-vm.req.files << 'EOF'
#!/bin/sh -efu
while IFS=$'\t' read -r f t; do
	[ -z "${f##${RPM_BUILD_ROOT-}%_libdir/squeak/%{vmver2}/so.*}" ] && echo "$f" ||:
done
'EOF'
chmod 755 %buildroot/usr/lib/rpm/squeak-vm.req*

%files
%doc unix/ChangeLog unix/doc/{README*,LICENSE,*RELEASE_NOTES}
%{_bindir}/*
%dir %{_libdir}/squeak
%dir %{_libdir}/squeak/%{vmver2}
%if 0 == 0%{?nonXOplugins}
%{_libdir}/squeak/%{vmver2}/so.FileCopyPlugin
%{_libdir}/squeak/%{vmver2}/so.B3DAcceleratorPlugin
#%{_libdir}/squeak/%{vmver2}/so.PseudoTTYPlugin
%{_libdir}/squeak/%{vmver2}/so.UnixOSProcessPlugin
%{_libdir}/squeak/%{vmver2}/so.XDisplayControlPlugin

%{_libdir}/squeak/%{vmver2}/so.AioPlugin
%{_libdir}/squeak/%{vmver2}/so.ClipboardExtendedPlugin
%{_libdir}/squeak/%{vmver2}/so.DBusPlugin
#%{_libdir}/squeak/%{vmver2}/so.GStreamerPlugin
#%{_libdir}/squeak/%{vmver2}/so.ImmX11Plugin
#%{_libdir}/squeak/%{vmver2}/so.KedamaPlugin
#%{_libdir}/squeak/%{vmver2}/so.KedamaPlugin2
%{_libdir}/squeak/%{vmver2}/so.MIDIPlugin
#%{_libdir}/squeak/%{vmver2}/so.OggPlugin
%{_libdir}/squeak/%{vmver2}/so.RomePlugin
%{_libdir}/squeak/%{vmver2}/so.Squeak3D
%{_libdir}/squeak/%{vmver2}/so.UUIDPlugin
#%{_libdir}/squeak/%{vmver2}/so.VideoForLinuxPlugin
%{_libdir}/squeak/%{vmver2}/so.HostWindowPlugin

#%{_libdir}/squeak/%{vmver2}/npsqueak.so
#%{_libdir}/squeak/%{vmver2}/squeak
%{_libdir}/squeak/%{vmver2}/so.vm-display-X11
%{_libdir}/squeak/%{vmver2}/so.vm-display-fbdev
%{_libdir}/squeak/%{vmver2}/so.vm-display-null
%{_libdir}/squeak/%{vmver2}/so.vm-sound-ALSA
%{_libdir}/squeak/%{vmver2}/so.vm-sound-OSS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-null

#%{_libdir}/squeak/%{vmver2}/so.Mpeg3Plugin
%{_libdir}/squeak/%{vmver2}/so.SqueakFFIPrims
%{_libdir}/squeak/%{vmver2}/so.vm-display-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-NAS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-pulse
%{_libdir}/squeak/%{vmver2}/squeakvm

# 4.10 plugins
%{_libdir}/squeak/%{vmver2}/ckformat
%{_libdir}/squeak/%{vmver2}/so.CameraPlugin
%{_libdir}/squeak/%{vmver2}/so.ScratchPlugin
%{_libdir}/squeak/%{vmver2}/so.UnicodePlugin
%{_libdir}/squeak/%{vmver2}/so.WeDoPlugin

%endif
%{_mandir}/man*/*
#%dir %{_datadir}/squeak
#%{_datadir}/squeak/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_datadir}/icons/gnome/*/mimetypes/*.png
%_libdir/squeak/%{vmver2}/so.Mpeg3Plugin
/usr/lib/rpm/squeak-vm.req*

%changelog
* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 4.10.2.2614-alt3_9
- force -std=c89 (see also debian#778129)

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 4.10.2.2614-alt3_8
- build with mp3 support; dropped symlink _libdir/squeak/current

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 4.10.2.2614-alt2_8
- added symlink _libdir/squeak/current

* Fri Aug 30 2013 Igor Vlasenko <viy@altlinux.ru> 4.10.2.2614-alt1_8
- Sisyphus build

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.0.3.2202-alt2.qa1
- NMU: rebuilt for debuginfo.

* Fri May 07 2010 Aleksey Lim <alsroot@altlinux.org> 4.0.3.2202-alt2
- remove squeak.sh that fetches kdebase-libs

* Thu Apr 29 2010 Aleksey Lim <alsroot@altlinux.org> 4.0.3.2202-alt1
- intial v4 spec rework by Anton A. Vinogradov
- minor spec tweak
- fix x86_64 build

* Fri Jan 29 2010 Anton A. Vinogradov <arc@altlinux.org> 3.10.5-alt0.6
- enable Mpeg3Plugin build

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 3.10.5-alt0.5
- initial build for ALT Linux

