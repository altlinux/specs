# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: chrpath
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           lib3ds
Version:        1.3.0
Release:        alt2_39

Summary:        3D Studio file format library

License:        LGPL-2.1-or-later
URL:            http://lib3ds.sourceforge.net
Source:         http://downloads.sourceforge.net/lib3ds/lib3ds-%{version}.zip
# Extracted from Debian's lib3ds_1.3.0-1.diff.gz
Patch0:         lib3ds-1.3.0-lib3ds-file.h.diff
# Address https://bugzilla.redhat.com/show_bug.cgi?id=633475
Patch1:         lib3ds-1.3.0-lib3ds-mesh.c.diff

Patch2:         lib3ds-1.2.0-pkgconfig.diff

BuildRequires:  gcc
# RHBZ 1987639: rpm corrupts older libtool sources
BuildRequires: autoconf automake libtool
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
Group: Graphics
Summary:        %summary

%description    tools
Some tools to process 3ds files.

%files          tools
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_bindir}/3dsdump
%{_mandir}/man1/3dsdump.1*

%package        devel
Group: Development/Other
Summary:        %summary
Requires:	pkgconfig
Requires:	lib3ds = %{version}-%{release}

%description    devel
Development files for lib3ds


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

autoreconf -fi

%build
%configure  --disable-static

%{make_build}

sed -e 's,@prefix@,%{_prefix},' \
  -e 's,@exec_prefix@,%{_exec_prefix},' \
  -e 's,@libdir@,%{_libdir},' \
  -e 's,@includedir@,%{_includedir},' \
  -e 's,@VERSION@,%{version},' \
  lib3ds.pc.in > lib3ds.pc

%install
%{makeinstall_std}

install -d ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install lib3ds.pc -m 0644 ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

## Remove libtool archive
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done


%files
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_libdir}/*.so.*




%files devel
%{_bindir}/lib3ds-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib3ds.pc
%{_mandir}/man1/lib3ds-config.1*
%{_includedir}/lib3ds
%{_datadir}/aclocal/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.3.0-alt2_39
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 1.3.0-alt2_36
- update to new release by fcimport

* Wed Oct 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_28
- converted for ALT Linux by srpmconvert tools

* Sun Jun 24 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt2_25.1
- Fix build for aarch64

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_25
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_23
- update to new release by fcimport

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

