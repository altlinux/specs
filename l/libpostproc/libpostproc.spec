Name: libpostproc
Version: 0.9.0
Release: alt1
Epoch: 1

Summary: Video postprocessing library

Group: System/Libraries
License: GPL
Url: http://git.videolan.org/?p=libpostproc.git

Source: %name-%version-%release.tar

BuildRequires: libavutil-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %epoch:%version-%release

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %epoch:%version-%release

%description devel
This package contains development files for %name

%description devel-static
This package contains static development files for %name

%prep
%setup

%build
%add_optflags -frename-registers
%ifarch x86_64
%add_optflags %optflags_shared
%else
%ifarch %ix86
%add_optflags %{?_enable_mmx:-DRUNTIME_CPUDETECT}
%endif
%endif
./configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --shlibdir=%_libdir \
    --mandir=%_mandir \
    --enable-pic \
    --enable-shared \
    --disable-static \
    --enable-debug \
    --extra-cflags="%optflags" \
    #
%make V=1

%install
%make_install \
	INCDIR="%buildroot%_includedir" \
	DESTDIR="%buildroot" \
	MANDIR="%buildroot%_mandir" install

%set_verify_elf_method textrel=relaxed

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Mon Nov 19 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.9.0-alt1
- 0.9.0 released
