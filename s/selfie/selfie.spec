Name:		selfie
# date '+%%y%%m%%d'
# https://github.com/cksystemsteaching/selfie
Version:	180722
Release:	alt1
License:	BSD
Source:		%name-%version.tar
Group:		Education
Summary:	Self-compiling C compiler, a tiny self-executing RISC-V emulator, and a tiny self-hosting RISC-V hypervisor.
ExclusiveArch:	x86_64
URL:		http://selfie.cs.uni-salzburg.at/

%description
The Selfie Project provides an educational platform for teaching
undergraduate and graduate students the design and implementation of
programming languages and runtime systems. The focus is on the
construction of compilers, libraries, operating systems, and even
virtual machine monitors. The common theme is to identify and resolve
self-reference in systems code which is seen as the key challenge when
teaching systems engineering, hence the name.

%prep
%setup

%build
make

%install
install -D -m755 selfie %buildroot%_bindir/selfie

%files
%doc *.md  docs manuscript Makefile
%_bindir/*

%changelog
* Sun Jul 22 2018 Fr. Br. George <george@altlinux.ru> 180722-alt1
- Initial build

