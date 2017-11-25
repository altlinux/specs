# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libpolyxmass
Version:        0.9.1
Release:        alt4_18
Summary:        Polymer chemistry-related functionalities

Group:          System/Libraries
License:        GPLv2+
URL:            http://www.polyxmass.org
Source0:        http://www.polyxmass.org/libpolyxmass/downloads/0.9.1/libpolyxmass-0.9.1.tar.gz
# Fix up autotool-sources and generated files
# Note: This package's auto*files are too old and incompatible to automake > 1.13.4
Patch0:         libpolyxmass-x86_64.patch

BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
Source44: import.info
Patch33: libpolyxmass-0.9.1-alt-no-g_memmove.patch

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
Group:    Development/Other
Requires: %{name} = %{version}-%{release}
Requires: pkg-config
Requires: libgio

%description devel
The %{name}-devel package contains the files needed for development with
%{name}

%prep
%setup -q
%patch0 -p1
# Fix up time stamps to prevent the autotools from being re-run
touch -r aclocal.m4 configure configure.in Makefile.in Makefile.am
%patch33 -p1

%build
export CFLAGS="${RPM_OPT_FLAGS} -Wno-error"
%configure --disable-static
%make_build


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
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt4_18
- fixed build

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt4_11
- Fixed build

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt3_11.1
- Fixed build

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_9
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_8
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_7
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_7
- initial import by fcimport

