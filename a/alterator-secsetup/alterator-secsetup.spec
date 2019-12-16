Name: alterator-secsetup
Version: 1.3
Release: alt1

Source: %name-%version.tar

Summary: alterator module for managing security settings
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator
BuildRequires: gcc gcc-c++ gcc-c++-common librpm-devel 

AutoReq: no

%description
alterator module for managing security settings

%prep
%setup -q

%build
%make_build RPM_V413=$(rpm --version | cut -d. -f2) LIB_PREFIX=%_libdir

%install
%makeinstall 
mkdir -p -m 0755 %buildroot%_unitdir
install -m 0644 macrosblock.service %buildroot%_unitdir/
mkdir -p -m 0755 %buildroot%_sysctldir/
install -m 0644 secsetup.conf %buildroot%_sysctldir/

%files
%_bindir/*
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/*
%config(noreplace) %_sysctldir/*

%changelog
* Fri Dec 13 2019 Ivan Razzhivin <underwit@altlinux.org> 1.3-alt1
- add sysctl default config for AltHa
- settings are saved after reboot

* Thu Dec 12 2019 Ivan Razzhivin <underwit@altlinux.org> 1.2-alt1
- add additional parameters

* Wed Dec 11 2019 Ivan Razzhivin <underwit@altlinux.org> 1.1-alt1
- add support AltHa (Alt Hardening)

* Mon Nov 18 2019 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- initial build
