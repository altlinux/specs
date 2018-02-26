# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/ld /usr/bin/pkg-config /usr/bin/swig /usr/bin/valgrind cppunit-devel gcc-c++ glib2-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel libgcrypt-devel libglibmm-devel libgmp-devel libgpgme-devel libhocr-devel libhspell-devel libifp-devel libmpfr-devel liboggz-devel libreadline-devel libspeex-devel libtiff-devel libusb-compat-devel libuuid-devel libvorbis-devel libxml2-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) python-module-pygobject-devel pkgconfig(pygtk-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libmatheval
Version:        1.1.8
Release:        alt1_2.1
Summary:        Library for parsing and evaluating symbolic expressions input as text

Group:          System/Libraries
License:        GPLv3+
URL:            http://www.gnu.org/software/libmatheval/
Source0:        http://ftp.gnu.org/gnu/libmatheval/libmatheval-%{version}.tar.gz


BuildRequires:  gcc-fortran guile18-devel bison flex flex texinfo
Source44: import.info


%description
GNU libmatheval is a library (callable from C and Fortran) to parse
and evaluate symbolic expressions input as text.  It supports
expressions in any number of variables of arbitrary names, decimal and
symbolic constants, basic unary and binary operators, and elementary
mathematical functions.  In addition to parsing and evaluation,
libmatheval can also compute symbolic derivatives and output
expressions to strings.

%package devel
Summary:        Development files for libmatheval
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libmatheval.


%prep
%setup -q

%build
%configure F77=gfortran --disable-static
make %{?_smp_mflags}

%check
make check ||:


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%files
%doc COPYING AUTHORS README
%{_libdir}/*.so.*

%files devel
%doc NEWS 
%{_includedir}/*
%{_libdir}/*.so
%{_infodir}/libmatheval.info*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.8-alt1_2.1
- Fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_6
- initial import by fcimport

