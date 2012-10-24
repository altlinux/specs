# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/pkg-config libICE-devel libSM-devel libpopt-devel pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(mateconf-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define libxml2_version 2.5
%define mate_corba_version 1.1.0
%define libmatecomponent_version 1.1.0
%define libmatecanvas_version 1.1.0
%define libmate_version 1.1.2
%define libart_lgpl_version 2.3.8
%define gtk2_version 2.6.0
%define libglade2_version 2.0.0
%define glib2_version 2.6.0

%define po_package libmatecomponentui

Summary: libmatecomponent user interface components
Name:    libmatecomponentui
Version: 1.4.0
Release: alt1_1.1
URL:     http://pub.mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: LGPLv2+
Group:   System/Libraries

Requires: mate-corba >= %{mate_corba_version}

BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: mate-corba-devel >= %{mate_corba_version}
BuildRequires: libmatecomponent-devel >= %{libmatecomponent_version}
BuildRequires: libmatecanvas-devel >= %{libmatecanvas_version}
BuildRequires: libmate-devel >= %{libmate_version}
BuildRequires: libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libglade2-devel >= %{libglade2_version}
BuildRequires: intltool >= 0.14-1
BuildRequires: libtool >= 1.4.2-12
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gettext
BuildRequires: mate-common


%description

libmatecomponentui is a component system based on CORBA, used by the MATE
desktop. libmatecomponentui contains the user interface related components
that come with libmatecomponent.

%package devel
Summary: Libraries and headers for libmatecomponentui
Group: Development/C
License: GPLv2+ and LGPLv2+
Requires: libmatecomponentui = %{version}-%{release}

%description devel

libmatecomponentui is a component system based on CORBA, used by the MATE desktop.
libmatecomponentui contains GUI components that come with libmatecomponent.

This package contains header files used to compile programs that
use libmatecomponentui.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la
#rm -f $RPM_BUILD_ROOT%{_datadir}/applications/matecomponent-browser.desktop

for serverfile in $RPM_BUILD_ROOT%{_libdir}/matecomponent/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done


%find_lang %{po_package}

%files -f %{po_package}.lang
%doc COPYING.LIB NEWS README
%{_libdir}/lib*.so.*
%{_libdir}/libglade/2.0/*.so
%{_libdir}/matecomponent/servers/*
%{_datadir}/applications/matecomponent-browser.desktop
%{_datadir}/mate-2.0/ui/*

%files devel
%doc COPYING COPYING.LIB
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/*
%{_libdir}/matecomponent-2.0
%{_datadir}/gtk-doc/html/libmatecomponentui/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

