Name: mkimage-profiles-office-server
Version: 5.0.0
Release: alt2

Summary: Profiles for build Office Server ISO image
License: GPLv2+ 
Group: Development/Other
Requires: mkimage
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>
BuildArch: noarch

%define profile_dir /usr/share/mkimage/profiles-office-server
%add_findreq_skiplist %profile_dir/*.d/*

Source:%name-%version.tar

%description
This packages contents profiles for building ALT Linux Office server ISO image

%prep
%setup -q

%install
# create directory structure
mkdir -p %buildroot%profile_dir
cp -a *	%buildroot%profile_dir/
rm %buildroot%profile_dir/*spec

%files
%profile_dir

%changelog
* Tue Mar 24 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0.0-alt2
- Fixed package dependencies.

* Tue Mar 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- first build 

