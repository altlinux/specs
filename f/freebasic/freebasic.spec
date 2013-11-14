
Name:		freebasic
Version:	0.90.1
Release:	alt3

Summary:	FreeBASIC language compiler
License:	GPL
Group:		Education

Source:		FreeBASIC-v%{version}-linux.tar.gz
Source1:	FB-manual-%version-fbhelp.zip
Source2:	FB-manual-%version-html.zip
URL: 		http://freebasic.net

Provides:	FreeBASIC = %version-%release

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
ExclusiveArch:  %ix86

Requires:  gcc
#Requires:  libstdc++-devel

%description	
FreeBASIC - is a completely free, open-source, 32-bit BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%prep
%setup -q -n FreeBASIC
unzip -q %SOURCE1 -d doc
mkdir doc/html
unzip -q %SOURCE2 -d doc/html

%build
%make_build FBCFLAGS="-i /usr/include/freebasic" FBLFLAGS="-p %_libdir/freebasic -prefix %_prefix"
# Make documentation
make -C doc/fbhelp TARGET=linux FBCFLAGS="-i /usr/include/freebasic -p %_libdir/freebasic -prefix %_prefix"

%install
mkdir -p %buildroot%_prefix
%makeinstall_std prefix=%buildroot%_prefix

# Install man page
install -D doc/fbc.1 %buildroot%_man1dir/fbc.1

# Install examples
mkdir -p %buildroot%_datadir/freebasic
cp -a examples %buildroot%_datadir/freebasic

# Make symlinks for set Arepo requires
ldd bin/fbc | sed -ne 's/^[[:space:]]*\(lib[^ ]*\.so\).*$/\1/p' | xargs -ri ln -s /usr/lib/{} %buildroot/usr/lib/freebasic/

# Install fbhelp and manual
install -D -m 0755 doc/fbhelp/fbhelp %buildroot%_bindir/fbhelp
mkdir -p %buildroot%_docdir/freebasic
cp -a doc/fbhelp.daz doc/html %buildroot%_docdir/freebasic

%check
make -C tests log-tests FB_LANG=fb || /bin/true

%files
%doc *.txt
%_bindir/fbc
%_bindir/fbhelp
%_libdir/freebasic/
%_includedir/freebasic/
%_datadir/freebasic/
%doc %_docdir/freebasic
%doc %_man1dir/*

%changelog
* Thu Nov 14 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt3
- Set required libraries in Arepo
- Build fbhelp
- Pack documentation

* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt2
- Rebuild from sources
- Pack fbc man page and examples

* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt1
- Build for Sisyphus (bootstrap)
