Name: unionfs
Version: 2.0
Release: alt1.git039ba92
Summary: union filesystem using FUSE

Group: File tools
License: BSD
Url: https://github.com/rpodgorny/unionfs-fuse

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %name-%version.tar

BuildRequires: gcc libattr-devel libfuse-devel

%description
unionfs filesystem implementation which is way more flexible than the current in-kernel unionfs solution.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/*
%_man8dir/*.8*
%doc README.md

%changelog
* Wed May 24 2017 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1.git039ba92
- Initial build for ALT Linux Sisyphus
