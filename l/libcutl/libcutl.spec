Group: System/Libraries
%add_optflags %optflags_shared
%define fedora 34
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# The base of the version (just major and minor without point)
%global base_version 1.10

Name:           libcutl
Version:        %{base_version}.0
Release:        alt1_21
Summary:        C++ utility library from Code Synthesis
License:        MIT
URL:            http://www.codesynthesis.com/projects/libcutl/
Source0:        http://www.codesynthesis.com/download/libcutl/%{base_version}/%{name}-%{version}.tar.bz2
Patch0:         libcutl_no_boost_license.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?fedora} && 0%{?fedora} < 28
# Use the system Boost instead of the internal one
%global external_boost --with-external-boost
BuildRequires: boost-complete
%endif

%if !0%{?external_boost}
Provides: bundled(boost) = 1.54
%endif

# Uses pkgconfig
BuildRequires: libexpat-devel
Source44: import.info

%description
libcutl is a C++ utility library. It contains a collection of generic and
fairly independent components.

%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0


%if 0%{?external_boost:1}
%patch0
rm -rv cutl/details/boost
%endif
rm -rv cutl/details/expat

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# Use the system Boost and expat libraries
confopts="--disable-static --with-external-expat %{?external_boost}"
# If building on RHEL 5
%if 0%{?rhel} == 5
# Use the EPEL Boost 1.41 instead of the standard system one
confopts="$confopts CPPFLAGS=-I%{_includedir}/boost141 LDFLAGS=-L%{_libdir}/boost141"
%endif
%configure $confopts
%make_build

%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}



%files
%doc LICENSE
%{_libdir}/libcutl-%{base_version}.so

%files devel
%doc NEWS
%{_includedir}/cutl/
%{_libdir}/libcutl.so
%{_libdir}/pkgconfig/libcutl.pc

%changelog
* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.10.0-alt1_21
- update to new release by fcimport

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_18
- update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_13
- update to new release by fcimport

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_10
- fixed build

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_4
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_3
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_1
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_6
- new version

