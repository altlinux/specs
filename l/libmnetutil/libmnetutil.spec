Epoch: 51104
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		Minisip library providing various C++ network classes
Name:			libmnetutil
Version:		0.8.0
Release:		alt6_0.3.20100629svn3775
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3775  svn://svn.minisip.org/minisip/trunk/libmnetutil libmnetutil-0.8.0
# tar cjf libmnetutil-0.8.0.tar.bz2 libmnetutil-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
Patch0:			libmnetutil-0001-Remove-bundled-udns.patch
Patch1:			libmnetutil-0.8.0-alt-build.patch
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libmutil-devel >= 0.8.0
BuildRequires:		libudns-devel
Source44: import.info

%description
libmnetutil is a library providing convenient C++ network utilities
(UDP/TCP/TLS sockets, IP addresses). It is used by the minisip project.

%package devel
Summary:		Development files for the libmnetutil library
Group:			Development/C
Requires:		%{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:		automake


%description devel
This package contains the development files for library %{name}.

%prep
%setup -q
%patch0 -p1 -b .udns
%patch1 -p2

%build
%add_optflags -std=c++14
sh ./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
# Removed installed examples
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc AUTHORS README COPYING.LIB
%{_libdir}/*.so.*

%files devel
%doc examples/tcpclient.cpp
%doc examples/tcpserver.cpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%{_datadir}/aclocal/*.m4


%changelog
* Thu Sep 30 2021 Igor Vlasenko <viy@altlinux.org> 51104:0.8.0-alt6_0.3.20100629svn3775
- fixed build with gcc11

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt5_0.3.20100629svn3775.qa1
- NMU: applied repocop patch

* Fri Sep 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 51104:0.8.0-alt5_0.3.20100629svn3775
- NMU: fixed build with new automake and gcc.

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt4_0.3.20100629svn3775
- gcc46 build

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt3_0.3.20100629svn3775
- applied repocop patches

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.3.20100629svn3775
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt1_0.3.20100629svn3775
- initial import by fcimport

