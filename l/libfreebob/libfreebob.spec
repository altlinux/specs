%def_disable static
%define rel rc1
%define svnrel r300
%undefine svnrel

Name: libfreebob
Version: 1.0.11
%ifdef svnrel
Release: alt0.svn.%svnrel
%else
Release: alt3
%endif

Summary: Free Firewire Audio Drivers
License: GPL
Group: System/Libraries
URL: http://freebob.sourceforge.net

%ifdef svnrel
Source0: %name-%version-svn.%svnrel.tar
%else
Source: http://prdonwnloads.sourceforge.net/%name/%name-%version.tar.gz
%endif

# fedora patch
Patch: libfreebob-1.0.11-includes.patch
# https://svn.pardus.org.tr/pardus/2011/devel/hardware/firewire/libfreebob/files/gcc-4.5.patch
Patch1: libfreebob-1.0.11-gcc-4.5.patch

BuildRequires: gcc-c++, libraw1394-devel >= 1.2.1, libiec61883-devel >= 1.1.0
BuildRequires: libavc1394-devel >= 0.5.3, libxml2-devel, libalsa-devel

%description
FreeBoB is a driver for BeBoB which is the firmware. Currently, there is only
one chip in the wild which is running this kind of software, the DM1000. But it
is to be expected to find soon other chips (still prefix-labled with DM) which
will running BeBoB versions.

%package devel
Summary: Header files for libfreebob library
Group: Development/C
Requires: %name = %version-%release
Provides: libfreebob-devel
Obsoletes: libfreebob-devel < %version-%release

%description devel
Header files for libfreebob library.

%prep
%ifdef svnrel
%setup -q -n %name-%version-svn.%svnrel
%else
%setup -q
%endif

%patch -p1
%patch1 -p1 
# Tweak libiec61883 build requirements.
perl -pi -e 's/1.1.0/1.0.0/' configure

%build
%ifdef svnrel
%autoreconf
%endif
%configure \
	%{subst_enable static}

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%name
%_pkgconfigdir/*.pc

%if_enabled static
%_libdir/lib*.a
%endif #static

%changelog
* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt3
- rebuild for soname set-versions

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt2
- fixed build (tnx fedora)

* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt1
- 1.0.11 release
- removed obsolete post{,un}_ldconfig calls

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.svn.r300
- svn snapshot r300 from 1.0.0 stable branch.

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.9.0-alt1.rc1
- initial build for ALTLinux.
