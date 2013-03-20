%define oldname unshield
Name:           libunshield
Version:        0.6
Release:        alt3_6
Summary:        Install InstallShield applications on a Pocket PC

Group:          Communications
License:        MIT
URL:            http://synce.sourceforge.net/
Source0:        http://dl.sf.net/synce/unshield-0.6.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  libtool
Source44: import.info

%description
To install a Pocket PC application remotely, an installable
Microsoft Cabinet File is copied to the /Windows/AppMgr/Install
directory on the PDA and then the wceload.exe is executed to
perform the actual install. That is a very simple procedure.

Unfortunately, many applications for Pocket PC are distributed as
InstallShield installers for Microsoft Windows, and not as
individual Microsoft Cabinet Files. That is very impractical for
users of other operating systems, such as Linux or FreeBSD.

%package devel
Group:          Development/C
Summary:        Files needed for software development with %{oldname}
Requires:       libunshield = %{version}-%{release}

%description devel
The %{oldname}-devel package contains the files needed for development with
%{oldname}

%prep
%setup -n %{oldname}-%{version} -q

%build
%configure --disable-static --disable-rpath
make LIBTOOL=%{_bindir}/libtool %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libunshield.{,l}a

%files
%doc README LICENSE
%{_bindir}/unshield
%{_mandir}/man1/unshield.1*
%{_libdir}/libunshield.so.*

%files devel
%{_libdir}/libunshield.so
%{_includedir}/libunshield.h
%{_libdir}/pkgconfig/libunshield.pc

%changelog
* Wed Mar 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_6
- restored in Sisyphus as fc import

* Thu Jan 19 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt3
- drop RPATH
- minor spec cleanup

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt2
- rebuild with new openssl

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat Dec 08 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt3
- update to SVN 20071207 version

* Fri Oct 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt2
- fix #13081 (linking with crypto lib), thanks to Slava Semushin

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt1
- 0.5

* Fri Sep 03 2004 Michael Shigorin <mike@altlinux.ru> 0.4-alt1
- built for ALT Linux (synce-kde dependency)


