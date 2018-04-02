# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 3
%define libname     librpcsecgss%{major}
%define develname	librpcsecgss-devel

Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Name:		librpcsecgss
Version:	0.19
Release:	alt1.qa1_9
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	libgssglue-devel
Source44: import.info

%description
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

%package -n	%{libname}
Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Group:		System/Libraries

%description -n	%{libname}
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

%package -n	%{develname}
Summary:	Static library and header files for the librpcsecgss library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	rpcsecgss-devel = %{version}-%{release}
Obsoletes:	librpcsecgss1-devel
Obsoletes:	librpcsecgss2-devel
Obsoletes:	librpcsecgss3-devel

%description -n	%{develname}
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

This package contains the static librpcsecgss library and its
header files.

%prep
%setup -q -n librpcsecgss-%{version}

%build
%configure --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files  -n %{develname}
%{_includedir}/rpcsecgss
%{_libdir}/*.so
%{_libdir}/pkgconfig/librpcsecgss.pc


%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.qa1_9
- new version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.19-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Nov 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19-alt1
- 0.19 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18-alt1
- 0.18 released

* Sat Oct 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17-alt1
- 0.17 released

* Wed Sep  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt2
- CVE-2007-3999 fixed

* Sun Dec  3 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt1
- 0.14 released

* Mon Jul 17 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt1
- 0.13 released

* Sun Mar 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt1
- 0.8 released

* Mon Jan 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt2
- fixed build for x86_64

* Sat Oct 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- 0.6 released

