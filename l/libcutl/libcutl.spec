# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 24
# The base of the version (just major and minor without point)
%global base_version 1.10

Name:           libcutl
Version:        %{base_version}.0
Release:        alt1_4
Summary:        C++ utility library from Code Synthesis

Group:          System/Libraries
License:        MIT
URL:            http://www.codesynthesis.com/projects/libcutl/
Source0:        http://www.codesynthesis.com/download/libcutl/%{base_version}/%{name}-%{version}.tar.bz2
Patch0:         libcutl_no_boost_license.patch

# Set BuildRoot for compatibility with EPEL <= 5
# See: http://fedoraproject.org/wiki/EPEL:Packaging#BuildRoot_tag

# If building on Fedora or RHEL 6/7
%if 0%{?rhel}%{?fedora} >= 6
# Use the system Boost instead of the internal one
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
%else
# Otherwise, on RHEL 5 use the EPEL Boost 1.41 instead of the internal one
BuildRequires: boost141-devel
%endif
# Uses pkgconfig
BuildRequires: libexpat-devel
Source44: import.info


%description
libcutl is a C++ utility library. It contains a collection of generic and
fairly independent components.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0
rm -r cutl/details/boost cutl/details/expat


%build
# Use the system Boost and expat libraries
confopts="--disable-static --with-external-boost --with-external-expat"
# If building on RHEL 5
%if 0%{?rhel}%{?fedora} <= 5
# Use the EPEL Boost 1.41 instead of the standard system one
confopts="$confopts CPPFLAGS=-I%{_includedir}/boost141 LDFLAGS=-L%{_libdir}/boost141"
%endif
%configure $confopts
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc LICENSE
%{_libdir}/libcutl-%{base_version}.so
# Exclude the documentation that doesn't need to be packaged
%exclude %{_datadir}/doc/%{name}/INSTALL
%exclude %{_datadir}/doc/%{name}/LICENSE
%exclude %{_datadir}/doc/%{name}/NEWS
%exclude %{_datadir}/doc/%{name}/README
%exclude %{_datadir}/doc/%{name}/version

%files devel
%doc NEWS
%{_includedir}/cutl/
%{_libdir}/libcutl.so
%{_libdir}/pkgconfig/libcutl.pc


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_4
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_3
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_1
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_6
- new version

