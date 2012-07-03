# BEGIN SourceDeps(oneline):
BuildRequires: libncurses-devel
# END SourceDeps(oneline)
# No FUSE on RHEL5
%if %{?el5:1}0
%define _without_fuse 1
%endif

Name:           afpfs-ng
Version:        0.8.1
Release:        alt2_9.3
Summary:        Apple Filing Protocol client

Group:          System/Base
License:        GPL+
URL:            http://alexthepuffin.googlepages.com/home
Source0:        http://downloads.sourceforge.net/afpfs-ng/%{name}-%{version}.tar.bz2
Patch0:         afpfs-ng-0.8.1-overflows.patch
Patch1:         afpfs-ng-0.8.1-pointer.patch

%{?!_without_fuse:BuildRequires: libfuse-devel}
BuildRequires: libgcrypt-devel libgmp-devel libgmp_cxx-devel libreadline-devel
Source44: import.info

%description
A command line client to access files exported from Mac OS system via
Apple Filing Protocol.
%{?!_without_fuse:The FUSE filesystem module for AFP is in fuse-afp package}


%if %{?!_without_fuse:1}0
%package -n fuse-afp
Summary:        FUSE driver for AFP filesystem
Group:          System/Base

%description -n fuse-afp
A FUSE file system server to access files exported from Mac OS system
via AppleTalk or TCP using Apple Filing Protocol.
The command line client for AFP is in fuse-afp package
%endif


%package devel
Summary:        Development files for afpfs-ng
Group:          Development/C
Requires:       %{name} = %{version}

%description devel
Library for dynamic linking and header files of afpfs-ng.


%prep
%setup -q
%patch0 -p1 -b .overflows
%patch1 -p1 -b .pointer


%build
# make would rebuild the autoconf infrastructure due to the following:
# Prerequisite `configure.ac' is newer than target `Makefile.in'.
# Prerequisite `aclocal.m4' is newer than target `Makefile.in'.
# Prerequisite `configure.ac' is newer than target `aclocal.m4'.
touch --reference aclocal.m4 configure.ac Makefile.in

%configure %{?_without_fuse:--disable-fuse} --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/afpfs-ng
cp -p include/* $RPM_BUILD_ROOT%{_includedir}/afpfs-ng


%files
%{_bindir}/afpcmd
%{_bindir}/afpgetstatus
%{_mandir}/man1/afpcmd.1*
%{_mandir}/man1/afpgetstatus.1*
%{_libdir}/*.so.*
%doc COPYING AUTHORS ChangeLog docs/README docs/performance docs/FEATURES.txt docs/REPORTING-BUGS.txt


%if %{?!_without_fuse:1}0
%files -n fuse-afp
%{_bindir}/afp_client
%{_bindir}/afpfs
%{_bindir}/afpfsd
%{_bindir}/mount_afp
%{_mandir}/man1/afp_client.1*
%{_mandir}/man1/afpfsd.1*
%{_mandir}/man1/mount_afp.1*
%doc COPYING AUTHORS ChangeLog
%endif


%files devel
%{_includedir}/afpfs-ng
%{_libdir}/*.so


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2_9.3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_9.3
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_8.3
- update to new release by fcimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_8
- initial release by fcimport

