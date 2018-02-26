Name: microcode_ctl
Version: 1.17
Release: alt2

Packager: Vicror Forsiuk <force@altlinux.org>

Summary: Tool to update x86/x86-64 CPU microcode
License: GPLv2+
Group: System/Kernel and hardware

URL: http://www.urbanmyth.org/microcode/
Source0: %url/microcode_ctl-%version.tar.gz
Source1: microcode_ctl.init
Patch1: microcode_ctl.patch

Requires: microcode-data

# microcode_ctl is useless for non-x86 processors. But in order to satisfy
# current ALT Linux distro releasing technology packages should build for all
# architectures.
#ExclusiveArch: %intel

%description
The microcode_ctl utility is a companion to the IA32 microcode driver.
The utility has two uses: a) it decodes and sends new microcode to the
kernel driver to be uploaded to Intel IA32 family processors. (Pentium
Pro, PII, Celeron, PIII, Xeon Pentium 4 etc.) b) it signals the kernel
driver to release any buffers it may hold

The microcode update is volatile and needs to be uploaded on each
system boot i.e. it doesn't reflash your cpu permanently, reboot and
it reverts back to the old microcode.

%prep
%setup
%patch1 -p1

%build
gcc %optflags microcode_ctl.c -o microcode_ctl

%install
install -pD microcode_ctl %buildroot/sbin/microcode_ctl
install -pD microcode_ctl.8 %buildroot%_man8dir/microcode_ctl.8

install -pD %SOURCE1 %buildroot%_initdir/microcode_ctl

%post -p "%post_service %name"
%preun -p "%preun_service %name"

%files
%doc README Change*
%config %_initdir/*
/sbin/microcode_ctl
%_man8dir/*

%changelog
* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Package only utility. Microcode data will be in separate packages.
- Move utility from %_sbindir to /sbin.
- Use /lib/microcode for microcode data instead of /etc.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt2
- Comment ExclusiveArch for now.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Dec 12 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt2
- Shift service start priority to run after udev is up.
- Remove microcode kernel module after microcode uploading.

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt1
- Initial build.
