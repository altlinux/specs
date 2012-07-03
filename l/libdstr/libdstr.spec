# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison cppunit-devel gcc-c++ libuuid-devel zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libdstr
Version:	20080124
Release:	alt2_5
Summary:	Dave's String class

Group:		System/Libraries
License:	Public Domain
URL:		http://www.flaterco.com/util/index.html
Source0:	http://www.flaterco.com/util/%{name}-%{version}.tar.bz2
Source44: import.info

%description
libdstr is a library containing Dstr, Dave's String class.


%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="%{__install} -c -p"

# Upstream uses some odd header file name,
# changing...
%{__mv} \
	$RPM_BUILD_ROOT%{_includedir}/Dstr \
	$RPM_BUILD_ROOT%{_includedir}/Dstr.h

find $RPM_BUILD_ROOT -name '*.la' \
	-exec %{__rm} -f {} ';'

%files
%doc	AUTHORS
%doc	COPYING
%doc	ChangeLog
%doc	README

%{_libdir}/lib*.so.*

%files devel

%{_includedir}/*.h
%{_libdir}/lib*.so


%changelog
* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 20080124-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 20080124-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 20080124-alt1_4
- initial import by fcimport

