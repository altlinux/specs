# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pod2man gcc-c++
# END SourceDeps(oneline)
%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/xsunpinyin.conf
%define gitdate 20130710

Name: sunpinyin
Version: 2.0.4
Release: alt2_0.11
Summary: A statistical language model based Chinese input method engine
Group: System/Libraries
License: LGPLv2 or CDDL
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://code.google.com/p/sunpinyin/
Source0: %name-%gitdate.tar.xz
Source2: http://open-gram.googlecode.com/files/lm_sc.t3g.arpa-20121025.tar.bz2
Source3: http://open-gram.googlecode.com/files/dict.utf8-20130220.tar.bz2
Patch0: sunpinyin-aarch64.patch
BuildRequires: libsqlite3-devel
BuildRequires: gettext
BuildRequires: scons
BuildRequires: perl(Pod/Man.pm)
BuildRequires: python-devel
Source44: import.info

%description
Sunpinyin is an input method engine for Simplified Chinese. It is an SLM based
IM engine, and features full sentence input.

SunPinyin has been ported to various input method platforms and operating
systems. The 2.0 release currently supports iBus, XIM, and Mac OS X.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files that allows user
to write their own front-end for sunpinyin.

%package data
Summary: Little-endian data files for %name
Group: System/Libraries
License: CC-BY-SA
Obsoletes: %name-data-le
Obsoletes: %name-data-be

%description data
The %name-data package contains necessary lexicon data and its index data
files needed by the sunpinyin input methods.

%prep
%setup -n %name-%gitdate
%patch0 -p1
mkdir -p raw
cp %SOURCE2 raw
cp %SOURCE3 raw
pushd raw
tar xvf lm_sc.t3g.arpa-20121025.tar.bz2
tar xvf dict.utf8-20130220.tar.bz2
popd

%build
scons %{?_smp_mflags} --prefix=%prefix --libdir=%_libdir --datadir=%_datadir
export PATH=`pwd`/src:$PATH
pushd raw
ln -sf ../doc/SLM-inst.mk Makefile
make %{?_smp_mflags} VERBOSE=1
popd

%install
scons %{?_smp_mflags} --prefix=%prefix --libdir=%_libdir --datadir=%_datadir install --install-sandbox=%buildroot
pushd raw
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%files
%doc AUTHORS COPYING *.LICENSE
%doc README TODO
%_libdir/libsunpinyin*.so.*
%_docdir/%name/README

%files devel
%_libdir/libsunpinyin*.so
%_libdir/pkgconfig/sunpinyin*.pc
%_includedir/sunpinyin*

%files data
%_datadir/%name
%_bindir/*
%_mandir/man1/*.1*
%_docdir/%name/SLM-*.mk

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 2.0.4-alt2_0.11
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.11
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.9
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.8
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.7
- initial fc import

