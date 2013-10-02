Name:		freebasic
Version:	0.90.1
Release:	alt1

Summary:	FreeBASIC language compiler
License:	GPL
Group:		Education

Source:		FreeBASIC-v%{version}-linux.tar.gz
URL: 		http://freebasic.net

ExclusiveArch: 	%ix86

%description	
FreeBASIC - is a completely free, open-source, 32-bit BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%prep
%setup -q -n FreeBASIC

%install
mkdir -p %buildroot%_man1dir/
./install.sh -i %buildroot/usr
mv %buildroot/usr/man/man1/fbc.1.gz %buildroot%_man1dir/

%files
%_bindir/fbc
%_libdir/freebasic/
%_includedir/freebasic/
%_man1dir/fbc*

%changelog
* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt1
- Build for Sisyphus (bootstrap)
