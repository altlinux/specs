Serial: 51104
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libmutil-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		Minisip library providing various C++ utility classes
Name:			libmutil
Version:		0.8.0
Release:		alt2_0.7.20100319svn3760.1
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3760  svn://svn.minisip.org/minisip/trunk/libmutil libmutil-0.8.0
# tar cjf libmutil-0.8.0.tar.bz2 libmutil-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libltdl7-devel
Source44: import.info

%description
libmutil is a library providing convenient C++ utilities (threads, mutexes,
memory object management, ...). It is used by the minisip project.

%package devel
Summary:		Development files for the libmutil library
# %%{_datadir}/aclocal/winfuncs.m4 is under GPLv2+
License:		LGPLv2+ and GPLv2+
Group:			Development/C
Requires:		libmutil = %{version}-%{release}
Requires:		automake


%description devel
This package contains the development files for library %{name}.

%prep
%setup -q
# Fix DOS line-endings
for f in examples/*; do
	sed "s|\r||g" $f > $f.new
	touch -r $f $f.new
	mv $f.new $f
done


%build
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
%doc examples/mutextest.cpp
%doc examples/semaphoretest.cpp
%doc examples/threadtest.cpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/aclocal/*.m4


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.7.20100319svn3760.1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.6.20100319svn3760.1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.5.20100319svn3760.1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt1_0.5.20100319svn3760.1
- initial import by fcimport

