# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%global veryear 2007
%global vermon  10
%global verday  18
%global namesq3 libsq3
Name:           libsqlite3x
Version:        %{veryear}%{vermon}%{verday}
Release:        alt3_11
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine

Group:          System/Libraries
# fix license tag: https://bugzilla.redhat.com/show_bug.cgi?id=491618
License:        zlib
URL:            http://www.wanderinghorse.net/computing/sqlite/
Source0:        http://www.wanderinghorse.net/computing/sqlite/%{name}-%{veryear}.%{vermon}.%{verday}.tar.gz
Source1:        libsqlite3x-autotools.tar.gz
Patch1:         libsqlite3x-prep.patch
Patch2:         libsqlite3x-includes.patch

BuildRequires:  libsqlite3-devel dos2unix automake libtool doxygen
Source44: import.info

%description
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libsqlite3x = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     %{namesq3}
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine
Group:          Development/C
Requires:       libsq3 = %{version}-%{release}

%description -n %{namesq3}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

%package -n     %{namesq3}-devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libsq3 = %{version}-%{release}

%description -n %{namesq3}-devel
The %{namesq3}-devel package contains libraries and header files for
developing applications that use %{namesq3}.

%prep
%setup -q -n %{name}-%{veryear}.%{vermon}.%{verday} -a 1
dos2unix *.hpp *.cpp
%patch1 -p0 -b .prep
%patch2 -p0 -b .incl
aclocal
libtoolize -f
autoheader
autoconf
automake -a -c
%configure --disable-static
iconv -f iso8859-1 -t utf-8  < README > R
mv R README
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%build
make
make doc
make doc-sq3

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS Doxygen-index.txt
%{_libdir}/libsqlite3x.so.*

%files devel
%doc README doc/html
%{_includedir}/sqlite3x
%{_libdir}/libsqlite3x.so
%{_libdir}/pkgconfig/libsqlite3x.pc

%files -n %{namesq3}
%doc AUTHORS Doxygen-index.txt
%{_libdir}/libsq3.so.*

%files -n %{namesq3}-devel
%doc README doc-sq3/html
%{_includedir}/sq3
%{_libdir}/libsq3.so
%{_libdir}/pkgconfig/libsq3.pc

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 20071018-alt3_11
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20071018-alt2_11
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 20071018-alt2_10
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 20071018-alt1_10
- initial import by fcimport

