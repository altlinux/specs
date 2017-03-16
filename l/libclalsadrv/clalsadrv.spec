# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname clalsadrv
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Summary:       ALSA driver C++ Library
Name:          libclalsadrv
Version:       2.0.0
Release:       alt1_13
License:       GPLv2+
Group:         System/Libraries
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{oldname}-%{version}.tar.bz2

Obsoletes:     alsadrv <= 0.0.2
Provides:      alsadrv > 0.0.2
BuildRequires: libalsa-devel
Provides: clalsadrv = %{version}-%{release}

%description
ALSA driver C++ access library

%package       devel
Summary:       ALSA driver C++ access library
Group:         Development/Other
Requires:      %{name} = %{version}-%{release}

Obsoletes:     alsadrv-devel <= 0.0.2
Provides:      alsadrv-devel > 0.0.2
Provides: clalsadrv-devel = %{version}-%{release}

%description devel
ALSA driver C++ access library. This package includes the development
tools.

%prep
%setup -n %{oldname}-%{version} -q

%build
cd libs
sed -i -e "s|/sbin/ldconfig|# /sbin/ldconfig|g" \
       -e "s|-O2|%{optflags}|g" Makefile
%make_build LIBDIR=%{_lib}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cd libs
make PREFIX=%{buildroot}%{_prefix} LIBDIR=%{_lib} install
ln -s lib%{oldname}.so.2.0.0 %{buildroot}%{_libdir}/lib%{oldname}.so.2

%files
%doc AUTHORS COPYING
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}.h
%{_libdir}/lib%{oldname}.so

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_6
- update to new release by fcimport

* Thu Jan 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_5
- fc import

