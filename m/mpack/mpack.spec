Name: mpack
Version: 1.6
Release: alt2

Summary: %name and munpack MIME e-mail utilities
Copyright: Distributable
Group: File tools
Url: ftp://ftp.andrew.cmu.edu/pub/mpack/
Patch0: %name-%version-%release.patch

Source: %name-%version.tar

%description
Mpack and munpack are utilities for encoding and decoding (respectively)
binary files in MIME (Multipurpose Internet Mail Extensions) format mail
messages. For compatibility with older forms of transferring binary files,
the munpack program can also decode messages in split-uuencoded format.
The Macintosh version can also decode messages in split-BinHex format.

%prep
%setup -q 
%patch0 -p1

%build
%configure
%make

%install
%makeinstall

%clean

%files
%_bindir/*
%_mandir/man?/*
%doc README.unix

%changelog
* Wed Nov 26 2008 Anton Farygin <rider@altlinux.ru> 1.6-alt2
- cleanup specfile
- added patches from Debian

* Tue Jan 25 2005 Anton Farygin <rider@altlinux.ru> 1.6-alt1
- new version
- specfile cleanup

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.5-ipl3
- rebuild

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.5-ipl2
- rebuild

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.5-ipl1
- FHSification.

* Sun Apr  9 2000 Dmitry V. Levin <ldv@fandra.org>
- RE adaptions.

* Tue Apr 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Build for RH5

* Sun Mar 22 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Build Root'ed
- Moved to /usr/bin
- Added attr in install
- Added clean
