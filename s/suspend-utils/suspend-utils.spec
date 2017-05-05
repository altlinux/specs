Name:           suspend-utils
Version:        1.0
Release:        alt1.git668c5f7
Summary:        A Set Of Tools To Support Sleep Modes
License:        GPLv2+
Url:            http://sourceforge.net/projects/suspend
#git		git://git.kernel.org/pub/scm/linux/kernel/git/rafael/suspend-utils.git
Group:          System/Base
#		git://git.altlinux.org/gears/s/suspend-utils.git
Source:         %name-%version-%release.tar
ExclusiveArch:  %ix86 x86_64

Provides: s2both
Provides: s2disk
Provides: s2ram
Provides: swap-offset

# Automatically added by buildreq on Thu Sep 09 2010
BuildRequires: libpci-devel libx86-devel perl-Switch

%description
A set of tools to support suspending notebooks, working around the
specific problems each machine has.

%prep
%setup -q

%build
%add_optflags --std=gnu89
%autoreconf
%configure
%make

%install
install -d %buildroot%_sysconfdir
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/suspend.conf
%doc %_datadir/doc/%name
%_man5dir/*
%_man8dir/*
%_libdir/suspend/resume
/usr/sbin/*

%changelog
* Fri May 05 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0-alt1.git668c5f7
- built commit 668c5f7
- packaged all the built files

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.1
- Fixed build

* Thu Sep 09 2010 Anton Farygin <rider@altlinux.ru> 0.8-alt1
- first build for Sisyphus
