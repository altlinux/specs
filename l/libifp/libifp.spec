# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/pkg-config /usr/bin/swig /usr/bin/valgrind cppunit-devel gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel libglibmm-devel libgmp-devel libhocr-devel libhspell-devel libifp-devel libmpfr-devel liboggz-devel libreadline-devel libspeex-devel libtiff-devel libuuid-devel libvorbis-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
BuildRequires: gcc-c++
%add_optflags %optflags_shared
Name:           libifp
Version:        1.0.0.2
Release:        alt2_11
Summary:        A general-purpose library-driver for iRiver's iFP portable audio players

Group:          System/Base
License:        GPLv2
URL:            http://ifp-driver.sourceforge.net/
Source0:        http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
Source1:        libifp.hotplug
Source2:        10-libifp.rules

BuildRequires:  libusb-compat-devel libusb-devel doxygen
Source44: import.info

%description
libifp is a general-purpose library-driver for iRiver's iFP (flash-based)
portable audio players. The source code is pure C and is fairly portable.

Also included is a console app that uses the library.

%package        devel
Summary:        Headers and libraries for developing with libifp
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries for developing apps that use
libifp.

%prep
%setup -q

%build
%configure --with-libusb --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
install -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/sbin/libifp-hotplug
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/10-libifp.rules
# kill rpath
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
	chrpath -d $i ||:
done
	    

%files
%doc ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/*.so.*
/sbin/*
%{_sysconfdir}/udev/rules.d/*.rules

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_11
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_10
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt1_10
- initial import by fcimport

