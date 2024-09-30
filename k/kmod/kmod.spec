Name:		kmod
Version:	32
Release:	alt1
Summary:	Linux kernel module management utilities

Group:		System/Kernel and hardware
License:	GPL-2.0-or-later AND LGPL-2.1-or-later
URL:		http://modules.wiki.kernel.org/
ExclusiveOS:	Linux
Requires:	lib%name = %version-%release

Source0:	%name-%version.tar

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

BuildRequires: bash-completion
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: glibc-devel-static
BuildRequires: liblzma-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: xsltproc
BuildRequires: zlib-devel

Provides:	module-init-tools = 3.17-alt1
Obsoletes:	module-init-tools
Conflicts:	module-init-tools-compat
Conflicts: filesystem < 3
Provides: /bin/kmod /bin/lsmod
Provides: /sbin/depmod /sbin/insmod /sbin/lsmod /sbin/modinfo /sbin/modprobe /sbin/rmmod

%description
The kmod package provides various programs needed for automatic
loading and unloading of modules under 2.6, 3.x, and later kernels, as well
as other module management programs. Device drivers and filesystems are two
examples of loaded and unloaded modules.

%package -n lib%name
Summary:	Libraries to handle kernel module loading and unloading
License:	LGPL-2.1-or-later
Group:		System/Kernel and hardware
Provides:	%name-libs = %version-%release

%description -n lib%name
The kmod-libs package provides runtime libraries for any application that
wishes to load or unload Linux kernel modules from the running system.

%package -n lib%name-devel
Summary:	Header files for kmod development
Group:		Development/C
License:	LGPL-2.1-or-later
Requires:	lib%name = %version-%release
Provides:	%name-devel = %version-%release

%description -n lib%name-devel
The libkmod-devel package provides header files used for development of
applications that wish to load or unload Linux kernel modules.

%package -n bash-completion-%name
Summary:        Bash completion routines for the kmod utilities
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Shells
BuildArch:      noarch
Requires:       %name
Requires:       bash-completion

%description -n bash-completion-%name
Contains bash completion support for kmod utilities.

%prep
%setup -q

%build
touch libkmod/docs/gtk-doc.make
%autoreconf

%configure \
	--disable-static \
	--disable-test-modules \
	--with-rootlibdir=%_libdir \
	--with-openssl \
	--with-zlib \
	--with-xz \
	--with-zstd \
	#
%make_build

%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot/%_libdir/*.la

# New configuration files we ship (if any) should go into /usr/lib/modprobe.d
# in order to allow the local sysadmin to customize /etc/modprobe.d
mkdir -p %buildroot/{%_sysconfdir,%prefix/lib}/modprobe.d
mkdir -p %buildroot/{%_sysconfdir,%prefix/lib}/depmod.d

# Add blacklists from module-init-tools
find rpm/modprobe.d -maxdepth 1 -type f -name '*.conf' -print0 |
	xargs -r0 install -m644 -p -t %buildroot%_modprobedir/ --

%ifarch %ix86 x86_64
install -m644 -p rpm/modprobe.d/arch/i386.conf %buildroot%_modprobedir/arch.conf
%endif

# Make compatibility symlinks
mkdir -p %buildroot%_sbindir
for n in modprobe modinfo insmod rmmod depmod lsmod; do
	t=$(relative %_bindir/kmod %_sbindir/$n)
	ln -s "$t" "%buildroot%_sbindir/$n"
done

# cleanup non-root access utils
rm -f %buildroot%_bindir/{depmod,insmod,modinfo,modprobe,rmmod}

%check
make check V=1

%files
%dir %_sysconfdir/depmod.d
%dir %_sysconfdir/modprobe.d
%dir %_prefix/lib/depmod.d
%dir %_modprobedir
%_modprobedir/*.conf
%_bindir/kmod
%_bindir/lsmod
%_sbindir/depmod
%_sbindir/insmod
%_sbindir/lsmod
%_sbindir/modinfo
%_sbindir/modprobe
%_sbindir/rmmod
%_man5dir/*
%_man8dir/*
%doc NEWS README.md COPYING

%files -n lib%name
%_libdir/libkmod.so.*

%files -n lib%name-devel
%_includedir/libkmod.h
%_pkgconfigdir/libkmod.pc
%_libdir/libkmod.so
%_datadir/pkgconfig/%name.pc

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%changelog
* Mon May 27 2024 Alexey Shabalin <shaba@altlinux.org> 32-alt1
- Version (32).
- Moved utils and lib to /usr.

* Sat Sep 30 2023 Alexey Gladkov <legion@altlinux.ru> 31-alt1
- Version (31).

* Wed Sep 21 2022 Alexey Gladkov <legion@altlinux.ru> 30-alt1
- Version (30).

* Tue Nov 02 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 29-alt1
- Version (29).
- Enabled zstd compression support.

* Thu Jun 25 2020 Alexey Gladkov <legion@altlinux.ru> 27.0.9.f5434cf-alt1
- Version (27).

* Mon Apr 01 2019 Alexey Gladkov <legion@altlinux.ru> 26-alt1
- Version (26).
- Add PKCS7 signatures support.

* Thu Mar 29 2018 Alexey Gladkov <legion@altlinux.ru> 25-alt1
- Version (25).

* Mon Aug 15 2016 Alexey Gladkov <legion@altlinux.ru> 23-alt1
- Version (23).

* Tue Jul 21 2015 Alexey Gladkov <legion@altlinux.ru> 21-alt1
- Version (21).
- Backport: fix return code in error path.

* Wed Nov 19 2014 Alexey Gladkov <legion@altlinux.ru> 19-alt1
- Version (19).

* Tue Sep 02 2014 Michael Shigorin <mike@altlinux.org> 18-alt1
- NMU: Version (18).

* Sun Feb 23 2014 Alexey Gladkov <legion@altlinux.ru> 16-alt1
- Version (16).

* Fri Jul 19 2013 Alexey Gladkov <legion@altlinux.ru> 14-alt1
- Version (14).

* Fri Dec 28 2012 Alexey Gladkov <legion@altlinux.ru> 12-alt1
- Version (12).

* Sun Sep 16 2012 Alexey Gladkov <legion@altlinux.ru> 10-alt1
- Version (10).

* Sun Aug 19 2012 Alexey Gladkov <legion@altlinux.ru> 9-alt2
- Updated to v9-20-g36ddee6.

* Tue Jul 17 2012 Alexey Gladkov <legion@altlinux.ru> 9-alt1
- Version (9).
- Replace the module-init-tools package (again).
- Add compatibility symlinks (again).

* Thu May 10 2012 Alexey Gladkov <legion@altlinux.ru> 8-alt2
- Fix rename kmod-devel to libkmod-devel.
- Fix libkmod-devel requires.

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 8-alt1
- Version (8).

* Thu Feb 16 2012 Alexey Gladkov <legion@altlinux.ru> 5-alt2
- Remove compatibility symlinks for now.

* Fri Feb 10 2012 Alexey Gladkov <legion@altlinux.ru> 5-alt1
- Version (5).
- Replace the module-init-tools package.
- Add blacklists.
- Add compatibility symlinks.

* Wed Feb 01 2012 Alexey Gladkov <legion@altlinux.ru> 4-alt1
- Version (4).
- Fix provides.

* Fri Jan 13 2012 Alexey Gladkov <legion@altlinux.ru> 3-alt1
- Version (3).
- Build for ALTLinux.

* Thu Jan 05 2012 Jon Masters <jcm@jonmasters.org> - 3-1
- Update to latest upstream (adds new depmod replacement utility)
- For the moment, use the "kmod" utility to test the various functions

* Fri Dec 23 2011 Jon Masters <jcm@jonmasters.org> - 2-6
- Update kmod-2-with-rootlibdir patch with rebuild automake files

* Fri Dec 23 2011 Jon Masters <jcm@jonmasters.org> - 2-5
- Initial build for Fedora following package import

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-4
- There is no generic macro for non-multilib "/lib", hardcode like others

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-3
- Update package incorporating fixes from initial review feedback
- Cleaups to SPEC, rpath, documentation, library and binary locations

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-2
- Update package for posting to wider test audience (initial review submitted)

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-1
- Initial Fedora package for module-init-tools replacement (kmod) library
