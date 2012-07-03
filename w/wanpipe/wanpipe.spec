%set_verify_elf_method relaxed
%define kernel_flavour el-smp
%add_findreq_skiplist %_sysconfdir/*

Name: wanpipe
Summary: %name
Version: 3.5.20
Release: alt1
License: GPL
Group: System/Kernel and hardware
BuildRequires: bison flex gcc-c++ libncurses-devel libreadline rsync
BuildPreReq: kernel-headers-modules-%kernel_flavour
BuildPreReq: kernel-headers-dahdi-%kernel_flavour
BuildPreReq: less
Url: http://wiki.sangoma.com/wanpipe-linux-drivers
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Patch1: %name.buildroot.patch
Patch2: %name.altlinux.patch
Patch3: %name.fix-build.patch
Patch4: %name.rc.conf.patch
Patch5: %name.dahdi.patch

%package -n kernel-source-wanpipe
Summary: %name
Group: Development/Kernel

%description -n kernel-source-wanpipe
%name

%package -n libsangoma
Summary: %name
Group: System/Kernel and hardware

%description -n libsangoma
%name

%package -n libsangoma-devel
Summary: %name
Group: System/Kernel and hardware
Requires: libsangoma = %version-%release

%description -n libsangoma-devel
%name

%package -n libsangoma-devel-static
Summary: %name
Group: System/Kernel and hardware
Requires: libsangoma-devel = %version-%release

%description -n libsangoma-devel-static
%name

%package complete
Summary: %name
Group: System/Kernel and hardware
Requires: kernel-source-wanpipe = %version-%release
Requires: libsangoma-devel = %version-%release
Requires: libsangoma = %version-%release
Requires: wanpipe-docs = %version-%release
Requires: wanpipe = %version-%release

%description complete
%name

%package docs
Summary: %name
Group: System/Kernel and hardware
BuildArch: noarch

%description docs
%name

%description
%name


%prep
%setup
%patch1
%patch2 -p2
%patch3 -p2
%patch4 -p1
%patch5 -p2
find -type f -name '*.swp' -delete
find -type f -name '*.bak' -delete
find -type f -name '*.orig' -delete
find -type d -name '.svn' -print0 | xargs -0r rm -rf
find -type f -name 'wanconfig_client' -delete
find -type f -name 'wpkbdmon' -delete
find -type f -name 'wp_x25_event_read' -delete

%build
tar -c -j -f ../%name-%version.tar.bz2 .
ls -l

%install
tmp_root=../000
tmp_kernel=../tmp.kernel
mkdir -p $tmp_root $tmp_kernel
tmp_root=`realpath "$tmp_root"`
tmp_kernel=`realpath "$tmp_kernel"`
mkdir -p $tmp_root/etc/wanpipe
mkdir -p $tmp_kernel
krn=%_usrsrc/`ls -1 %_usrsrc | grep ^linux-.*-%kernel_flavour-alt | sort -n | tail`
rsync -ak --delete $krn/ $tmp_kernel/
inc=`realpath $tmp_kernel/include`
bd=$tmp_root
cp -a $tmp_kernel/drivers/dahdi/* $tmp_kernel/kernel/
cat $tmp_kernel/kernel-modules-dahdi.symvers >> $tmp_kernel/Module.symvers
touch $tmp_kernel/drivers/Makefile
export EXTRA_FLAGS=-I$inc
./Setup install \
    --silent \
    --builddir=$bd \
    --protocol=TDM \
    --with-linux="$tmp_kernel" \
    --with-zaptel=$tmp_kernel/drivers/
mkdir -p %buildroot%_usrsrc/kernel/sources/
cp ../%name-%version.tar.bz2 %buildroot%_usrsrc/kernel/sources/kernel-source-%name-%version.tar.bz2
install -D -m755 samples/wanrouter $bd%_initdir/wanrouter
rm -rf $tmp_root/%_sysconfdir/wanpipe/api
rm -rf $tmp_root/lib/modules
rm -rf $tmp_root/%_docdir
rm -f  $tmp_root/usr/local/sbin/setup-sangoma
mv  $tmp_root/%_sysconfdir/wanpipe/util/wan_aftup/wan_aftup $tmp_root/%_sbindir/
ln -s %_sbindir/wan_aftup $tmp_root/%_sysconfdir/wanpipe/util/wan_aftup/wan_aftup
%ifarch x86_64
mkdir  -p $tmp_root/usr/lib64
mv $tmp_root/usr/lib/* $tmp_root/usr/lib64/
%endif
find $tmp_root/ -type d -empty -delete
cp -a $tmp_root/* %buildroot/
rm -f %buildroot/etc/wanpipe/util/wan_aftup/*.o

%preun
%preun_service wanrouter

%post
%post_service wanrouter

%files
%_initdir/wanrouter
%_sbindir/*
%config(noreplace) %_sysconfdir/wanpipe

%files -n kernel-source-wanpipe
%_usrsrc/kernel/sources/kernel-source-%name-%version.tar.bz2

%files -n libsangoma
%_libdir/libsangoma.so.3
%_libdir/libsangoma.so.3.0.5
%_libdir/libstelephony.so.2
%_libdir/libstelephony.so.2.0.0

%files -n libsangoma-devel
%_libdir/libsangoma.so
%_libdir/libstelephony.so
%_includedir/*

%files -n libsangoma-devel-static
%_libdir/libsangoma.a
%_libdir/libstelephony.a

%files complete

%files docs
%doc doc/*

%changelog
* Sat Jul 09 2011 Denis Smirnov <mithraen@altlinux.ru> 3.5.20-alt1
- 3.5.20

* Sun Jan 09 2011 Denis Smirnov <mithraen@altlinux.ru> 3.5.14-alt1
- 3.5.14

* Sun Apr 18 2010 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt7
- fix build (build with headers from ovz-smp)

* Wed Nov 11 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt6
- fix build
- fix DAHDI support in default start script

* Thu Sep 17 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt5
- build with DAHDI instead of Zaptel

* Wed Sep 16 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt4
- correct initscript install

* Wed Sep 02 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt3
- fix building

* Wed Sep 02 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt2
- fix requires

* Wed Sep 02 2009 Denis Smirnov <mithraen@altlinux.ru> 3.5.6-alt1
- 3.5.6

* Mon Feb 16 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.15-alt1.4
- package initscript

* Mon Dec 15 2008 Denis Smirnov <mithraen@altlinux.ru> 3.3.15-alt1.3
- small fixes

* Mon Dec 15 2008 Denis Smirnov <mithraen@altlinux.ru> 3.3.15-alt1.2
- fix kernel-source-%name
- build kernel-source-%name as noarch

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 3.3.15-alt1.1
- fix build in hasher

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 3.3.15-alt1
- first build for Sisyphus

