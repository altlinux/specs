Name: rack-plugin-mindmeld
Version: 2.5.0
Release: alt1

Summary: Mind Meld modules for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/MarcBoule/MindMeldModular

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

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
* Mon Oct 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.5.0-alt1
- 2.5.0 released

* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.3-alt1
- 2.2.3 released


