%def_disable snapshot
%define api_ver 1.0
%define sover 2
# disabled by default
%def_disable gtk_doc
%def_disable introspection
%def_disable check

Name: libinstpatch
Version: 1.1.6
Release: alt1

Summary: MIDI instrument patch library
Group: System/Libraries
License: LGPL-2.1-only
Url: https://www.swamiproject.org/

%if_disabled snapshot
Source: https://github.com/swami/%name/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/swami/libinstpatch
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: astyle cmake libgio-devel libsndfile-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: ctest}

%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument "patch" files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: %name = %EVR

%description devel
This package includes the development libraries and header files for
%name.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
-DCMAKE_BUILD_TYPE="Release" \
%{?_enable_gtk_doc:-DGTKDOC_ENABLED=TRUE} \
%{?_enable_introspection:-DINTROSPECTION_ENABLED=TRUE}
%nil
%cmake_build

%install
%cmakeinstall_std

%check
%make -C BUILD test

%files
%_libdir/%name-%api_ver.so.*
%doc AUTHORS ChangeLog README.md COPYING

%files devel
%_includedir/%name-%sover/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%doc examples/*.c

%changelog
* Tue Jan 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Apr 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Fri Mar 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3 (ALT #38227)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_14.20110806svn386
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_12.20110806svn386
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_11.20110806svn386
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_10.20110806svn386
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_9.20110806svn386
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_8.20110806svn386
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_7.20110806svn386
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_6.20110806svn386
- update to new release by fcimport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_5.20110806svn386
- update to new release by fcimport

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_4.20110806svn386
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4.20110806svn386
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3.20110806svn386
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3.20110806svn386
- initial import by fcimport

