Summary: Flat assembler
Name: fasm
Version: 1.71.57
Release: alt1
License: distributable
Group: Development/Tools
Source0: http://flatassembler.net/%name-%version.tgz
Url: http://flatassembler.net/

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

%build
cd source/Linux
../../%name %name.asm

%install
install -Dm755 source/Linux/%name %buildroot%_bindir/%name

%files
%doc *.txt examples tools
%_bindir/*

%changelog
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
