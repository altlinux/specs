Group: System/Libraries
%add_optflags %optflags_shared
%define oldname clalsadrv
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Summary:       ALSA driver C++ Library
Name:          libclalsadrv
Version:       2.0.0
Release:       alt1_21
License:       GPLv2+
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{oldname}-%{version}.tar.bz2

BuildRequires: libalsa-devel
BuildRequires: gcc-c++
# This package has been deprecated upstream and replaced by zita-alsa-pcmi
Provides:      deprecated()
Source44: import.info

%description
ALSA driver C++ access library

%package       devel
Group: Development/Other
Summary:       ALSA driver C++ access library
Requires:      %{name} = %{version}-%{release}
Provides:      deprecated()


%description devel
ALSA driver C++ access library. This package includes the development
tools.

%prep
%setup -n %{oldname}-%{version} -q

%build
cd libs
sed -i -e "s|/sbin/ldconfig|# /sbin/ldconfig|g" \
       -e "s|-O2|%{optflags}|g" Makefile
%make_build LDFLAGS="$RPM_LD_FLAGS" LIBDIR=%{_lib}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cd libs
make PREFIX=%{buildroot}%{_prefix} LIBDIR=%{_lib} install
ln -s lib%{oldname}.so.2.0.0 %{buildroot}%{_libdir}/lib%{oldname}.so.2


%files
%doc AUTHORS
%doc --no-dereference COPYING
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}.h
%{_libdir}/lib%{oldname}.so

%changelog
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_21
- update to new release by fcimport

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_19
- cleaned up provides (closes: #36613)

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_15
- update to new release by fcimport

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

