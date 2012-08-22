%define _altdata_dir %_datadir/alterator

Name: alterator-mkimage
Version: 0.2
Release: alt1

Summary: Create distribution images
License: GPL
Group: System/Configuration/Other

Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: gettext
Requires: mkimage-profiles >= 0.6.6
# see also #23377
Requires: alterator >= 4.21
BuildPreReq: alterator >= 3.1

%description
%summary by means of mkimage-profiles.

%prep
%setup

%build
%make_build libdir=%_libdir

%install
%makeinstall
cat >%name <<EOF
#!/bin/sh
/usr/sbin/alterator-standalone mkimage
EOF
install -pDm755 %name %buildroot%_bindir/%name
%find_lang %name

%files -f %name.lang
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_altdata_dir/help/*/*
%_alterator_backend3dir/*
%_bindir/%name

%changelog
* Wed Aug 22 2012 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- UI improvements and a tiny reliability fix (thx dkr@)

* Fri May 11 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
