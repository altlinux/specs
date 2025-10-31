Name: rack-plugin-vcv-recorder
Version: 2.0.3
Release: alt1

Summary: Recorder for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/VCV-Recorder

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)

%description
%summary

%prep
%setup

%build
%make_build RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Fri Oct 31 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.3-alt1
- initial
