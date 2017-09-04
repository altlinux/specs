%global _udevlibdir /lib/udev

Summary: Tools for Linux kernel block layer cache
Name: bcache-tools
Version: 1.0.8
Epoch: 1
Release: alt2
License: GPLv2
Group: System/Kernel and hardware
Url: http://bcache.evilpiepirate.org/

Source0: %name.tar
Patch: %name-%version-alt.patch
BuildRequires: libuuid-devel libblkid-devel

# This part is a prerelease version obtained by https://gist.github.com/djwong/6343451:
# git clone https://gist.github.com/6343451.git
# cd 6343451/
# git archive --format=tar --prefix=bcache-status-20140220/ 6d278f9886ab5f64bd896080b1b543ba7ef6c7a6 | gzip > ../bcache-status-20140220.tar.gz
# see also http://article.gmane.org/gmane.linux.kernel.bcache.devel/1951
Source1: bcache-status-20140220.tar.gz
# bcache status not provided as a true package, so this is a self maintained
# man page for it
# http://article.gmane.org/gmane.linux.kernel.bcache.devel/1946
Patch5: %{name}-status-20160804-man.patch
# Fix BZ#1360951 - this fix is python 3 only
Patch6: bcache-status-rootgc.patch

%description
Bcache is a Linux kernel block layer cache. It allows one or more fast disk
drives such as flash-based solid state drives (SSDs) to act as a cache for
one or more slower hard disk drives.
This package contains the utilities for manipulating bcache.

%package -n bcache-status
Summary: Display useful bcache statistics
Group: System/Kernel and hardware
Requires: %name
BuildArch: noarch
%description -n bcache-status
Display useful bcache statistics

%prep
%setup -n %name
%patch0 -p1

tar xzf %SOURCE1 --strip-components=1
mv -fv bcache-status.8 bcache-status.8.old
%patch5 -p1 -b .man
chmod +x configure
%patch6 -p1 -b .rootgc

%build
%configure
%make_build

%install
mkdir -p \
    %buildroot%_sbindir \
    %buildroot%_man8dir \
    %buildroot%_udevlibdir \
    %buildroot%_udevrulesdir

%makeinstall_std \
    UDEVLIBDIR=%_udevlibdir \
    MANDIR=%_mandir

install -p  -m 755 bcache-status %buildroot%_sbindir/bcache-status

%files
%_udevrulesdir/*
%_man8dir/bcache-super-show.8.*
%_man8dir/make-bcache.8.*
%_man8dir/probe-bcache.8.*
%_udevlibdir/bcache-register
%_udevlibdir/probe-bcache
%_sbindir/bcache-super-show
%_sbindir/make-bcache
%doc README COPYING

%files -n bcache-status
%_sbindir/bcache-status
%_man8dir/bcache-status.8.*

%changelog
* Mon Sep 04 2017 Lenar Shakirov <snejok@altlinux.ru> 1:1.0.8-alt2
- External bcache-status added (peeped from Fedora)

* Mon Aug 22 2016 Alexei Takaseev <taf@altlinux.org> 1:1.0.8-alt1
- 1.0.8
- fix build with gcc5

* Thu Jan 23 2014 Terechkov Evgenii <evg@altlinux.org> 1:0.9-alt1
- 0.9

* Fri Nov  8 2013 Terechkov Evgenii <evg@altlinux.org> 0-alt1.20131108
- git-20131108

* Mon Sep  9 2013 Terechkov Evgenii <evg@altlinux.org> 0-alt1.20130907
- Initial build for ALT Linux Sisyphus
