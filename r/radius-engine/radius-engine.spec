Name:		radius-engine
Version:	0.7
Release:	alt2_3
Summary:	A Lua based real-time 2D graphics game engine
Group:		System/Libraries
License:	MIT
URL:		http://radius-engine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-0.7-shared-libs.patch
BuildRequires:	liblua5-devel libSDL-devel libGL-devel libGLU-devel
BuildRequires:	libphysfs-devel libpng-devel zlib-devel libSDL_sound-devel
# I could not figure out a way to generate a patch to enable shared libraries 
# that worked right. All my attempts resulted in an environment where make, 
# when invoked, would re-run aclocal and automake. :P
# So, I'm just running autoreconf in the spec file. :P :P
BuildRequires:	autoconf libtool
Source44: import.info

%description
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.

%package devel
Summary:	Development libraries and headers for Radius Engine
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries and headers for Radius Engine.

%prep
%setup -q
%patch0 -p1 -b .lua
%patch1 -p1 -b .shared
autoreconf -if
chmod -x *.c *.h ChangeLog

%build
%configure --disable-static
make %{?_smp_mflags}

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

