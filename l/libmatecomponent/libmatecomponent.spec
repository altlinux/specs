# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/perl libpopt-devel pkgconfig(MateCORBA-CosNaming-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
%define _libexecdir %_prefix/libexec
Name:           libmatecomponent
Version:        1.4.0
Release:        alt1_14
Summary:        Libraries for matecomponent package of MATE-Desktop
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  mate-common
BuildRequires:  pkgconfig(MateCORBA-2.0)
BuildRequires:  popt-devel

Provides:       libmatecomponent-activation%{?_isa} = %{version}-%{release}
Provides:       libmatecomponent-activation = %{version}-%{release}

Patch0:         libmatecomponent-multishlib.patch

# momentary lapse of reason introducing a -libs subpkg here, sorry -- rex
Obsoletes: libmatecomponent-libs < 1.4.0-13
Provides:  libmatecomponent-libs = %{version}-%{release}
Provides:  libmatecomponent-libs%{?_isa} = %{version}-%{release}
Source44: import.info

%description
Libraries for matecomponent package of MATE-Desktop

%package devel
Group: Development/C
Summary:        Development libraries for libmatecomponent
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libmatecomponent-activation-devel%{?_isa} = %{version}-%{release}
Provides:       libmatecomponent-activation-devel = %{version}-%{release}

%description devel
Development libraries and includes for libmatecomponent.

%prep
%setup -q
%patch0 -p1 -b .multishlib
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

for serverfile in %{buildroot}%{_libdir}/matecomponent/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

#required for multilib installs /usr/lib/matecomponent/servers
mkdir -p %{buildroot}%{_prefix}/lib/matecomponent/servers

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config(noreplace) /etc/matecomponent-activation/matecomponent-activation-config.xml
%{_bindir}/matecomponent-activation-client
%{_bindir}/matecomponent-activation-run-query
%{_bindir}/matecomponent-echo-client-2
%{_bindir}/matecomponent-slay
%{_sbindir}/matecomponent-activation-sysconf
%{_libexecdir}/matecomponent-activation-server
%{_datadir}/man/man1/*
%{_datadir}/idl/matecomponent-2.0/
%{_datadir}/idl/matecomponent-activation-2.0/
%{_libdir}/libmatecomponent-2.so.0*
%{_libdir}/libmatecomponent-activation.so.4*
%{_libdir}/matecomponent-2.0/
%{_libdir}/matecomponent/
%dir %{_prefix}/lib/matecomponent/
%dir %{_prefix}/lib/matecomponent/servers/
%{_libdir}/matecorba-2.0/MateComponent_module.so

%files devel
%{_libdir}/libmatecomponent-2.so
%{_libdir}/pkgconfig/libmatecomponent-2.0.pc
%{_libdir}/pkgconfig/matecomponent-activation-2.0.pc
%{_libdir}/libmatecomponent-activation.so
%{_includedir}/libmatecomponent-2.0/
%{_includedir}/matecomponent-activation-2.0/
%{_datadir}/gtk-doc/html/libmatecomponent/
%{_datadir}/gtk-doc/html/matecomponent-activation/


%changelog
* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_14
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

