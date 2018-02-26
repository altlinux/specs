Name: jikes
Version: 1.22
Release: alt1.1

Summary: Java source to bytecode compiler
License: IBM Public License
Group: Development/Java
Url: http://oss.software.ibm.com/developerworks/opensource/jikes/

Source: %url/%name-%version.tar.bz2

Provides: jikes

Prefix: %prefix

# Automatically added by buildreq on Fri Nov 26 2004
BuildRequires: hostinfo libstdc++-devel

BuildRequires: gcc-c++

%description
The IBM Jikes compiler translates Java source files to bytecode. It
also supports incremental compilation and automatic makefile generation,
and is maintained by the Jikes Project.

%prep
%setup -q

%build
%configure --disable-dependency-tracking
make

%install
%makeinstall

%files
%doc README AUTHORS ChangeLog NEWS TODO INSTALL
%doc doc/*.htm*
%doc %_mandir/man1/*
%_bindir/jikes
/usr/include/*.h

%changelog
* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.22-alt1.1
- Rebuilt with libstdc++.so.6.
- Remove gcc3.3-c++ from BuildReq.

* Fri Nov 26 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.22-alt1
- new version

* Mon Apr 19 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.20-alt1
- new version


* Thu Oct 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.17-alt1
- new version

* Wed Aug 14 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.16-alt1
- new version

* Sat May 18 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.15-alt1
- new version

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.14-alt1
- new version

* Thu Apr 05 2001 Rider <rider@altlinux.ru> 1.13-alt1
- 1.13

* Mon Nov 20 2000 Dmitry V. Levin <ldv@fandra.org> 1.12-ipl2mdk
- Patched to enable build with gcc-2.96.

* Sun Aug 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.12-ipl1mdk
- RE adaptions.

* Mon Aug 7 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 1.12-1mdk
- Moved to jikes 1.12
- Moved man to the FHS compliant places.

* Tue Apr 11 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed Distribution name

* Thu Mar 16 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Adapted to the new Group structure

* Thu Jan 20 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed packager name

* Wed Jan 12 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Moved to 1.11

* Wed Nov 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First spec file for Mandrake distribution.

