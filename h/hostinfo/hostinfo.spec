Name: hostinfo
Version: 2.2
Release: alt5

Summary: Utility for looking up hostnames and IP addresses
License: BSD-style
Group: System/Configuration/Networking
Url: http://www.jmknoble.net/software/hostinfo
Packager: Dmitry V. Levin <ldv@altlinux.org>

# due to resolve(1).
Conflicts: net-tools < 0:1.60-alt10

BuildRequires: help2man

# %url/hostinfo-%version.tar.gz
Source: hostinfo-%version.tar
Source1: resolve.c
Source2: resolve.1.inc
Patch: hostinfo-2.2-alt-fixes.patch

%description
hostinfo is an utility for looking up hostnames and IP addresses.
It is a simple wrapper around gethostbyname(3) and gethostbyaddr(3);
thus, it uses a combination of the local system's "host database"
(/etc/hosts and/or NIS/NIS+) and the DNS resolver.

%prep
%setup -q
%patch -p1
install -pm644 %_sourcedir/{resolve.c,resolve.1.inc} .

%build
make OPTFLAGS="%optflags"
help2man -N -s1 -i hostinfo.1.inc ./hostinfo >hostinfo.1
gcc %optflags resolve.c -o resolve
help2man -N -s1 -i resolve.1.inc ./resolve >resolve.1


%install
%make_install install \
	prefix="%prefix" \
	DESTDIR="%buildroot" \
	#
install -pD -m644 hostinfo.1 %buildroot%_man1dir/hostinfo.1

install -pm755 resolve %buildroot%_bindir/
install -pm644 resolve.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*
%doc ChangeLog

%changelog
* Mon Oct 27 2008 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt5
- resolve: Fixed build with fresh glibc headers.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt4
- Reduced macro abuse in specfile.

* Sat Sep 16 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt3
- resolve: Implemented timeout option (inger).

* Tue Apr 19 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt2
- Fixed --help/--version exit code.
- Adjusted --help/--version output for help2man,
  build and package help2man-generated manpage.
- Relocated resolve(1) from net-tools to this package (#6360).

* Sun Feb 23 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt1
- Initial revision.
