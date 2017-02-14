%define _altdata_dir %_datadir/alterator

Name: alterator-selinux-users
Version: 0.2.5
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
rm -f %buildroot/%_altdata_dir/applications/selinux-seusers.desktop

%files
%_altdata_dir/ui/*
%_altdata_dir/applications/*
%_alterator_backend3dir/*
%_bindir/*

%changelog
* Tue Feb 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1
- Use common Makefile include module.mk to support localization
- Fix case of labels, fix unlocalized label
- Do not display selinux-seusers module
- Do not display module in ahttpd (missing template)
- Put module to Users section

* Fri Feb 13 2015 Andriy Stepanov <stanv@altlinux.ru> 0.2.4-alt1
- LC_MESSAGES=C for backends

* Wed Oct 09 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.3-alt1
- Fixed saving of the last category SE User.

* Tue Oct 08 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.2-alt1
- can't change SE User if linux users tied it.
- linux users always have minimal context SE User associated with it.

* Thu Oct 03 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.1-alt1
- can't delete SE User if linux users tied it

* Thu Oct 03 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.0-alt1
- added new module selinux-seusers for change SELinux Users

* Wed Sep 26 2013 Andrey Kolotov <qwest@altlinux.org> 0.1.0-alt1
- Initial release
