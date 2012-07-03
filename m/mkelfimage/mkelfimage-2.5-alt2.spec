%define Name mkelfImage
Name: mkelfimage
Summary: Utility to Create ELF Boot Images from Linux Kernel Images
Version: 2.5
Release: alt2
License: %gpl2plus
Group: Networking/Other
Source: %Name-%version.tar
Patch0: %Name-2.5.dif
Patch1: %Name-optflags.patch
Patch2: %name-2.5-alt.patch
Provides: %Name = %version-%release

# Automatically added by buildreq on Wed Jul 25 2007
BuildRequires: zlib-devel rpm-build-licenses

%description
%Name is a program that makes an ELF boot image for Linux kernel
images. The image should work with any i386 multiboot compliant boot
loader or an ELF boot loader that passes no options. It is compliant
with the LinuxBIOS ELF booting specification or with the Linux kexec
kernel patch. A key feature here is that nothing relies on BIOS calls,
but they are made when necessary. This is useful for systems running
LinuxBIOS.


%prep
%setup -n %Name-%version
%patch0 -p0
%patch1 -p1
%patch2 -p1


%build
%autoreconf
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install
ln -sf %Name %buildroot%_sbindir/%name
ln -sf %Name.8 %buildroot%_man8dir/%name.8


%files
%_sbindir/*
%doc AUTHORS News
%_man8dir/*


%changelog -n mkelfImage
* Sun Aug 10 2008 Led <led@altlinux.ru> 2.5-alt2
- fixed spec
- updated %name-2.5-alt.patch

* Thu Jul 25 2007 Led <led@altlinux.ru> 2.5-alt1
- initial build for Sisyphus
- cleaned up spec
- renamed package from %Name to %name
- added %name-2.5-alt.patch

* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires

* Wed Jun 15 2005 - meissner@suse.de
- use RPM_OPT_FLAGS

* Wed May 19 2004 - ro@suse.de
- make it build on x86 again

* Wed Oct 29 2003 - stepan@suse.de
- initial version 2.5
