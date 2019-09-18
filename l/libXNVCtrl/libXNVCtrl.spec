Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libXNVCtrl
Version:        435.17
Release:        alt1_1
Summary:        Library providing the NV-CONTROL API
License:        GPLv2+
URL:            https://download.nvidia.com/XFree86/nvidia-settings/
Source0:        %{url}/nvidia-settings-%{version}.tar.bz2
Patch0:         libxnvctrl_so_0.patch

BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: coreutils

# Obsoletes older package provided in the NVIDIA CUDA repository
Obsoletes: nvidia-%{name} < 3:%{version}-100
Provides: nvidia-%{name} = 3:%{version}-100
Source44: import.info

%description
This packages contains the libXNVCtrl library from the nvidia-settings
application. This library provides the NV-CONTROL API for communicating with
the proprietary NVidia xorg driver. This package does not contain the
nvidia-settings tool itself as that is included with the proprietary drivers
themselves. 


%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n nvidia-settings-%{version}
%patch0 -p1



%build

%make_build \
   CC="gcc" \
   NV_VERBOSE=1 \
   DO_STRIP=0 \
   STRIP_CMD=/dev/true \
   -C src/%{name} \
   libXNVCtrl.so


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
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/%{name}.so


%changelog
* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 435.17-alt1_1
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 352.21-alt1_11
- fc merge

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 352.21-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 352.21-alt1_4
- update to new release by fcimport

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

