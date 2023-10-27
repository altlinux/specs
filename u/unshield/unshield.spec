# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name unshield
%define major	0
%define libname	lib%{name}%{major}
%define devname	lib%{name}-devel

Name:		unshield
Version:	1.4.3
Release:	alt1_4
Summary:	Install InstallShield applications on a Pocket PC
Group:		File tools
License:	MIT
URL:		http://synce.sourceforge.net/
Source0:	https://github.com/twogood/unshield/archive/%{version}/unshield-%{version}.tar.gz
# Originally from openSUSE:
Patch0100:	libconvert_utf_static.patch
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	ccmake cmake ctest
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

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Provides: libunshield = %EVR
Conflicts: libunshield < 1.4.3-alt1_3
Obsoletes: libunshield < 1.4.3-alt1_3


%description -n %{libname}
This package contains the shared libraries for %{name}.

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -q
%patch100 -p1


%build
%{mageia_cmake}
%mageia_cmake_build

%install
%mageia_cmake_install

find %{buildroot} -name "*.la" -delete

%files
%doc README.md
%doc --no-dereference LICENSE
%{_bindir}/unshield
%{_mandir}/man1/unshield.1*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_includedir}/lib%{name}.h
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Fri Oct 27 2023 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt1_4
- mageia re-import
- switched to shared libs policy

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_7
- update to new release by fcimport

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


