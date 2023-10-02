# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html
%global optflags_lto %nil
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	2
%define libname	libcerf%{major}
%define devname	libcerf-devel

Name:		libcerf
Summary:	Complex error functions, Dawson, Faddeeva, and Voigt function
Version:	2.4
Release:	alt1_2
Group:		System/Libraries
License:	MIT
Url:		https://jugit.fz-juelich.de/mlz/libcerf
Source0:	https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:	ccmake cmake ctest
Source44: import.info

%description
A self-contained C library providing complex error functions, based on
Faddeeva's plasma dispersion function w(z).

Also provides Dawson's integral and Voigt's convolution of a Gaussian
and a Lorentzian.

%package -n %{libname}
Summary:	Complex error functions, Dawson, Faddeeva, and Voigt function
Group:		System/Libraries

%description -n %{libname}
A self-contained C library providing complex error functions, based on
Faddeeva's plasma dispersion function w(z).

Also provides Dawson's integral and Voigt's convolution of a Gaussian
and a Lorentzian.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q -n %{name}-v%{version}


# Force cmake to use the paths passed at configure time
sed -i -e 's|lib/pkgconfig/|%{_lib}/pkgconfig/|' CMakeLists.txt
sed -i -e 's|DESTINATION lib|DESTINATION %{_lib}|' lib/CMakeLists.txt
sed -i -e 's|${prefix}/lib|@LIB_INSTALL_DIR@|' libcerf.pc.in
sed -i -e 's|@destination@|@CMAKE_INSTALL_PREFIX@|' libcerf.pc.in

# remove cruft
rm -rf fortran/__MACOSX

%build
%remove_optflags -frecord-gcc-switches
%{mageia_cmake}
%mageia_cmake_build

%install
%mageia_cmake_install

%check
%{mageia_ctest}

%files -n %{libname}
%doc CHANGELOG README*
%doc --no-dereference LICENSE
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{version}

%files -n %{devname}
%doc %{_docdir}/cerf/
%{_includedir}/cerf.h
%{_libdir}/%{name}.so
%{_libdir}/cmake/cerf/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*


%changelog
* Mon Oct 02 2023 Igor Vlasenko <viy@altlinux.org> 2.4-alt1_2
- update by mgaimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 2.1-alt1_1
- update by mgaimport

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 1.17-alt1_1
- new version

* Thu Aug 26 2021 Igor Vlasenko <viy@altlinux.org> 1.14-alt1_1
- new version

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_4
- fixed build

* Wed Aug 05 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt2_4
- llvm7 -> llvm9

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_4
- fixed build

* Wed Jun 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- mga update

* Mon Mar 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_2
- new version

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- new version

