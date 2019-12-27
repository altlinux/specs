# BEGIN SourceDeps(oneline):
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
Version:       0.6.1
Release:       alt1_1
License:       GPLv2
Group:         System/Libraries
URL:           http://www.linuxsampler.org/
Source0:       https://sourceforge.net/projects/qsampler/files/liblscp/%{version}/%{name}-%{version}.tar.gz
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
%doc COPYING
%dir %_includedir/lscp
%_includedir/lscp/*.h
%_libdir/liblscp.so
%_libdir/pkgconfig/lscp.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete


%changelog
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

