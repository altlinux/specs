Name: light-locker-settings
Version: 1.5.0
Release: alt2

Summary: Simple settings dialog for light-locker
License: %gpl3only
Group: Graphical desktop/Other

URL: https://launchpad.net/light-locker-settings
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

BuildRequires: python3-devel intltool

Requires: light-locker

%define _unpackaged_files_terminate_build 1

%description
%summary

%prep
%setup
%patch -p1

%build
./configure \
	--prefix=%_prefix

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name

%changelog
* Fri Nov 22 2019 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt2
- Port to python3.

* Tue Apr 12 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1
- Update for current psutils.
- Initial build.

