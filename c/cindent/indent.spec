Summary: CIndent - format C program sources
Name: cindent
Version: 2.0.20230205
Release: alt1
License: GPLv2
Group: Development/C
Url: https://invisible-island.net/cindent/cindent.html
Source0: indent-%version.tgz

# Automatically added by buildreq on Wed Jan 10 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libgpg-error python3 python3-base python3-dev sh5
BuildRequires: cppcheck ctags

%description
The `cindent' program changes the appearance of a C program by
inserting or deleting whitespace.

This is a stable version of indent, used in most programs at
    https://invisible-island.net/

It has some feature enhancements required by those programs,
not found in other versions of indent.

%prep
#setup -n indent-%(echo %version | sed -E 's/(.*)[.](.*)/\1-\2/')
%setup -n indent

%build
%configure --program-prefix=c
%make_build

%install
%makeinstall_std

%check
make check

%files
%_bindir/*
%_mandir/man1/*
%_datadir/tdindent/*
%_infodir/*

%changelog
* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 2.0.20230205-alt1
- Autobuild version bump to 2.0.20230205

* Wed Jan 10 2024 Fr. Br. George <george@altlinux.ru> 2.0.20221016-alt1
- Initial build for ALT

* Sun Oct 02 2022 Thomas Dickey
- add xxx-compare

* Mon Oct 04 2010 Thomas Dickey
- initial version
