Name: dynamips
Version: 0.2.8
Release: alt1rc2

Summary: Cisco 7200 Simulator
License: GPL
Group: Emulators

Url: http://www.ipflow.utc.fr/index.php/Cisco_7200_Simulator

Source0: %name-%version-RC2.tar.gz
Patch0: dynamips-Makefile.patch
Patch1: %name-0.2.8-RC2-alt-makefile.patch

# Automatically added by buildreq on Sun Mar 23 2008
BuildRequires: libelf-devel libpcap-devel

%description
A project to emulate a Cisco 7200 on a traditionnal PC.
The emulator currently supports the following platforms:
 - Cisco 7200 (NPE-100 to NPE-400)
 - Cisco 3600 (3620, 3640 and 3660)
 - Cisco 2691
 - Cisco 3725
 - Cisco 3745
 - Cisco 2600 (2610 to 2650XM)
 - Cisco 1700 (1710 to 1760)

The goals of this emulator are mainly:
    * To be used as a training platform, with software used in real world. It
      would allow people to become more familiar with Cisco devices, Cisco
      being the world leader in networking technologies ;
    * Test and experiment the numerous and powerful features of Cisco IOS ;
    * Check quickly configurations to be deployed later on real routers.

%prep
%setup -q -n %name-%version-RC2
%patch1 -p1

%build
%ifarch x86_64
# parallel build fails
ARCH=amd64
%else
%ifarch %ix86
ARCH=x86
%else
ARCH=nojit
%endif
%endif

%make \
	DYNAMIPS_ARCH=$ARCH \
	CC="%__cc" \
	LD="%__ld"

%install
install -d %buildroot{%_bindir,%_man1dir,%_man7dir}
install -d %buildroot%_localstatedir/%name/{labs,images}
install -p -m755 %name %buildroot%_bindir/
install -m644 dynamips.1 nvram_export.1 %buildroot%_man1dir/
install -m644 hypervisor_mode.7 %buildroot%_man7dir/

%files
%doc README* ChangeLog TODO
%_man1dir/dynamips.1*
%_man1dir/nvram_export.1*
%_man7dir/hypervisor_mode.7*
%_bindir/%name
%dir %_localstatedir/%name/images
%dir %_localstatedir/%name/labs

%changelog
* Sat Mar 22 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.8-alt1rc2
- 0.2.8-RC2
- add hypervisor_mode man page

* Thu Jul 05 2007 Michael Shigorin <mike@altlinux.org> 0.2.7-alt1
- initial build for ALT Linux Sisyphus (spec based on 
  PLD 0.2.5-0.1 rev 1.5 and Mandriva Contribs 0.2.7-1mdv2008.0)
- use mdv makefile patch

