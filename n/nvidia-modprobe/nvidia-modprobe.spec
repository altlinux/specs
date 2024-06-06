Name: nvidia-modprobe
Version: 550.90.07
Release: alt1

Group: System/Configuration/Hardware
Summary: Helper to load kernel module and create device files
Url: ftp://download.nvidia.com/XFree86/nvidia-modprobe/
License: GPL-2.0-or-later

Source: %name-%version.tar
Patch1: alt-cflags.patch

BuildRequires: glibc-devel

%description
 The nvidia-modprobe utility is used by user-space NVIDIA driver components
to make sure the NVIDIA kernel module is loaded and that the NVIDIA
character device files are present.  These facilities are normally provided
by Linux distribution configuration systems such as udev.  When possible,
it is recommended to  use  your  Linux distribution's  native  mechanisms
for  managing kernel module loading and device file creation.  This utility
is provided as a fallback to work out-of-the-box in a distribution-independent way.

%prep
%setup -q
%patch1 -p1 -b .flags

%build
%make_build NV_VERBOSE=1 OUTPUTDIR=BUILD STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1 PREFIX=%prefix CC=gcc LOCAL_CFLAGS="%optflags"
cp -ar BUILD/nvidia-modprobe.unstripped BUILD/nvidia-modprobe

%install
make install NV_VERBOSE=1 OUTPUTDIR=BUILD STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1 PREFIX=%buildroot/%prefix bindir=%buildroot/%_bindir mandir=%buildroot/%_man1dir
#install -m 0755 nvidia-modprobe %buildroot/%_bindir

%files
%doc COPYING
%attr(4711,root,root) %_bindir/%name
%_man1dir/%name.*


%changelog
* Thu Jun 06 2024 Sergey V Turchin <zerg@altlinux.org> 550.90.07-alt1
- new version

* Thu Feb 29 2024 Sergey V Turchin <zerg@altlinux.org> 550.54.14-alt1
- new version

* Tue Sep 19 2023 Sergey V Turchin <zerg@altlinux.org> 535.104.05-alt1
- new version

* Mon Jul 31 2023 Sergey V Turchin <zerg@altlinux.org> 535.86.05-alt2
- allow force permissions for all users

* Fri Jul 21 2023 Sergey V Turchin <zerg@altlinux.org> 535.86.05-alt1
- new version
- remove SUID (closes: 43826)

* Tue Apr 11 2023 Sergey V Turchin <zerg@altlinux.org> 525.105.17-alt1
- new version

* Fri Apr 08 2022 Sergey V Turchin <zerg@altlinux.org> 510.60.02-alt1
- new version

* Wed Nov 24 2021 Sergey V Turchin <zerg@altlinux.org> 470.86-alt2
- make SUID

* Mon Nov 22 2021 Sergey V Turchin <zerg@altlinux.org> 470.86-alt1
- initial build

