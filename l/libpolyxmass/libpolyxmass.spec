# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libpolyxmass
Version:        0.9.1
Release:        alt3_8
Summary:        Polymer chemistry-related functionalities

Group:          System/Libraries
License:        GPLv2+
URL:            http://www.polyxmass.org
Source0:        http://www.polyxmass.org/libpolyxmass/downloads/0.9.1/libpolyxmass-0.9.1.tar.gz
Patch0:         libpolyxmass-x86_64.patch

BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: autoconf automake libtool
Source44: import.info

%description
libpolyxmass is a library that implements some housekeeping
functionalities and polymer chemistry-related functionalities that are
used in the other modules of the GNU polyxmass mass spectrometry
framework. It was born as the merge of the two libpxmutils and
libpxmchem libraries (last versions of these two libraries were for
both 0.7.0). This fact is still visible as the files do have either
"pxmutils-" or "pxmchem-" as prefix in their name. This nomenclature
is going to be maintained as it helps understanding the
functionalities that are housed in the different files of the new
library.

%package devel
Summary:  Files needed for software development with %{name}
Group:    Development/C
Requires: libpolyxmass = %{version}-%{release}

%description devel
The %{name}-devel package contains the files needed for development with
%{name}

%prep
%setup -q
%patch0

libtoolize
autoreconf

%build
export CFLAGS="${RPM_OPT_FLAGS} -Wno-error"
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=${RPM_BUILD_ROOT}

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*
%{_datadir}/man/man7/*
%exclude %{_datadir}/doc

%files devel
%{_includedir}/libpolyxmass
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpolyxmass.pc

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_8
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_7
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_7
- initial import by fcimport

