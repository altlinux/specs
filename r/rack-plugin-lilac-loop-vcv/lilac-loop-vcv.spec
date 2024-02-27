Name: rack-plugin-lilac-loop-vcv
Version: 2.1.6
Release: alt1

Summary: Live looping plugin
License: GPLv3
Group: Sound
Url: https://github.com/grough/lilac-loop-vcv

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
Lilac Loop is a free plugin for VCV Rack inspired by the recording style
of a live looper pedal.

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
* Tue Feb 27 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.6-alt1
- 2.1.6 released

