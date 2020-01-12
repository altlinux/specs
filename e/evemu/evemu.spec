# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++ python-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name evemu
%define		major		3
%define		libname		lib%{name}%{major}
%define		devname		lib%{name}-devel

Name:		evemu
Version:	2.7.0
Release:	alt2_2
Summary:	Event Device Query and Emulation Program
Group:		Development/Other
License:	GPLv3+
URL:		http://www.freedesktop.org/wiki/Evemu/
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(libevdev) >= 0.5
BuildRequires:	xmlto
BuildRequires:	asciidoc asciidoc-a2x
Source44: import.info

%description
%{name} is a simple utility to capture the event stream from input devices
and replay that stream on a virtual input device.

#------------------------------------------------------------------

%package -n	%{libname}
Summary:	Event Device Query and Emulation Program Library Package
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs
dynamically linked with evemu.

#------------------------------------------------------------------

%package -n	%{devname}
Summary:	Event Device Query and Emulation Program Development Package
Group:		Development/Other
Requires:       %{libname} = %{version}-%{release}
Requires:	pkgconfig
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides headers files for evemu development.

#------------------------------------------------------------------
%prep
%setup -q

%build
autoreconf -vfi
%configure \
		--disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files
%doc COPYING
%{_bindir}/%{name}-describe
%{_bindir}/%{name}-device
%{_bindir}/%{name}-play
%{_bindir}/%{name}-record
%{_bindir}/%{name}-event
%{_mandir}/man1/%{name}-*.1*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{python_sitelibdir_noarch}/%{name}/
%{python_sitelibdir_noarch}/%{name}/*


%changelog
* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt2_2
- fixed build

* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt2_1
- to Sisyphus as dependency for frame

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_4
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_3
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_1
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_2.20150818giteba96a4
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.99.0-alt1_3.20140324gitaf60032
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- update to new release by fcimport

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_3
- update to new release by fcimport

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_2
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_1
- fc import

