Name: rack-plugin-frozen-wasteland
Version: 2.1.0
Release: alt1

Summary: Frozen Wasteland VCV plugins
License: GPLv3
Group: Sound
Url: https://github.com/almostEric/FrozenWasteland

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

%prep
%setup

%build
make RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- initial

