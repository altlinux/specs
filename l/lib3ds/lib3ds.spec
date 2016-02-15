# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           lib3ds
Version:        1.3.0
Release:        alt2_22

Summary:        3D Studio file format library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://lib3ds.sourceforge.net
Source:         http://downloads.sourceforge.net/lib3ds/lib3ds-%{version}.zip
# Extracted from Debian's lib3ds_1.3.0-1.diff.gz
Patch0:         lib3ds-1.3.0-lib3ds-file.h.diff
# Address https://bugzilla.redhat.com/show_bug.cgi?id=633475
Patch1:         lib3ds-1.3.0-lib3ds-mesh.c.diff

Patch2:         lib3ds-1.2.0-pkgconfig.diff

Patch3:         lib3ds-1.3.0-config.patch
Source44: import.info

%description
lib3ds is a free ANSI-C library for working with the popular "3ds" 3D model
format.

Supported platforms include GNU (autoconf, automake, libtool, make, GCC) on
Unix and Cygwin, and MS Visual C++ 6.0. lib3ds loads and saves Atmosphere
settings, Background settings, Shadow map settings, Viewport setting,
Materials, Cameras, Lights, Meshes, Hierarchy, Animation keyframes. It also
contains useful matrix, vector and quaternion mathematics tools. lib3ds
usually integrates well with OpenGL. In addition, some diagnostic and
conversion tools are included.

%package        tools
Summary:        %summary
Group:          Graphics

%description    tools
Some tools to process 3ds files.

%files          tools
%doc AUTHORS ChangeLog README
%doc COPYING
%{_bindir}/3dsdump
%{_mandir}/man1/3dsdump.1*

%package        devel
Summary:        %summary
Group:          Development/C
Requires:	pkgconfig
Requires:	lib3ds = %{version}

%description    devel
Development files for lib3ds


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%configure  --disable-static

make %{?_smp_mflags}

sed -e 's,@prefix@,%{_prefix},' \
  -e 's,@exec_prefix@,%{_exec_prefix},' \
  -e 's,@libdir@,%{_libdir},' \
  -e 's,@includedir@,%{_includedir},' \
  -e 's,@VERSION@,%{version},' \
  lib3ds.pc.in > lib3ds.pc

%install
make install DESTDIR=$RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install lib3ds.pc -m 0644 ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

## Remove libtool archive
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la


%files
%doc AUTHORS ChangeLog README
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/lib3ds-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib3ds.pc
%{_mandir}/man1/lib3ds-config.1*
%{_includedir}/lib3ds
%{_datadir}/aclocal/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_16
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_13
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_12
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_11
- spec cleanup thanks to ldv@

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_11
- initial release by fcimport

