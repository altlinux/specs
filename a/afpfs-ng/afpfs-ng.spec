Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libncurses-devel
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           afpfs-ng
Version:        0.8.1
Release:        alt3_41
Summary:        Apple Filing Protocol client


# by default build with the fuse module
# rpmbuild --rebuild afpfs-ng.src.rpm --without fuse
%bcond_without     fuse


License:        GPL+
URL:            http://alexthepuffin.googlepages.com/home
Source0:        http://downloads.sourceforge.net/afpfs-ng/%{name}-%{version}.tar.bz2
Patch0:         afpfs-ng-0.8.1-overflows.patch
Patch1:         afpfs-ng-0.8.1-pointer.patch
# Sent by e-mail to Alex deVries <alexthepuffin@gmail.com>
Patch2:         afpfs-ng-0.8.1-formatsec.patch
Patch3:         afpfs-ng-0.8.1-longoptions.patch
Patch4: afpfs-ng-c99.patch

%{?with_fuse:BuildRequires: libfuse-devel}
BuildRequires: gcc
BuildRequires: libgcrypt-devel libgmp-devel libgmpxx-devel readline-devel
BuildRequires: libtool
BuildRequires: autoconf
Source44: import.info


%description
A command line client to access files exported from Mac OS system via
Apple Filing Protocol.
%{?with_fuse:The FUSE filesystem module for AFP is in fuse-afp package}


%if 0%{?with_fuse}
%package -n fuse-afp
Group: System/Base
Summary:        FUSE driver for AFP filesystem

%description -n fuse-afp
A FUSE file system server to access files exported from Mac OS system
via AppleTalk or TCP using Apple Filing Protocol.
The command line client for AFP is in fuse-afp package
%endif


%package devel
Group: Development/Other
Summary:        Development files for afpfs-ng
Requires:       %{name} = %{version}

%description devel
Library for dynamic linking and header files of afpfs-ng.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

libtoolize
autoreconf

%build
# make would rebuild the autoconf infrastructure due to the following:
# Prerequisite `configure.ac' is newer than target `Makefile.in'.
# Prerequisite `aclocal.m4' is newer than target `Makefile.in'.
# Prerequisite `configure.ac' is newer than target `aclocal.m4'.
touch --reference aclocal.m4 configure.ac Makefile.in

export CFLAGS="${RPM_OPT_FLAGS} -fcommon" 
%configure %{?!with_fuse:--disable-fuse} --disable-static
%make_build


%install
%makeinstall_std
install -d %{buildroot}%{_includedir}/afpfs-ng
cp -p include/* %{buildroot}%{_includedir}/afpfs-ng
# libtool .la file works different in different versions of libtool, should not be packaged
[ -f %{buildroot}%{_libdir}/libafpclient.la ] && rm -f %{buildroot}%{_libdir}/libafpclient.la

%if ( 0%{?rhel} && 0%{?rhel} <= 7 )

%endif


%files
%doc --no-dereference COPYING
%{_bindir}/afpcmd
%{_bindir}/afpgetstatus
%{_mandir}/man1/afpcmd.1*
%{_mandir}/man1/afpgetstatus.1*
%{_libdir}/libafpclient.so.*
%doc AUTHORS ChangeLog docs/README docs/performance docs/FEATURES.txt docs/REPORTING-BUGS.txt


%if 0%{?with_fuse}
%files -n fuse-afp
%doc --no-dereference COPYING
%{_bindir}/afp_client
%{_bindir}/afpfs
%{_bindir}/afpfsd
%{_bindir}/mount_afp
%{_mandir}/man1/afp_client.1*
%{_mandir}/man1/afpfsd.1*
%{_mandir}/man1/mount_afp.1*
%doc AUTHORS ChangeLog
%endif


%files devel
%{_includedir}/afpfs-ng
%{_libdir}/*.so

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt3_41
- update to new release by fcimport

* Tue Nov 30 2021 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt3_37
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt3_35
- update to new release by fcimport

* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt3_34
- update to new release by fcimport

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_32
- fixed build

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_25
- rebuild with readline7

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_23
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_21
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_20
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_19
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_15
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_13.3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_12.3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_11.3
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_10.3
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2_10.3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2_9.3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_9.3
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_8.3
- update to new release by fcimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_8
- initial release by fcimport

