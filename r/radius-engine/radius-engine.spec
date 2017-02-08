# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		radius-engine
Version:	1.1
Release:	alt1_8
Summary:	A Lua based real-time 2D graphics game engine
Group:		System/Libraries
License:	MIT
URL:		http://radius-engine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-1.1-shared-libs.patch
# Latest autoconf enables "extra-portability" along with "Wall", which causes
# warnings (treated as errors because of Wall) to be thrown. We just need to 
# pass "-Wno-extra-portability" to fix this.
Patch2:		radius-engine-1.1-disable-extra-portability.patch
# Use compat-lua
Patch3:		radius-engine-1.1-compat-lua.patch
BuildRequires:	liblua5.1-devel, libSDL-devel, libGL-devel, libGLU-devel
BuildRequires:	libphysfs-devel, libpng-devel, zlib-devel, libSDL_sound-devel
# I could not figure out a way to generate a patch to enable shared libraries 
# that worked right. All my attempts resulted in an environment where make, 
# when invoked, would re-run aclocal and automake. :P
# So, I'm just running autoreconf in the spec file. :P :P
BuildRequires:	autoconf-common, libtool-common

%description
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.

%package devel
Summary:	Development libraries and headers for Radius Engine
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries and headers for Radius Engine.

%prep
%setup -q
%patch0 -p1 -b .lua
%patch1 -p1 -b .shared
%patch2 -p1 -b .disable-extra-portability
%patch3 -p1 -b .compat-lua
# autoconf is being anal now.
mv configure.in configure.ac
autoreconf -if
chmod -x *.c *.h ChangeLog

%build
%configure --disable-static
%make_build

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%files
%doc ChangeLog
%{_libdir}/libradius-engine.so.*

%files devel
%{_includedir}/radius.h
%{_libdir}/libradius-engine.so
%{_libdir}/pkgconfig/radius-engine.pc

%changelog
* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8
- converted for ALT Linux by srpmconvert tools

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- update to new release by fcimport

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1_1.1
- Rebuilt with libpng15

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_3
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_2
- initial release by fcimport

