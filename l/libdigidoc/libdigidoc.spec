# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libdigidoc
Version:        2.7.0
Release:        alt2_4
Summary:        Library for handling digitally signed documents

Group:          System/Libraries
License:        LGPLv2+
URL:            http://code.google.com/p/esteid/
Source0:        http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:  ctest cmake
BuildRequires:  libxml2-devel
BuildRequires:  libssl-devel
BuildRequires:  zlib-devel
Requires:       opensc
Source44: import.info

%description
libDigiDoc is a library implementing a subset of the XAdES digital
signature standard on top of Estonian specific .ddoc container format.
It allows to create, sign, verify, and modify digidoc XML containers.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libdigidoc = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}


%files
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/digidoc.conf
%{_bindir}/cdigidoc
%{_libdir}/*.so.*
%{_datadir}/libdigidoc/

%files devel
%{_includedir}/libdigidoc/
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/*.so

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt2_4
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_2
- initial import by fcimport

