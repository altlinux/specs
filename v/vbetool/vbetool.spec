Name: vbetool
Version: 1.2.2
Release: alt1

Summary: Run real-mode video BIOS code to alter hardware state

Group: System/Kernel and hardware
License: GPLv2
Url: http://www.codon.org.uk/~mjg59/vbetool/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.codon.org.uk/~mjg59/vbetool/download/vbetool-%version.tar

# does not build on ppc, ppc64 and sparc arches, see #285361 (RedHat Bugzilla)
# on ppc sys/io.h is missing, on ppc64 there are more complaints
# build.logs are attached in the bug report
ExcludeArch: ppc ppc64

# Automatically added by buildreq on Mon Mar 22 2010
BuildRequires: glibc-devel libpciaccess-devel libx86-devel zlib-devel

%description
vbetool uses lrmi in order to run code from the video BIOS. Currently, it is
able to alter DPMS states, save/restore video card state and attempt to
initialize the video card from scratch.

%prep
%setup

%build
%autoreconf
# TODO: add pkg-config file to libx86-devel
%configure --with-x86emu LIBX86_LIBS="-L%_libdir" LIBX86_CFLAGS="-I%_includedir"
%make_build

%install
%makeinstall_std
install -m 0644 -D udev-video-post-example.rules %buildroot%_sysconfdir/udev/rules.d/92-video-post.rules

%files
%_sbindir/vbetool
%_man1dir/*
%_sysconfdir/udev/rules.d/92-video-post.rules

%changelog
* Mon Mar 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 from new codebase (thanks, Fedora)

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 0.7-alt1
- new version

* Tue Jan 31 2006 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- new version
- fixed build for x86_64

* Fri Feb 18 2005 Anton Farygin <rider@altlinux.ru> 0.2-alt1
- first build for Sisyphus
