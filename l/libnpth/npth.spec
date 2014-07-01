%add_optflags %optflags_shared
%define oldname npth
Summary:        The New GNU Portable Threads library
Name:           libnpth
Version:        0.91
Release:        alt1_7
# software uses dual licensing (or both in parallel)
License:        LGPLv3+ or GPLv2+ or (LGPLv3+ and GPLv2+)
Group:          System/Libraries
URL:            ftp://ftp.gnupg.org/gcrypt/npth/
Source:         ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2.sig
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source2:        npth-config.1
Source44: import.info
Provides: npth = %{version}-%{release}

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth.  It has been designed as a replacement of
GNU Pth for non-ancient operating systems.  In contrast to GNU Pth is is
based on the system's standard threads implementation.  Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package devel
Summary:        Development headers and libraries for GNU nPth
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: npth-devel = %{version}-%{release}

%description devel
Development headers and libraries for GNU Pth.

%prep
%setup -n %{oldname}-%{version} -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL='install -p'
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -p -c -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_mandir}/man1/
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la


%check
make check


%files
%doc AUTHORS COPYING COPYING.LESSER ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/*/*
%{_datadir}/aclocal/*


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_6
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- initial fc import

