%define _altdata_dir %_datadir/alterator

Name: alterator-selinux-users
Version: 0.2.1
Release: alt1

Packager: Andrey Kolotov <qwest@altlinux.org>

Source:%name-%version.tar

Summary: alterator module for administration users in SE Linux
License: GPL
Group: System/Configuration/Other

BuildRequires: alterator >= 4.10-alt5
BuildRequires: gcc-c++ libselinux-devel

%description
alterator module for administration users in SE Linux

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall DESTDIR=%buildroot

%files
%_altdata_dir/ui/*
%_altdata_dir/applications/*
%_alterator_backend3dir/*
%_bindir/*

%changelog
* Thu Oct 03 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.1-alt1
- can't delete SE User if linux users tied it

* Thu Oct 03 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.0-alt1
- added new module selinux-seusers for change SELinux Users

* Wed Sep 26 2013 Andrey Kolotov <qwest@altlinux.org> 0.1.0-alt1
- Initial release
