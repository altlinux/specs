# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/valgrind imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libfreetype-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libcmml
Version:        0.9.1
Release:        alt2_10
Summary:        Library for handling Continuous Media Markup Language

Group:          System/Libraries
License:        BSD
URL:		http://www.annodex.net/
Source:		http://www.annodex.net/software/libcmml/download/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	libexpat-devel

# libtool
BuildRequires:	gcc-c++
Source44: import.info
Patch33: libcmml-0.9.1-alt-link-libm.patch

%description
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

%package devel
Summary:	Files needed for development using libcmml
Group:          Development/C
Requires:       libcmml = %{version}

%description devel
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

This package contains the header files and documentation needed for
development using libcmml.

%prep
%setup -q -n %{name}-%{version}
%patch33 -p1

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make docdir=/doxygen DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/doxygen .

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# remove doxygen build stamp; fixed in upstream CVS
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/libcmml/doxygen-build.stamp

%files
%doc AUTHORS ChangeLog COPYING NEWS README
# zero length NEWS file
# %doc NEWS
%{_libdir}/libcmml.so.*
%{_bindir}/cmml*

%files devel
%doc doxygen/html
%{_libdir}/libcmml.so
%{_libdir}/pkgconfig/cmml.pc
%{_includedir}/cmml.h

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_10
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_9
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_9
- initial import by fcimport

