Name: alterator-secsetup
Version: 1.0
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
%make_build RPM_V413=$(rpm --version | cut -d. -f2)

%install
%makeinstall 
mkdir -p -m 0755 %buildroot/%_unitdir
install -m 0644 macrosblock.service %buildroot/%_unitdir/

%files
%_bindir/*
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/*

%changelog
* Mon Nov 18 2019 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- initial build
