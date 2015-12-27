Name:		ftplib
Version:	4.0
Release:	alt1_1
Summary:	Library of FTP routines
Group:		System/Libraries
License:	LGPLv2+
URL:		http://nbpfaus.net/~pfau/ftplib/
Source0:	http://nbpfaus.net/~pfau/ftplib/%{name}-%{version}.tar.gz
Patch0:		ftplib-3.1-1-modernize.patch
Source44: import.info

%description
ftplib is a set of routines that implement the FTP protocol. They allow 
applications to create and access remote files through function calls 
instead of needing to fork and exec an interactive ftp client program.

%package devel
Summary:	Development files for ftplib
Group:		Development/C
Requires:	ftplib = %{version}-%{release}

%description devel
Development libraries and headers for ftplib.

%package -n qftp
Summary:	Simple ftp client application
Group:		Networking/WWW
License:	GPLv2+

%description -n qftp
Command line driven ftp file transfer program using ftplib.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .modern

%build
cd src/
make %{?_smp_mflags} DEBUG="$RPM_OPT_FLAGS"

%install
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cd src/
make DESTDIR=$RPM_BUILD_ROOT LIBDIR="%{_libdir}" install

cd ${RPM_BUILD_ROOT}%{_libdir}
chmod +x libftp.so.4.0
ln -sf libftp.so.4.0 libftp.so.4
ln -sf libftp.so.4 libftp.so

cd ${RPM_BUILD_ROOT}%{_bindir}
for f in ftpdir ftpget ftplist ftprm ftpsend; do
	ln -s qftp $f
done

%files
%doc CHANGES
%doc LICENSE
%{_libdir}/libftp*.so.*

%files devel
%doc additional_rfcs README.ftplib* RFC959.txt html/
%{_includedir}/ftplib.h
%{_libdir}/libftp*.so

%files -n qftp
%doc README.qftp
%{_bindir}/ftpdir
%{_bindir}/ftpget
%{_bindir}/ftplist
%{_bindir}/ftprm
%{_bindir}/ftpsend
%{_bindir}/qftp

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_8
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_7
- initial release by fcimport

