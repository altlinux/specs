Summary: Flat assembler
Name: fasm
Version: 1.73.28
Release: alt1
License: BSD-like
Group: Development/Tools
Source0: http://flatassembler.net/%name-%version.tgz
Url: http://flatassembler.net/
ExclusiveArch: %ix86

# Automatically added by buildreq on Wed Feb 08 2017
# optimized out: python-base
BuildRequires: fasm prelink glibc-devel-static

%description
The flat assembler is a fast and efficient self-assembling 80x86
assembler for DOS, Windows and Linux operating systems. Currently it
supports all 8086-80486/Pentium instructions with MMX, SSE, SSE2, SSE3
and 3DNow! extensions, can produce output in binary, MZ, PE, COFF or
ELF format. It includes the powerful but easy to use macroinstruction
support and does multiple passes to optimize the instruction codes for
size. The flat assembler is self-compilable and the full source code
is included.

%prep
%setup -n %name
sed -i 's/fopen/fopen64/g' source/libc/system.inc
sed -i 's/fopen/fopen64/g' tools/libc/system.inc
sed -i 's/cinvoke exit$/cinvoke exit, 0/' examples/elfexe/dynamic/hello.asm
sed -i '/ret$/i xor eax, eax' examples/libcdemo/libcdemo.asm
sed -i 's/gcc libcdemo.o/gcc -static libcdemo.o/' examples/libcdemo/libcdemo.asm

%build
find * -name \*.o -exec rm {} \;
%define FTOOLS listing prepsrc symbols
fasm source/Linux/fasm.asm fasm
for n in %FTOOLS; do
	./fasm tools/libc/$n.asm $n.o
	cc -static $n.o -o $n
	execstack -c $n
done

%install
install -Dm755 %name %buildroot%_bindir/%name
install %FTOOLS %buildroot%_bindir/

%check
./fasm examples/elfexe/hello.asm
examples/elfexe/hello | { read A; test "$A" = 'Hello world!'; }
./fasm examples/elfexe/dynamic/hello.asm
examples/elfexe/dynamic/hello | { read A; test "$A" = 'Hello world!'; }
./fasm examples/elfobj/msgdemo.asm
./fasm examples/elfobj/writemsg.asm
ld examples/elfobj/msgdemo.o examples/elfobj/writemsg.o -o examples/elfobj/msgdemo
examples/elfobj/msgdemo | { read A; test "$A" = 'Elves are coming!'; }
./fasm examples/libcdemo/libcdemo.asm
cc -static examples/libcdemo/libcdemo.o -o examples/libcdemo/libcdemo
examples/libcdemo/libcdemo >o &
wait
read A <o
test "$A" = "Current process ID is $!."

%files
%doc *.txt examples
%_bindir/*

%changelog
* Sun Oct 03 2021 Fr. Br. George <george@altlinux.ru> 1.73.28-alt1
- Autobuild version bump to 1.73.28

* Wed Apr 21 2021 Fr. Br. George <george@altlinux.ru> 1.73.27-alt1
- Autobuild version bump to 1.73.27
- Introduce check section

* Mon Jun 17 2019 Fr. Br. George <george@altlinux.ru> 1.73.12-alt1
- Autobuild version bump to 1.73.12

* Wed Feb 21 2018 Fr. Br. George <george@altlinux.ru> 1.73.02-alt1
- Autobuild version bump to 1.73.02

* Tue Sep 26 2017 Fr. Br. George <george@altlinux.ru> 1.71.64-alt1
- Autobuild version bump to 1.71.64

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 1.71.62-alt1
- Autobuild version bump to 1.71.62

* Wed Feb 08 2017 Fr. Br. George <george@altlinux.ru> 1.71.60-alt1
- Autobuild version bump to 1.71.60
- Package made ix86-only
- Assembler tools added

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.71.57-alt1
- Autobuild version bump to 1.71.57

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 1.71.54-alt1
- Autobuild version bump to 1.71.54

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 1.71.49-alt1
- Autobuild version bump to 1.71.49

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.71.47-alt1
- Autobuild version bump to 1.71.47

* Wed Apr 15 2015 Fr. Br. George <george@altlinux.ru> 1.71.39-alt1
- Autobuild version bump to 1.71.39

* Wed Apr 15 2015 Fr. Br. George <george@altlinux.ru> 1.71.06-6.1
- Initial build for ALT

* Sun Nov 25 2012 Huaren Zhong <huaren.zhong@gmail.com> - 1.71.06
- Rebuild for Fedora
* Sun Aug 29 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.3  2004/08/29 15:17:22  undefine
- update to 1.55
Revision 1.2  2004/08/05 20:02:48  qboosh
- bcond header, pl cosmetics
Revision 1.1  2004/08/05 18:04:26  undefine
- initital rpm version
