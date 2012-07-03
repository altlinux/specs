Name: tthsum
Version: 1.2.1
Release: alt2
Summary: md5sum-alike program that works with Tiger/THEX hashes

Group: Archiving/Backup
License: GPLv3
URL: http://tthsum.devs.nu/
Source: http://tthsum.devs.nu/%name-%version.tar.bz2
Patch1: makefile.patch

BuildRequires: gcc-c++
Conflicts: microdc2

%description
tthsum is an md5sum-alike program that works with Tiger/THEX hashes.
Use it to calculate TTH checksums and to compare those with previously
calculated sums (digests).

%prep
%setup
%patch1 -p2

%build
%make_build

%install
%makeinstall DESTDIR="%buildroot"

%files
%_bindir/%name
%_man1dir/*
%doc COPYING.txt CHANGES.txt README.txt TODO.txt

%changelog
* Wed Apr 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.2.1-alt2
- Conflicts with the package microdc2

* Thu Mar 11 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
