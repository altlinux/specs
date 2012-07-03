Name: lockfile-progs
Version: 0.1.11
Release: alt2

Summary: Programs for locking and unlocking files and mailboxes
License: GPLv2
Group: File tools

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

# http://ftp.debian.org/debian/pool/main/l/lockfile-progs/%{name}_%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Oct 29 2008
BuildRequires: liblockfile-devel

%description
This package includes several programs to safely lock and unlock files
and mailboxes from the command line.

These include:
- lockfile-create
- lockfile-remove
- lockfile-touchlock
- mail-lock
- mail-unlock
- mail-touchlock.

These programs use liblockfile to perform the file locking and
unlocking.

%prep
%setup

%build
%make

%install
install -d %buildroot{%_bindir,%_man1dir}

cp -a bin/* %buildroot%_bindir
cp -a man/* %buildroot%_man1dir

echo '.so lockfile-progs.1' > lockfile-progs.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-create.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-remove.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-touch.1
install lockfile-progs.1 %buildroot%_man1dir/mail-lock.1
install lockfile-progs.1 %buildroot%_man1dir/mail-unlock.1
install lockfile-progs.1 %buildroot%_man1dir/mail-touchlock.1

%files
%doc TODO debian/changelog
%_bindir/lockfile-create
%_bindir/lockfile-remove
%_bindir/lockfile-touch
%_bindir/mail-lock
%_bindir/mail-touchlock
%_bindir/mail-unlock
%_man1dir/lockfile-create.1*
%_man1dir/lockfile-progs.1*
%_man1dir/lockfile-remove.1*
%_man1dir/lockfile-touch.1*
%_man1dir/mail-lock.1*
%_man1dir/mail-touchlock.1*
%_man1dir/mail-unlock.1*

%changelog
* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.11-alt2
- Fix building with gcc4.4

* Wed Oct 29 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.11-alt1
- Initial build for ALT Linux (spec from PLD)
