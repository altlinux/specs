
Name:		freebasic
Version:	0.90.1
Release:	alt2

Summary:	FreeBASIC language compiler
License:	GPL
Group:		Education

Source:		FreeBASIC-v%{version}-linux.tar.gz
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
ExclusiveArch:  %ix86

Requires:  gcc
Requires:  libstdc++-devel

%description	
FreeBASIC - is a completely free, open-source, 32-bit BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%prep
%setup -q -n FreeBASIC

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

%files
%doc *.txt
%_bindir/fbc
%_libdir/freebasic/
%_includedir/freebasic/
%_datadir/freebasic/
%_man1dir/*

%changelog
* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt2
- Rebuild from sources
- Pack fbc man page and examples

* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt1
- Build for Sisyphus (bootstrap)
