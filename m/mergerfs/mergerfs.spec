Name: mergerfs
Version: 2.3.0
Release: alt1
Summary: A FUSE union filesystem

Group: File tools
License: MIT
Url: https://github.com/trapexit/mergerfs
Packager: Evgenii Terechkov <evg@altlinux.org>
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: gcc-c++ libattr-devel libfuse-devel pandoc

%description
mergerfs is similar to mhddfs, unionfs, and aufs. Like mhddfs in that it too
uses FUSE. Like aufs in that it provides multiple policies for how to handle
behavior.

%prep
%setup
%patch0 -p1

%build
make %{?_smp_mflags}
make man

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/*
%_man1dir/*.1*
%doc README.md

%changelog
* Sat Sep  5 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Aug 22 2015 Terechkov Evgenii <evg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Linux Sisyphus
