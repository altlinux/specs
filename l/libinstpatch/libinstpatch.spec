# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(pygtk-2.0) pkgconfig(sndfile) python-module-pygobject-devel
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
Name:		libinstpatch
Summary:	MIDI instrument patch library
Version:	1.0.0
Release:	alt3_11.20110806svn386
URL:		http://www.swamiproject.org/
License:	LGPLv2+
# Fetch source via
# sh libinstpatch-snapshot.sh 386
Source0:	libinstpatch-%{version}-svn386.tar.bz2
# script to download sources and make tarball from svn
Source1:	libinstpatch-snapshot.sh
# .pc file fixes. Patch sent upstream via their mailing list
Patch0:		libinstpatch-cmake-fixes.patch

BuildRequires: ctest cmake
BuildRequires:	glib2-devel
BuildRequires:	libsndfile-devel
Source44: import.info
 

%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument "patch" files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.


%package devel
Group: Development/C
Summary:	Development package for %{name}
Requires:	%{name}%{?_isa} = %{version}

%description devel
This package includes the development libraries and header files for
%{name}.


%prep
%setup -q
%patch0 -p1 -b .pkgconfig


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}*.so.*


%files devel
%doc examples/create_sf2.c
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc


%changelog
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

