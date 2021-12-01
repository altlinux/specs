Name: alterator-setup-welcome
Version: 0.0.1
Release: alt1

Summary: alterator module for showing welcome message
License: GPLv2
Group: System/Configuration/Other

BuildArch:  noarch
BuildRequires: alterator

Source: %name-%version.tar

%description
%summary

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
## %_alterator_backend3dir/*

%changelog
* Fri Nov 26 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- initial build
