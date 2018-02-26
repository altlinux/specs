Name: mksh
Version: 40b
Release: alt1

Summary: MirBSD enhanced version of the Korn Shell
License: BSD
Group: Shells

URL: http://www.mirbsd.de/mksh.htm

# http://www.mirbsd.org/MirOS/dist/mir/%{name}/%{name}-R%{version}.cpio.gz
Source: %{name}-%{version}.tar

Packager: Alexey Gladkov <legion@altlinux.ru>

%description
mksh is the MirBSD enhanced version of the Public Domain Korn shell (pdksh),
a bourne-compatible shell which is largely similar to the original AT&T Korn
shell. It includes bug fixes and feature improvements in order to produce a
modern, robust shell good for interactive and especially script use, being a
bourne shell replacement, pdksh successor and an alternative to the C shell.

%prep
%setup -q

%build
%add_optflags %optflags_warnings
sh Build.sh -r

%install
install -D -m 755 %name %buildroot/bin/%name
install -D -m 644 %name.1 %buildroot/%_man1dir/%name.1

%files
/bin/%name
%_man1dir/*
%doc dot.mkshrc

%changelog
* Fri Sep 16 2011 Alexey Gladkov <legion@altlinux.ru> 40b-alt1
- new version (R40b).

* Wed Jun 22 2011 Alexey Gladkov <legion@altlinux.ru> 40-alt1
- new version (R40).

* Mon Nov 16 2009 Alexey Gladkov <legion@altlinux.ru> 39-alt1
- new version (R39).

* Tue Mar 04 2008 Alexey Gladkov <legion@altlinux.ru> 33-alt1
- new version (R33).

* Wed Sep 12 2007 Alexey Gladkov <legion@altlinux.ru> 31c-alt1
- new version (R31c).

* Tue Jul 31 2007 Alexey Gladkov <legion@altlinux.ru> 30-alt1
- new version (R30).

* Mon Jul 16 2007 Alexey Gladkov <legion@altlinux.ru> 29g-alt1
- new version (R29g).

* Sun Jul 15 2007 Alexey Gladkov <legion@altlinux.ru> 29f-alt1
- First build ALT Linux.
