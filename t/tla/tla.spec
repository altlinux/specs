Name: tla
Version: 1.3.5
Release: alt1.1
#define subver -fix-1
%define subver %nil

Summary: GNU Arch -- revision control system
License: GPL
Group: Development/Other
Url: http://gnuarch.org/
Packager: Alexey Voinov <voins@altlinux.ru>

# ftp://ftp.gnu.org/pub/gnu/gnu-arch/tla-%version%subver.tar.gz
Source: tla-%version%subver.tar
Source1: tla.1
Source2: tla-gpg-check.1

Patch0: tla-1.3.5-neon.patch
Patch1: tla-1.3.5-neon-327111.patch

Requires: diffutils >= 2.8.1, patch, tar
BuildRequires: libneon-devel

%description
Gnu arch is a modern and remarkable revision control system.  It helps
programmers to coordinate and share their changes to a project's
source code.  It helps project managers to organize, track, and control
multi-branch development.  It supports both centralized and distributed
projects.

%package docs
Summary: GNU Arch documentation
Group: Development/Other
BuildArch: noarch

%description docs
GNU Arch documentation in HTML format.

%prep
%setup -q -n %name-%version%subver
%patch0 -p1
%patch1 -p1

# Remove unused code.
rm -rf src/{expat,libneon}

# Fix HTML docs.
find -type f -name \*.html -print0 |
	xargs -r0 grep -lZ '<!--[^>]*>' -- |
	xargs -r0 subst -p '/^[[:space:]]*<!--[^>]*>[[:space:]]*$/ d' --

%build
cd src
mkdir build
cd build
../configure --prefix=%_prefix 
make

%install
install -pD -m755 src/build/tla/tla/tla %buildroot%_bindir/tla
install -pm755 src/tla/=gpg-check.awk %buildroot%_bindir/tla-gpg-check

pushd src/docs-tla/
find -type f '(' -name '*.html' -or -name '*.css' ')' -exec \
	install -pD -m644 '{}' %buildroot%_docdir/%name-%version/'{}' ';'
popd

mkdir -p %buildroot%_man1dir
install -pm644 %_sourcedir/tla{,-gpg-check}.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%files docs
%doc %_docdir/%name-%version/

%changelog
* Wed Jun 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.5-alt1.1
- NMU: rebuild with libneon.so.27

* Sat Apr 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- Updated to 1.3.5.
- Packaged tla-gpg-check
- Imported tla.1 and tla-gpg-check.1 from Debian.

* Thu Jan 05 2006 Alexey Voinov <voins@altlinux.ru> 1.3.4-alt1
- new version (1.3.4)

* Sat Nov 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt2
- Fixed HTML documentation.
- Do not even build libneon.

* Thu Jun 02 2005 Alexey Voinov <voins@altlinux.ru> 1.3.3-alt1
- new version (1.3.3)

* Sun May 22 2005 Alexey Voinov <voins@altlinux.ru> 1.3.2-alt1
- new version (1.3.2)
- nolibneon patch updated
- info pages were removed
- psdocs and htmldocs subpackages removed, docs package created

* Thu Mar 24 2005 Alexey Voinov <voins@altlinux.ru> 1.3.1-alt1
- new version (1.3.1-fix-1)
- nolibneon patch updated

* Wed Jan 12 2005 Alexey Voinov <voins@altlinux.ru> 1.3-alt1
- new version (1.3)
- nolibneon patch updated
- sftpfdleak patch removed
- it now reuqires patch, diffutils, tar.

* Tue Jun 22 2004 Alexey Voinov <voins@altlinux.ru> 1.2-alt6
- packager, description & summary updated
- fd leak in sftp fixed [thanks to dustin@spy.net,
    http://bugs.gnuarch.org/cgi-bin/bugreport.cgi?bug=67]
- added dir entry for info docs
- html & ps docs moved into separate subpackages

* Fri May 14 2004 Alexey Voinov <voins@altlinux.ru> 1.2-alt5
- rebuilt with external libneon

* Tue Apr 13 2004 Alexey Voinov <voins@altlinux.ru> 1.2-alt4
- fix for CAN-2004-0179 in libneon
- explicit packager tag added

* Sat Feb 28 2004 Ott Alex <ott@altlinux.ru> 1.2-alt3
- Release new stable version

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 1.2-alt2.pre2
- Fix Url

* Sat Jan 31 2004 Ott Alex <ott@altlinux.ru> 1.2-alt1.pre2
- Initial build for ALTLinux

