%def_with klibc
%def_without debug

Name: v86d
%define prerel %nil
Version: 0.1.9
Release: alt1
Summary: A x86 Emulation Daemon
License: %gpl2only
Group: System/Kernel and hardware
URL: http://dev.gentoo.org/~spock/projects/uvesafb/
Source: %name-%version%prerel.tar
Patch: %name-%version-alt.patch

BuildPreReq: kernel-headers >= 2.6.25

BuildRequires: rpm-build-licenses
%{?_with_klibc:BuildRequires: klibc-devel >= 1.5-alt1.2}

%description
%name provides a backend for kernel drivers that need to execute ?86
BIOS code. The code is executed in a controlled environment and the
results are passed back to the kernel via the netlink interface.


%prep
%setup
%patch -p1

# Assume that adjust_kernel_headers --first has been run.
install -d -m 0755 linux/include
ln -s "$(readlink -ev /usr/include/linux/../..)"/include/* linux/include/


%build
%ifarch %ix86
%define _optlevel s
%else
%if_with klibc
%define _optlevel s
%else
%define _optlevel 3
%endif
%endif
export CFLAGS="%optflags"
./configure \
    %{subst_with debug} \
%if_with klibc
    --with-klibc
%else
    --default
%endif
%make KDIR=./linux


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README TODO
/sbin/*


%changelog
* Tue Oct 07 2008 Led <led@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Wed Sep 24 2008 Led <led@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Sat Aug 02 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.1.5.2-alt1
- 0.1.5.2

* Mon Jun 16 2008 Led <led@altlinux.ru> 0.1.5-alt3
- build with system klibc

* Sat May 31 2008 Led <led@altlinux.ru> 0.1.5-alt2
- fixed Summary and Group

* Fri May 30 2008 Led <led@altlinux.ru> 0.1.5-alt1
- added:
  + %name-0.1.5-format.patch
  + %name-0.1.5-makefile.patch
- build with system libc

* Wed May 07 2008 Led <led@altlinux.ru> 0.1.5-alt0.1
- 0.1.5

* Wed Dec 26 2007 Led <led@altlinux.ru> 0.1.3-alt0.1
- 0.1.3

* Sat Nov 17 2007 Led <led@altlinux.ru> 0.1.2-alt0.1
- 0.1.2

* Sun Oct 28 2007 Led <led@altlinux.ru> 0.1.1-alt0.1
- 0.1.1

* Fri Oct 19 2007 Led <led@altlinux.ru> 0.1-alt0.2
- fixed License

* Wed Aug 22 2007 Led <led@altlinux.ru> 0.1-alt0.1
- initial build
