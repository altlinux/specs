Name: clisp
Version: 2.49.92
Release: alt2.1
Epoch: 1

Summary: Common Lisp (ANSI CL) implementation
License: GPL
Group: Development/Lisp
Url: http://clisp.cons.org/

Source: %name-%version.tar

# core
BuildRequires: libsigsegv-devel libffcall-devel libreadline-devel libtinfo-devel
# modules
BuildRequires: libdb6-devel libgdbm-devel libpcre-devel postgresql-devel zlib-devel
BuildRequires: libX11-devel libXpm-devel libXext-devel libXau-devel
# check
BuildRequires: /proc /dev/pts

%description
Common Lisp is a high-level, general-purpose programming language.

GNU CLISP is a Common Lisp implementation by Bruno Haible of Karlsruhe
University and Michael Stoll of Munich University, both in Germany.
It mostly supports the Lisp described in the ANSI Common Lisp standard.
It runs on microcomputers (Windows NT/2000/XP, Windows 95/98/ME) as well
as on Unix workstations (Linux, SVR4, Sun4, DEC Alpha OSF, HP-UX, BeOS,
NeXTstep, SGI, AIX and others) and needs only 2 MB of RAM.

It is Free Software and may be distributed under the terms of GNU GPL,
while it is possible to distribute commercial applications compiled
with GNU CLISP.

The user interface comes in German, English, French, Spanish, Dutch,
Russian and Danish.

GNU CLISP includes an interpreter, a compiler, a debugger, CLOS,
a foreign language interface, sockets, i18n, fast bignums and more.
An X11 interface is available through CLX, Garnet, CLUE/CLIO.
GNU CLISP runs Maxima, ACL2 and many other Common Lisp packages.

%prep
%setup
cp -f /usr/share/autoconf/build-aux/config.{guess,sub} src/build-aux/

%build
sh configure --prefix=%prefix --libdir=%_libdir \
	--with-module=asdf \
	--with-module=berkeley-db \
	--with-module=clx/new-clx \
	--with-module=gdbm \
	--with-module=pcre \
	--with-module=postgresql \
	--with-module=rawsock \
	--with-module=zlib

%make_build

%install
%makeinstall_std
rm -vfr %buildroot%_libdir/clisp-%version/build-aux/

%find_lang --output=%name.lang --append clisp clisplow

%check
make check

%files -f %name.lang
%_docdir/%name-%version
%_bindir/clisp
%_bindir/clisp-link
%_libdir/clisp-%version
%_datadir/aclocal/clisp.m4
%_man1dir/*

%changelog
* Tue Aug 06 2024 Ivan A. Melnikov <iv@altlinux.org> 1:2.49.92-alt2.1
- Update config.guess and config.sub from current autoconf
  (fixes FTBFS on loongarch64).

* Thu Jul 25 2019 Ivan A. Melnikov <iv@altlinux.org> 1:2.49.92-alt2
- Apply debian patch to fix tests on mipsel.

* Thu Dec 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.49.92-alt1
- 2.49.92 released

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:2.48-alt1.qa1
- NMU: rebuilt with libsigsegv.so.2.

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1:2.48-alt1
- 2.48

* Tue Apr 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1:2.47-alt2
- update requires

* Wed Dec 24 2008 Ilya Mashkin <oddity@altlinux.ru> 1:2.47-alt1
- 2.47
- Dedicated to the 50th birthday of Lisp

* Sat Dec 15 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.43-alt1
- clisp 2.43

* Sat Nov 03 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.42-alt1
- clisp 2.42

* Sat Sep 22 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.41-alt2
- remove Russian summary and description

* Sat Oct 14 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.41-alt1
- clisp 2.41

* Sun Oct 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.40-alt1
- clisp 2.40

* Sun Jul 23 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.39-alt1
- clisp 2.39

* Mon Apr 03 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.38-alt3
- added -falign-functions=4

* Sat Mar 11 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.38-alt2
- check tinfo for tgetent()

* Sat Feb 04 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.38-alt1
- clisp 2.38

* Thu Jan 05 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.37-alt1
- clisp 2.37

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:2.36-alt1.1
- Rebuilt with libreadline.so.5.

* Thu Dec 08 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.36-alt1
- clisp 2.36

* Sat Oct 22 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.35-alt2
- fix for x86_64 build

* Wed Aug 31 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.35-alt1
- clisp 2.35

* Fri Aug 05 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.34-alt1
- clisp 2.34

* Wed Feb 23 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.2-alt4
- rebuild with gcc 3.4.

* Sat Dec 25 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.2-alt3
- another fix for directories.

* Mon Dec 13 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.2-alt2
- fix directories.

* Wed Jul 21 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.2-alt1
- clisp 2.33.2 bugfix release

* Sun Jul 11 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.1-alt2
- full linking set is removed from package since in this build
  it is totally identical to base linking set

* Thu May 27 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33.1-alt1
- clisp 2.33.1

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33-alt2
- Rebuild

* Sat Mar 20 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.33-alt1
- clisp 2.33

* Thu Feb 12 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.32-alt1
- clisp 2.32

* Thu Sep 04 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.31-alt1
- clisp 2.31
- seems to work fine with gcc 3.2

* Tue Aug 26 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.30-alt4cvs20030818
- pass -march -mcpu to configure/makemake via CC

* Tue Aug 19 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.30-alt3cvs20030818
- CVS 08.18.2003

* Sun Jul 20 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.30-alt3cvs20030709
- BuildRequires on libncurses-devel and libreadline-devel

* Wed Jul 16 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.30-alt2cvs20030709
- BuildRequires on gcc2.96

* Wed Jul 09 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.30-alt1cvs20030709
- 2.30 CVS build. Building with gcc 2.96 since gcc 3.2 problem with
  readline is not resolved yet (probably gcc 3.2 bug).

* Wed Oct 23 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:2.29-alt5
- Set Serial: 1 to rollback from 2.30 properly since 2.30 and
  current CVS have problems with readline
- I give up with gcc 3.2 for clisp 2.29 and restore gcc 2.96
  probably we have to wait for more robust post 2.30 clisp release

* Thu Oct 17 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.29-alt4
- patch to build with gcc 3.2

* Sat Oct 12 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.30-alt1csv20021012
- clisp 2.30 CVS 2002.10.12
- floating point bugs are fixed now Maxima with clisp
  passes all tests

* Sat Sep 28 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.30-alt1
- clisp 2.30 without libsigsegv yet
- gcc 3.2

* Wed Sep 25 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.29-alt3
- spec cleanup

* Sat Sep 21 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 2.29-alt2
- gcc-2.96 is required explicitly
- regexp module removed

* Sat Sep 07 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 2.29-alt1
- 2.29

* Thu Mar 28 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 2.28-alt1
- 2.28

* Tue Nov 06 2001 Stanislav Ievlev <inger@altlinux.ru> 2.27-alt3
- rebuilt

* Sun Oct 28 2001 Vadim V. Zhytnikov <vvzhy@mail.ru> 2.27-alt2
- regexp module added

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 2.27-alt1
- 2.27

* Thu Apr 12 2001 Stanislav Ievlev <inger@altlinux.ru> 2.25.1-alt1
- up to 2.25.1

* Thu Jan 04 2001  AEN <aen@logic.ru>
- adopted for RE

* Sun Nov 05 2000 David BAUDENS <baudens@mandrakesoft.com> 2000.03.06-3mdk
- Rewrite spec following Clisp Install documentation to be able to build this
  package on all archs
- Have an intelligent description

* Sun Jul 23 2000 Pixel <pixel@mandrakesoft.com> 2000.03.06-2mdk
- *much* cleanup, macorizaiton, BM

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 2000.03.06-1mdk
- Update to 2000.03.06

* Tue Feb 22 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- rewrote most of .spec file
- updated to 1999.07.22
