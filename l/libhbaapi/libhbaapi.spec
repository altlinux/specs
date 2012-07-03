# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/pkg-config /usr/bin/valgrind cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel libglibmm-devel libgmp-devel libmpfr-devel liboggz-devel libreadline-devel libspeex-devel libuuid-devel libvorbis-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define buildversion 2.2.5

Name:           libhbaapi
Version:        2.2
Release:        alt2_14
Summary:        SNIA HBAAPI library
Group:          System/Libraries
License:        SNIA
URL:            http://sourceforge.net/projects/hbaapi/
Source0:        http://downloads.sourceforge.net/hbaapi/hbaapi_src_%{version}.tgz
# This source was cloned from upstream git. To create tarball, run:
# git clone git://open-fcoe.org/openfc/hbaapi_build.git
# cd hbaapi_build
# git archive v%{buildversion} > ../hbaapi_build.tar
# cd .. && gzip hbaapi_build.tar
Source1:        hbaapi_build_%{buildversion}.tar.gz
Patch0:         libhbaapi-2.2-9-dl-linking.patch
BuildRequires:  automake libtool
Source44: import.info

%description
The SNIA HBA API library. C-level project to manage
Fibre Channel Host Bus Adapters.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n hbaapi_src_2.2
%setup -q -T -D -a 1 -n hbaapi_src_2.2
%patch0 -p1 -b .ld-linking

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc readme.txt COPYING
%config(noreplace) %{_sysconfdir}/hba.conf
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_14
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_12
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_12
- initial import by fcimport

