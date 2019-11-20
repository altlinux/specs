# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global majorver 3 

Name: libapogee
Version: 3.2
Release: alt1_3
Summary: Library for Apogee CCD Cameras

License: GPLv2+ and MPLv2.0
URL: http://indilib.org

# Tar is generated from the huge all-in-one tar from INDI
# by using ./libapogee-generate-tarball.sh 1.3.1
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-generate-tarball.sh

BuildRequires:  gcc-c++
BuildRequires: boost-complete ctest cmake libusb-compat-devel libcurl-devel libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils
Source44: import.info

%description
Apogee library is used by applications to control Apogee CCDs.

%package devel
Group: Development/C
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}-%{version}
sed -i 's|/etc/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION lib${LIB_SUFFIX}|g' CMakeLists.txt

%build
%{fedora_cmake}
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}



%files
%doc --no-dereference LICENSE
%doc README
%{_libdir}/*.so.*
%{_sysconfdir}/Apogee/*
%{_udevrulesdir}/99-apogee.rules

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_3
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_1
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_4
- new version

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.3234-alt1_8.1
- NMU: rebuilt with boost-1.67.0

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.3234-alt1_8
- update to new release by fcimport

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.3234-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_18
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_13
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_8
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_6
- spec cleanup thanks to ldv@

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5
- initial import by fcimport

