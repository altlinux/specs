# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname varconf
Name:           libvarconf
Version:        0.6.7
Release:        alt1_3
Summary:        Configuration library used by WorldForge clients

Group:          Development/C++
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/varconf
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2

BuildRequires:  libsigc++2-devel
Source44: import.info
Provides: varconf = %{version}-%{release}

%description
Varconf is a configuration library intended for all applications. It manages
configuration data in files, command line arguments, and is used by most
WorldForge components.


%package devel
Summary: Development files for varconf library
Group:   Development/C++
Requires: libvarconf = %{version}-%{release}
Provides: varconf-devel = %{version}-%{release}


%description devel
Development libraries and headers for linking against the varconf library.


%prep
%setup -q -n %{oldname}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

## cleaning up redundant docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}-%{version}

%check
make %{?_smp_mflags} check
cd tests ; ./conftest < conf.cfg

%files
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%{_libdir}/lib%{oldname}-1.0.so.*


%files devel
%{_includedir}/%{oldname}-1.0
%{_libdir}/lib%{oldname}-1.0.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_2
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_1
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_2
- initial release by fcimport

