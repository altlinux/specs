Name: nosync
Version: 0.1
Release: alt2

Summary: library to disable sync/fsync/fdatasync
License: Public domain
Group: Development/C

#Url:
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

%description
Library to disable sync/fsync/fdatasync.
Run your program as $ nosync program for disable sync calls.
Uwaga! Use only if you needs in data corrupted after system failure.

See http://lj.rossia.org/users/igorpashev/26733.html
for use examples.

%prep
%setup
%__subst "s|/usr/lib|%_libdir|g" nosync
%build
gcc %optflags_shared -s -Wall -shared -o libnosync.so libnosync.c

%install
install -D -m644 libnosync.so %buildroot%_libdir/libnosync.so
install -D nosync %buildroot%_bindir/nosync

%files
%doc README
%_bindir/nosync
%_libdir/libnosync.so

%changelog
* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- build from git, add README

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
