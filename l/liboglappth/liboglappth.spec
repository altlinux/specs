# BEGIN SourceDeps(oneline):
BuildRequires: libglvnd-devel
# END SourceDeps(oneline)
Group: Engineering
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           liboglappth
Summary:        An OpenGL wrapper library
Version:        1.0.0
Release:        alt1_22

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
Source44: import.info

%description
Library for creating portable OpenGL applications with easy-to-code
scene setup and selection operations.

%package devel
Group: Development/Other
Summary:    Libraries and header files from %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Libraries and header include files for developing programs
based on %{name}.

%prep
%setup -q
# FIXME: set -e behavior change between f26 and f27??
[ -s NEWS ] && exit 1 || :
[ -s README ] && exit 1 || :
autoreconf -v -f -i

%build
%configure --disable-static
%make_build CCOPTIONS="%{optflags}" LIBS="-lGL -lGLU"

%install
%makeinstall_std
find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;



%files
%doc AUTHORS
%doc ChangeLog
%doc --no-dereference COPYING

%{_libdir}/liboglappth.so.2
%{_libdir}/liboglappth.so.2.*

%files devel
%{_includedir}/oglappth/
%{_libdir}/liboglappth.so
%{_libdir}/pkgconfig/liboglappth.pc


%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 1.0.0-alt1_22
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_13
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_9
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_7
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_7
- initial import by fcimport

