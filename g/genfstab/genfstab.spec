Name:    genfstab
Version: 28
Release: alt1

Summary: Generate output suitable for addition to an fstab file
License: GPL-2.0-only
Group:   System/Configuration/Other
Url:     https://github.com/archlinux/arch-install-scripts.git

BuildRequires: asciidoc-a2x

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

%description
genfstab helps fill in an fstab file by autodetecting all the current mounts 
below a given mountpoint and printing them in fstab-compatible format to standard output. 
It can be used to persist a manually mounted filesystem hierarchy and is often used 
during the initial install and configuration of an OS.

%prep
%setup
%patch -p1

%install
%makeinstall_std man

%check
make check

%files
%doc COPYING README.md
%_bindir/%name
%_man8dir/%name.8.*


%changelog
* Thu Jun 22 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 28-alt1
- Initial build for ALT 

