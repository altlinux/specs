# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/pkg-config /usr/bin/valgrind cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel libgmp-devel libmpfr-devel liboggz-devel libreadline-devel libspeex-devel libuuid-devel libvorbis-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libgcroots
Version:	0.2.3
Release:	alt2_2
License:	MIT
URL:		http://code.google.com/p/sigscheme/wiki/libgcroots

Source0:	http://sigscheme.googlecode.com/files/%{name}-%{version}.tar.bz2


Summary:	Roots acquisition library for Garbage Collector
Group:		Development/C
Source44: import.info

%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.
This library encourages to have own GC such as for small-footprint,
some application-specific optimizations, just learning or to test
experimental ideas.

%package devel
Summary:	Development files for libgcroots
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This package contains a header file and development library to help you
to develop any own GC.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install

make install DESTDIR=$RPM_BUILD_ROOT

# Remove unnecessary files
rmdir $RPM_BUILD_ROOT%{_includedir}/libgcroots
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc COPYING ChangeLog README
%{_libdir}/libgcroots.so.*

%files devel
%doc COPYING ChangeLog README
%{_includedir}/gcroots.h
%{_libdir}/libgcroots.so
%{_libdir}/pkgconfig/gcroots.pc

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_1
- initial import by fcimport

