Name: libss7
Summary: SS7 library for Asterisk
Version: 1.0.2
Release: alt5
License: GPL
Group: System/Libraries

Url: http://downloads.asterisk.org/pub/telephony/libss7/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sat Jul 11 2009
BuildRequires: dahdi-linux-headers

%description
SS7 library

%package devel
Summary: development files for libss6
License: GPL
Group: Development/C
Requires: libss7

%description devel
Headers for SS7 library

%prep
%setup
sed -i 's/-Werror//' Makefile

%build
find -type f -name '.depend' -print0 \
	| xargs -0r rm -f

%make_build

%install
%make_install \
	DESTDIR=%buildroot \
	INSTALL_PREFIX=%buildroot \
	libdir=%_libdir \
	install

%files devel
%_includedir/libss7.h
%_libdir/libss7.so
%files
%_libdir/libss7.so.1.0
%_libdir/libss7.so.1
%exclude %_libdir/libss7.a

%changelog
* Mon Jun 18 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt5
- fix build

* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt4
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt3
- auto rebuild

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt2
- add Url tag

* Sat Jul 11 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- update to 1.0.2

* Sun Jul 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20090705
- svn update

* Fri Nov 14 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20081114
- svn update

* Fri May 16 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20080516
- svn update

* Sun Jan 14 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20070114
- svn update

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20061015
- svn update

* Sat Oct 14 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20061014
- svn update

* Thu Sep 21 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060921
- svn update

* Tue Sep 19 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060919
- svn update

* Mon Sep 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060918
- svn update

* Sat Sep 16 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060916
- svn update

* Fri Sep 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060915
- svn update

* Thu Sep 14 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060914
- svn update

* Wed Sep 13 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060913
- svn update

* Tue Sep 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060912
- svn update

* Mon Sep 11 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060911
- svn update

* Sun Sep 10 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060910
- svn update

* Sat Sep 09 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060909
- svn update

* Fri Sep 08 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060908
- svn update

* Thu Sep 07 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060907
- svn update

* Wed Sep 06 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060906
- svn update

* Tue Sep 05 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060905
- svn update

* Mon Sep 04 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060904
- svn update

* Sun Sep 03 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060903
- svn update

* Sat Sep 02 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060902
- svn update

* Fri Sep 01 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060901
- svn update

* Thu Aug 31 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060831
- svn update

* Wed Aug 30 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060830
- svn update

* Tue Aug 29 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060829
- svn update

* Mon Aug 28 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060828
- svn update

* Sun Aug 27 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060827
- svn update

* Sat Aug 26 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060826
- svn update

* Fri Aug 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060825
- svn update

* Thu Aug 24 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060824
- svn update

* Wed Aug 23 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060823
- svn update

* Tue Aug 22 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060822
- svn update

* Mon Aug 21 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060821
- svn update

* Sun Aug 20 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060820
- svn update

* Sat Aug 19 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060819
- svn update

* Fri Aug 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060818
- svn update
- create separate devel file

* Sat Aug 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20060812
- first build for Sisyphus
