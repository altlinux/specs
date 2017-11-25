%filter_from_requires /^python2.7.haru/d
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: python-modules-encodings
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag0 RELEASE_2_3_0

Name:           libharu
Version:        2.3.0
Release:        alt1_3
Summary:        C library for generating PDF files
License:        zlib with acknowledgement
URL:            http://libharu.org
Source0:        https://github.com/libharu/${name}/archive/%{gittag0}/%{name}-%{version}.tar.gz
Patch0:         libharu-RELEASE_2_3_0_cmake.patch

BuildRequires:  gcc-common
BuildRequires:  ctest cmake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
Source44: import.info

%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.

%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{gittag0}
# fix cmake build
%patch0 -p1 -b .cmake

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} -DLIBHPDF_STATIC=NO ..
popd

%make_build -C %{_target_platform}

%install
make install/fast -C %{_target_platform}  DESTDIR=%{buildroot}

%files
%doc README
%{_libdir}/libhpdf.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/libhpdf.so

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3
- new version

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_9
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_3
- spec cleanup thanks to ldv@

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3
- converted by srpmconvert script

