Name:		freebasic
Version:	1.05.0
Release:	alt1

Summary:	FreeBASIC language compiler
License:	GPLv2+ and LGPLv2+ with exception
Group:		Education

Source:		FreeBASIC-%version-source.tar.gz
Source1:	FB-manual-%version-html.zip
URL: 		http://freebasic.net
#VCS:           https://github.com/freebasic/fbc

Provides:	FreeBASIC = %version-%release
%ifarch x86_64
Provides:	i586-freebasic = %version-%release
Obsoletes:	i586-freebasic < %version-%release
%endif

BuildRequires:  freebasic
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  libgpm-devel
BuildRequires:  libGL-devel
BuildRequires:  libncurses-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  zlib-devel
BuildRequires:  unzip

Requires: 	gcc

%description	
FreeBASIC - is a completely free, open-source, 32-bit BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%prep
%setup -q -n FreeBASIC-%version-source
mkdir doc/html
unzip -q %SOURCE1 -d doc/html
ln -s 00index.html doc/html/index.html

%build
%make_build FBCFLAGS="-i /usr/include/freebasic" FBLFLAGS="-p %_libdir/freebasic -prefix %_prefix"

%install
mkdir -p %buildroot%_prefix
%makeinstall_std prefix=%buildroot%_prefix

# Install man page
install -D doc/fbc.1 %buildroot%_man1dir/fbc.1

# Install examples
mkdir -p %buildroot%_datadir/freebasic
cp -a examples %buildroot%_datadir/freebasic

# Install manual
mkdir -p %buildroot%_docdir/freebasic
cp -a doc/html/* %buildroot%_docdir/freebasic

%check
#make -C tests log-tests FB_LANG=fb || /bin/true

%files
%doc *.txt
%_bindir/fbc
%_includedir/freebasic/
%_libexecdir/freebasic/
%_datadir/freebasic/
%doc %_docdir/freebasic
%_man1dir/*

%changelog
* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.05.0-alt1
- New version

* Wed Aug 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.03.0-alt1
- New version 1.03.0

* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt2
- Replace old i586-freebasic

* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt1
- Rebuild in bootstrapped arch

* Tue Apr 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt0.1
- New version
- Bootstrap for x86_64 version
- Disable tests

* Wed Nov 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt6
- Simplify build parameters
- Remove deprecated linker flags

* Tue Nov 19 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt5
- Supress linking warnings on 64-bit systems
- Fix strict version in library symlinks

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt4
- Remove fbhelp binary and its help file
- Add missing libraries

* Thu Nov 14 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt3
- Set required libraries in Arepo
- Build fbhelp
- Pack documentation

* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt2
- Rebuild from sources
- Pack fbc man page and examples

* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt1
- Build for Sisyphus (bootstrap)
