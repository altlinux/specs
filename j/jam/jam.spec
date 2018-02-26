Name: jam
Version: 2.5
Release: alt1

Summary: Jam is a powerful and highly customizable utility to build programs.
License: GPL
Group: Development/C
Url: http://www.perforce.com

Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: %name-%version.tar.bz2

Conflicts: boost-jam

%description
Jam is a make(1) replacement that makes building simple things 
simple and building complicated things manageable.

%prep 
%setup -q -n %name

%build
%make

%install
mkdir -p %buildroot%_bindir

./jam0 -sBINDIR=%buildroot%_bindir -sCCFLAGS=-g -sOPTIM=-O2 install

%files
%doc README RELNOTES Porting
%_bindir/jam

%changelog
* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.5-alt1
- Initial build for Sisyphus.

