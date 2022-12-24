# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major       6
%define libname     lib%{oname}%{major}
%define develname   lib%{oname}-devel

%define oname       lscp

Name:          liblscp
Summary:       LinuxSampler Control Protocol (LSCP) wrapper library
Version:       0.9.7
Release:       alt1_1
License:       LGPLv2
Group:         System/Libraries
URL:           http://www.linuxsampler.org/
Source0:       https://sourceforge.net/projects/qsampler/files/liblscp/%{version}/%{name}-%{version}.tar.gz

BuildRequires: ccmake cmake ctest
Source44: import.info

%description
LinuxSampler Control Protocol (LSCP) wrapper library.

#--------------------------------------------------------------------

%package -n     %libname
Group:          System/Libraries
Summary:        Libraries for %name
Provides:       %name = %version-%release

%description -n %libname
LinuxSampler Control Protocol (LSCP) wrapper library.

%files -n %libname
%{_libdir}/liblscp.so.%{major}*

#--------------------------------------------------------------------

%package -n     %develname
Group:          Development/Other
Summary:        Libraries for %name
Requires:       %libname = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %develname
Development libraries from %oname.

%files -n %develname
%doc --no-dereference LICENSE  
%dir %{_includedir}/lscp
%{_includedir}/lscp/*.h
%{_libdir}/liblscp.so
%{_libdir}/pkgconfig/lscp.pc

#--------------------------------------------------------------------

%prep
%setup -q


%build
%{mageia_cmake} -DCMAKE_INSTALL_PREFIX=%{_usr} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

%mageia_cmake_build

%install
%mageia_cmake_install

find %{buildroot} -name "*.la" -delete


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.7-alt1_1
- update by mgaimport

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 0.9.6-alt1_1
- update by mgaimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.9.5-alt1_1
- update by mgaimport

* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0.9.3-alt1_1
- update by mgaimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 0.9.2-alt1_1
- update by mgaimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 0.9.1-alt1_1
- update by mgaimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_1
- update by mgaimport

* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update by mgaimport

* Thu Dec 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_1
- update by mgaimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- update by mgaimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_2
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.1-alt1.qa2
- NMU: rebuilt for debuginfo.

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liblscp
  * postun_ldconfig for liblscp
  * postclean-05-filetriggers for spec file

* Sat Nov 05 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux

