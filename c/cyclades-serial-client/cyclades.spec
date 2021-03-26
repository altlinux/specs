Name: cyclades-serial-client
Version: 0.93
Release: alt5

Summary: Serial port client
License: GPL
Group: System/Kernel and hardware
Url: http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client
Packager: Ilya Mashkin <oddity@altlinux.ru>

#Source: %url/%name-%version.tar.gz
Source: %name-%version.tgz
Patch: %name.patch
Patch1: %name-cflags.patch

# Automatically added by buildreq on Fri Jun 08 2007
BuildRequires: gcc-c++

%description
cyclades-serial-client is a 
RFC 2217 compliant client

%set_verify_elf_method textrel=relaxed

%prep
%setup -q

patch -p0 -i %PATCH0
%patch1 -p2

%build
%add_optflags -fcommon
%configure
%make
#%%make_build

%install
#mkdir -p %buildroot%_sysconfdir
%make_install install prefix=%buildroot
#install -m755 -D sercd.xinetd %buildroot/%_sysconfdir/sercd

%files
%_target_libdir_noarch/lib*
%_sysconfdir/*
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 0.93-alt5
- fix build with gcc-10

* Mon Apr 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.93-alt4
- fix build

* Fri Aug 20 2010 Ilya Mashkin <oddity@altlinux.ru> 0.93-alt3
- fix requires

* Tue Jun 12 2007 Lunar Child <luch@altlinux.ru> 0.93-alt2
- fix changelog.

* Fri Jun 08 2007 Lunar Child <luch@altlinux.ru> 0.93-alt1
- Initial build for ALT Linux Sisyphus.
