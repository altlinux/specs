Name: rack-plugin-valley
Version: 2.4.5
Release: alt1

Summary: Valley plugins fro VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/ValleyAudio/ValleyRackFree

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

%prep
%setup

%build
%ifarch x86_64
%add_optflags -msse3
%endif
%make_build RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.5-alt1
- 2.4.5 released


