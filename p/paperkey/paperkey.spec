# SPEC file for paperkey package

Name: paperkey
Version: 1.5
Release: alt1

Summary: an OpenPGP key archiver

License: %gpl2plus
Group: Archiving/Backup
URL: http://www.jabberwocky.com/software/paperkey/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Tue Sep 19 2017
# optimized out: gnu-config python-base python-modules python3 python3-base ruby ruby-stdlibs
BuildRequires: gnu-config

%description
Paperkey provides a reasonable way to achieve a long term backup
of OpenPGP (GnuPG, PGP, etc) keys is to print them out on paper.
Paper and ink have amazingly long retention qualities - far
longer than the magnetic or optical means that are generally
used to back up computer data.

%prep
%setup

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make
%make check

%install
%makeinstall

%files
%doc README AUTHORS ChangeLog NEWS
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%{name}*

%changelog
* Sat Nov 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.5-alt1
- New version

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.4-alt2
- Initial build for ALT Linux Sisyphus

