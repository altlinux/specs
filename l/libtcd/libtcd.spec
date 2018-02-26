# BEGIN SourceDeps(oneline):
BuildRequires: scheme48-prescheme
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%global		postver		-r2
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		2.2.5

%global		fedorarel	4
%global		rpmrel		%{fedorarel}%{?postver:.%postrpmver}

Name:		libtcd
Version:	%{mainver}
Release:	alt3_4.%(echo "-r2" | sed -e 's|-|.|g' | sed -e 's|^\.||')
Summary:	Tide Constituent Database Library

Group:		System/Libraries
License:	Public Domain
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/%{name}-%{version}%{?postver}.tar.bz2
Source44: import.info


%description
libtcd provides a software API for reading and writing Tide
Constituent Database (TCD) files.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	libtcd = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags} -k

%install
make \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	install

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%doc *.html

%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt3_4.%(echo "-r2" | sed -e 's|-|.|g' | sed -e 's|^\.||')
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt2_4.%(echo "-r2" | sed -e 's|-|.|g' | sed -e 's|^\.||')
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_2
- initial import by fcimport

