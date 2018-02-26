Name: kinit-utils
Version: 1.5.25
Release: alt1

Summary: Small utilities built with klibc
License: BSD/GPL
Group: System/Base

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Patch0:  klibc.patch
Patch1:  md_run.patch
Patch2:  replace.patch
Patch3:  showenv.patch
Patch4:  ifconfig-readonly-fs.patch
Patch5:  ifconfig-quiet.patch
Patch6:  halt.patch
Patch7:  run-init-env.patch

# Automatically added by buildreq on Wed Nov 11 2009
BuildRequires: libcap-devel zlib-devel

%description
This package contains a collection of programs that are linked against
klibc.  These duplicate some of the functionality of a regular Linux
toolset, but are typically much smaller than their full-function
counterparts.  They are intended for inclusion in initramfs images and
embedded systems.

%prep
%setup -q
%patch0 -p0 -b .fix0
%patch1 -p0 -b .fix1
%patch2 -p0 -b .fix2
%patch3 -p0 -b .fix3
%patch4 -p0 -b .fix4
%patch5 -p0 -b .fix5
%patch6 -p0 -b .fix6
%patch7 -p0 -b .fix7

%build
%make_build

%install
%make_install \
	bindir=%buildroot/lib/initrd/bin \
	install
ln -s halt %buildroot/lib/initrd/bin/reboot
ln -s halt %buildroot/lib/initrd/bin/poweroff

rm -f %buildroot/lib/initrd/bin/fstype

%files
/lib/initrd

%changelog
* Thu Feb 09 2012 Alexey Gladkov <legion@altlinux.ru> 1.5.25-alt1
- Update kinit sources upto klibc-1.5.25-28-gdfd907c.
- replace:
  + Add posix character classes;
  + Add -r (revert) option;
  + Fix bugs.
- showenv:
  + Add -s (shell) option;
- Drop 'fstype' unused utility.

* Tue Jan 03 2012 Alexey Gladkov <legion@altlinux.ru> 1.5.17-alt2
- run-init:
  + Add -e option.

* Tue Apr 06 2010 Alexey Gladkov <legion@altlinux.ru> 1.5.17-alt1
- Update sources.
- Add halt utility.

* Fri Mar 05 2010 Alexey Gladkov <legion@altlinux.ru> 1.5.15-alt3
- ipconfig:
  + Add -r option;
  + Add -q option.

* Thu Nov 12 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.15-alt2
- Fix build with new kernel headers.

* Tue Nov 10 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.15-alt1
- First build for Sisyphus.

