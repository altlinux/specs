%add_optflags %optflags_shared
Name:           libXNVCtrl
Version:        169.12
Release:        alt2_10
Summary:        Library providing the NV-CONTROL API
Group:          System/Libraries
License:        GPLv2+
URL:            ftp://download.nvidia.com/XFree86/nvidia-settings/
Source0:        ftp://download.nvidia.com/XFree86/nvidia-settings/nvidia-settings-%{version}.tar.gz
Patch0:         libXNVCtrl-imake.patch
BuildRequires: xorg-cf-files gccmakedep imake libX11-devel libXext-devel
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
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n nvidia-settings-1.0
%patch0 -p1 -z .imake
pushd src/%{name}
xmkmf
#libdir doesnt get set right on sparc64
%ifarch sparc64
sed -i -e 's|/usr/lib|/usr/lib64|g' Makefile
%endif
popd


%build
pushd src/%{name}
make %{?_smp_mflags} CDEBUGFLAGS="$RPM_OPT_FLAGS"
popd


%install
pushd src/%{name}
make install DESTDIR=$RPM_BUILD_ROOT INSTINCFLAGS="-p -m 644"
popd
# imake installs these under X11/extensions, but apps expect them under NVCtrl
mv $RPM_BUILD_ROOT%{_includedir}/X11/extensions \
  $RPM_BUILD_ROOT%{_includedir}/NVCtrl


%files
%doc COPYING src/%{name}/README.LIBXNVCTRL
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/%{name}.so


%changelog
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

