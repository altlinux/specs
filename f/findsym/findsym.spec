Name: findsym
Version: 1.2
Release: alt1

Summary: Search through all your shared libraries for a specific symbol
Group: Development/Other
License: GPL
# Seems to be dead...
#Url: http://meatloop.andover.net/~count/src/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

BuildRequires: help2man

Source: %name-%version.tar

%description
This program will attempt to search through all your shared libraries
for a specific symbol.  This is useful when trying to compile something
and the compiler complains about an undefined reference similar to this:

/tmp/cceuy0nE.o(.text+0x7): undefined reference to `foo'

Running "%name foo" would try to locate the symbol foo and indicate
what library you should be linking with.

%prep
%setup -q

%build
%make_build

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Sun Aug 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Cleaned up new shell implementation.
- Implemented -C/--demangle option.
- Added manpage.

* Fri Aug 04 2006 Sir Raorn <raorn@altlinux.ru> 1.1.1-alt1.1
- Really fixed x86_64.

* Fri Aug 04 2006 Sir Raorn <raorn@altlinux.ru> 1.1.1-alt1
- NMU: 1.1.1
 + Rewritten in shell (speedup up to 4.5 times)
 + Works on x86_64 (closes: #9557)
 + Can search more than one symbol at a time
- Minor spec cleanup
- Added Packager tag

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- 1.1

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- RE adaptions.

* Thu Jul 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-1ipl
- 1.0
- Initial revision.
