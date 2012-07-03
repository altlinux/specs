Name: bash-builtin-lockf
Version: 0.3.1
Release: alt1

Summary: lockf bash builtin
License: GPLv2+
Group: Shells
Packager: Dmitry V. Levin <ldv@altlinux.org>

Requires: /usr/lib/bash
BuildRequires: bash-devel

Source: lockf.c

%description
This package contains lockf bash builtin.

%prep
%setup -cT

%build
%__cc -shared -o lockf %_sourcedir/lockf.c \
	-DHAVE_CONFIG_H -I%_includedir/bash %optflags %optflags_shared

%install
install -pDm644 lockf %buildroot/usr/lib/bash/lockf

%files
/usr/lib/bash/*

%changelog
* Wed Jan 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Fixed typo in the help output.

* Thu Nov 27 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Add O_NONBLOCK to open flags iff non-blocking lock is requested.
- Reworked directory locking support.
- Added O_NOCTTY to open flags.

* Wed Oct 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Made the builtin less verbose by default.
- Added -v option to restore previous behavior.
- Implemented locking for directories.

* Sat Oct 06 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
