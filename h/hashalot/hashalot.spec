Name: hashalot
Version: 0.3
Release: alt1

Summary: Binary hash generator
License: GPL
Group: System/Base
Url: http://www.paranoiacs.org/~sluskyb/hacks/hashalot/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://www.paranoiacs.org/~sluskyb/hacks/hashalot/hashalot-%version.tar.gz
Source: hashalot-%version.tar
Patch: hashalot-%version-%release.patch

%description
This program will read a passphrase from standard input and print a binary
(not printable) hash to standard output.  The output is suitable for use as
an encryption key.

%prep
%setup -q
%patch -p1

%build
autoreconf -fisv
%define _sbindir /sbin
%configure
%make_build

%install
%makeinstall

%files
%_sbindir/*
%_man8dir/*

%changelog
* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Updated to 0.3.
- Added -q option.
- Fixed compilation warnings.

* Wed Mar 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.0-alt3
- Minor error reporing corrections.

* Mon Mar 08 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.0-alt2
- Major code cleanup.

* Thu Mar 04 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt1
- Initial build
