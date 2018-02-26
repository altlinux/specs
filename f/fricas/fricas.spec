Name: fricas
Version: 1.1.6
Release: alt1

Summary: FriCAS Computer Algebra System
License: Modified BSD License
Group: Sciences/Mathematics
Url: http://fricas.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: fricas-%version-full.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name.desktop

Requires: sbcl = 1.0.56

Conflicts: axiom

BuildRequires: libXpm-devel libXpm clisp
BuildRequires: /proc
BuildRequires: sbcl = 1.0.56

%description
FriCAS is an advanced computer algebra system. Its capabilities range 
from calculus (integration and differentiation) to abstract algebra. 
It can plot functions and has integrated help system.
 
FriCAS a fork of Axiom project -- its starting point was wh-sandbox 
branch of the Axiom project.

%prep 
%setup -q -n %name-%version

%build

#configure --with-lisp=sbcl
%configure --with-lisp=clisp
make

%install
%define _strip_method no

#mkdir -p %buildroot%_libdir/fricas
#mkdir -p %buildroot%_libdir/fricas/emacs

make install DESTDIR=%buildroot

#install -D -m644 ??? %buildroot%_bindir/axiom
#install -D -m644 ??? %_libdir/axiom/*



# icons
install -D -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

# menu items
install -D -m644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

#__subst "s:%buildroot/usr:/usr:g" %buildroot%_bindir/axiom   


%files
%_bindir/*
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_libdir/%name/*
%doc README FAQ CHA* Cha*


%changelog

* Fri Apr 27 2012 Ilya Mashkin <oddity@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Jan 06 2012 Ilya Mashkin <oddity@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Wed Sep 14 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.3-alt2
- rebuild with sbcl 1.0.51

* Mon Aug 15 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Mon Jun 13 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt2
- rebuild with sbcl 1.0.49

* Sat Mar 26 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt3
- rebuild with sbcl 1.0.45

* Mon Feb 14 2011 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt2
- rebuild

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt0.M51.1
- Build for 5.1

* Wed Nov 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Oct 30 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6.5
- rebuild with sbcl 1.0.42

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6.4
- rebuild with sbcl 1.0.33

* Fri Oct 30 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6.3
- rebuild with sbcl 1.0.32

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6.2
- rebuild with sbcl 1.0.30
- fix desktop file
- fix icons locations

* Wed Jul 29 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6.1
- fix requires

* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt6
- rebuild with sbcl 1.0.29

* Tue Mar 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt5
- build with clisp instead of sbcl 1.0.25

* Sun Jan 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt4
- rebuild with sbcl 1.0.24

* Wed Dec 17 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt3
- rebuild with sbcl 1.0.23
- apply repocop patch

* Tue Jan 08 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt2
- Correct libdir for x86_64.

* Mon Jan 07 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt1
- First ALT Linux build.



