# Original author: Enrique Martinez <enmaca@hotmail.com>
# For other authors see git log
# license: GPL-3+

%global _unpackaged_files_terminate_build 1
%ifarch aarch64 armh %mips loongarch64
%def_disable seccomp
%else
%def_enable seccomp
%endif

# clsync handles IPO including LTO on its own,
# interference is not welcome
%define optflags_lto %nil

Name: clsync
Version: 0.4.5
Release: alt5

Summary: Live sync tool based on inotify
License: GPLv3+
Group: File tools

Url: https://github.com/clsync/clsync
Source0: %name-%version.tar

BuildRequires: glib2-devel libcap-devel libcgroup-devel
BuildRequires: doxygen graphviz
# XXX: graphviz produces broken graphs without fontconfig (and
# the actual font). Most importantly those graphs are broken in
# different ways on different architectures which causes a build
# failure due to non-identical noarch packages.
BuildRequires: fontconfig fonts-ttf-liberation


%define common_descr \
Live sync tool based on inotify, written in GNU C \
Clsync recursively watches for source directory and executes external \
program to sync the changes. Clsync is adapted to use together with rsync. \
This utility is much more lightweight than competitors and supports such\
features as separate queue for big files, regex file filter, \
multi-threading.

%description
%common_descr

%package devel
Summary: Development files for clsync
Group: Development/C
Requires: clsync = %EVR

%description devel
%common_descr

This package provides clsync development files.

%package -n libclsync
Summary: Control and monitoring library for clsync
Group: Development/C

%description -n libclsync
%common_descr

This package provides libclsync control and monitoring interface library.

%package -n libclsync-devel
Summary: Development files for the control and monitoring library for clsync
Group: Development/C
Requires: libclsync = %EVR

%description -n libclsync-devel
%common_descr

This package provides development files for the libclsync control and
monitoring interface library.

%package -n libclsync-devel-static
Summary: Static development files for the control and monitoring library for clsync
Group: Development/C
Requires: libclsync = %EVR

%description -n libclsync-devel-static
%common_descr

This package provides static development files for the libclsync control and
monitoring interface library.

%package examples
Summary: Examples for clsync
Group: Documentation
Buildarch: noarch

%description examples
%common_descr

This package provides config and usage examples for clsync.

%package apidocs
Summary: API documentation for clsync
Group: Development/Documentation
Buildarch: noarch

%description apidocs
%common_descr

This package provides doxygen API documentation for clsync.


%prep
%setup

%build
%autoreconf
%configure \
	--enable-socket-library \
	--enable-clsync \
	--disable-debug \
	--enable-paranoid=1 \
	--without-bsm \
	--without-kqueue \
	--enable-capabilities \
	--disable-cluster \
	--enable-socket \
	--enable-highload-locks \
	--enable-lto \
	--enable-unshare \
	%{subst_enable seccomp} \
	--with-libcgroup \
	--without-gio \
	--with-inotify=native \
	--without-mhash
%make_build
doxygen .doxygen

%install
%makeinstall_std

install -Dpm755 alt/%name.init %buildroot%_initdir/%name
install -Dpm644 alt/%name.sysconf %buildroot%_sysconfdir/sysconfig/%name
install -Dpm644 alt/%name.conf %buildroot%_sysconfdir/%name/%name.conf
install -Dpm644 "examples/%name@.service" %buildroot%_unitdir/%name@.service

mv doc/doxygen/html %buildroot%_docdir/%name/

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%doc %_docdir/%name
%exclude %_docdir/%name/examples
%exclude %_docdir/%name/html
%_man1dir/%name.1*
%_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_initdir/%name
%_unitdir/%name@.service

%files devel
%_includedir/%name/

%files -n libclsync
%_libdir/lib%name.so.0*

%files -n libclsync-devel
%_includedir/lib%name/
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%files -n libclsync-devel-static
%_libdir/lib%name.a

%files examples
%_docdir/%name/examples

%files apidocs
%_docdir/%name/html

%changelog
* Wed Nov 15 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.4.5-alt5
- Disabled seccomp on LoongArch. As a side note the list of allowed syscalls
  looks wrong even for x86: it should have included openat, fchmodat, etc.
  While at in fixed broken graphs in the documentation (so the apidocs
  package is identical on all architectures).

* Sun Sep 12 2021 Andrew Savchenko <bircoph@altlinux.org> 0.4.5-alt4
- Fix build after gross LTO enforcement.

* Wed Jul 28 2021 Ivan A. Melnikov <iv@altlinux.org> 0.4.5-alt3
- Disable seccomp on %%mips (porting is required)

* Mon Nov 30 2020 Andrew Savchenko <bircoph@altlinux.org> 0.4.5-alt2
- Major init script improvements, including:
  - Support for multiple clsync instances via config blocks and
    corresponding init script symlinks.
  - Add actions to control clsync via signals.

* Sun Nov 08 2020 Andrew Savchenko <bircoph@altlinux.org> 0.4.5-alt1
- Version bump
- Enable LTO support
- Disable seccomp on armh (porting is required)

* Wed May 06 2020 Andrew Savchenko <bircoph@altlinux.org> 0.4.4-alt2
- Disable mhash support since it is actually used only with cluster
  or kqueue code and both are disabled in Alt.

* Wed May 06 2020 Andrew Savchenko <bircoph@altlinux.org> 0.4.4-alt1
- Version bump
- Package configuration change to follow upstream
- Repackage for finer split
- Fix various bugs

* Sat Oct 01 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt2
- improved initscript to actually stop the service
- added post/preun service scriptlets

* Sat Oct 01 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- built for sisyphus @ #ossdevconf

* Thu Sep 29 2016 Andrew A. Savchenko <bircoph@gmail.com> - 0.4.2-1
- Maintenance release, many bug fixes

* Thu Nov 6 2014 Dmitry Yu Okunev <dyokunev@ut.mephi.ru> - 0.4-1
- A lot of fixes

* Thu Jan 9 2014 Dmitry Yu Okunev <dyokunev@ut.mephi.ru> - 0.3-1
- Added support of control socket

* Thu Oct 24 2013 Barak A. Pearlmutter <bap@debian.org> - 0.2.1-1
- New upstream version

* Fri Oct 11 2013 Barak A. Pearlmutter <bap@debian.org> - 0.1-2
- Tweak debian/watch to ignore debian releases

* Sat Sep 07 2013 Barak A. Pearlmutter <bap@debian.org> - 0.1-1
- Initial release (Closes: #718769 )
