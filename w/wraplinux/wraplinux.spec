Summary: Utility to wrap a Linux kernel and initrd into an ELF or NBI file
Name: wraplinux
Version: 1.1
Release: alt1
License: GPL2
Group: System/Kernel and hardware
Url: http://www.kernel.org/pub/linux/utils/boot/wraplinux/
Source: http://www.kernel.org/pub/linux/utils/boot/wraplinux/wraplinux-%version.tar.gz
Patch: wraplinux-1.1-reloc.patch

%ifarch x86_64
%define mflag -fno-stack-protector
%else
%define mflag -m32 -fno-stack-protector
%endif


%description
A tool to wrap an x86 Linux kernel and one or more initrd files into a
single file in ELF or NBI format, as required by some booting protocols.

%prep
%setup 
%patch -p1 

%build
%autoreconf
%configure
%make CC='gcc %mflag' 

%install
%makeinstall CC='gcc %mflag' 

%files
%doc COPYING
%_bindir/wraplinux
%_man1dir/wraplinux.1*

%changelog
* Thu Feb 14 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.1-alt1
- ALT Linux adaptation

* Thu Jan 10 2008 H. Peter Anvin <hpa@zytor.com>
- Initial version.
