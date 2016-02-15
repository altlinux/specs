%add_optflags %optflags_shared
Name:           libXNVCtrl
Version:        352.21
Release:        alt1_3
Summary:        Library providing the NV-CONTROL API
Group:          System/Libraries
License:        GPLv2+
URL:            ftp://download.nvidia.com/XFree86/nvidia-settings/
Source0:        ftp://download.nvidia.com/XFree86/nvidia-settings/nvidia-settings-%{version}.tar.bz2
Patch0:         libxnvctrl_so_0.patch
Patch1:         libxnvctrl_optflags.patch

BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: coreutils
Source44: import.info

%description
This packages contains the libXNVCtrl library from the nvidia-settings
application. This library provides the NV-CONTROL API for communicating with
the proprietary NVidia xorg driver. This package does not contain the
nvidia-settings tool itself as that is included with the proprietary drivers
themselves. 


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n nvidia-settings-%{version}
%patch0 -p1
%patch1 -p1


%build
make %{?_smp_mflags} \
   CC="gcc" \
   NV_VERBOSE=1 \
   OPTFLAGS="%{optflags}" \
   -C src/%{name}


%install
pushd src/%{name}
install -m 0755 -d $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0755 libXNVCtrl.so.0.0.0    $RPM_BUILD_ROOT%{_libdir}/
ln -s libXNVCtrl.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libXNVCtrl.so.0
ln -s libXNVCtrl.so.0 $RPM_BUILD_ROOT%{_libdir}/libXNVCtrl.so
install -m 0755 -d $RPM_BUILD_ROOT%{_includedir}/NVCtrl/
install -p -m 0644 {nv_control,NVCtrl,NVCtrlLib}.h $RPM_BUILD_ROOT%{_includedir}/NVCtrl/
popd


%files
%doc COPYING
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/%{name}.so


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 352.21-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 352.21-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_7
- update to new release by fcimport

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 169.12-alt2_6.1
- Fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 169.12-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 169.12-alt1_5
- initial import by fcimport

