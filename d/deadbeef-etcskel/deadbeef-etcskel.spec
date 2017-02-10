%define oname deadbeef
Name: %oname-etcskel
Version: 0.1
Release: alt1
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Summary: Configuration for %oname
License: GPLv3
Group: Sound
Url: https://git.altlinux.org/people/antohami/packages/%name.git
BuildArch: noarch

Source0: config
Requires: deadbeef-full

%description
Configuration for %oname

%prep

%build

%install
mkdir -p %buildroot/%_sysconfdir/skel/.config/%oname
cp %SOURCE0 %buildroot%_sysconfdir/skel/.config/%oname

%files
%_sysconfdir/skel/.config/%oname

%changelog
* Fri Feb 10 2017 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus.
