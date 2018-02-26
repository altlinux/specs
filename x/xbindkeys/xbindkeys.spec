%def_enable guile

Name: xbindkeys
Version: 1.8.4
Release: alt1

Summary: Binds keys or mouse buttons to shell commands under X
License: GPLv2+
Group: System/Configuration/Other

Packager: Terechkov Evgenii <evg@altlinux.org>

URL: http://www.nongnu.org/xbindkeys/xbindkeys.html
Source0: %name-%version.tar

BuildPreReq: libX11-devel
%if_enabled guile
BuildPreReq: guile-devel
%endif

%description
xbindkeys is a program that allows you to launch shell commands with your
keyboard or mouse under X. It links commands to keys or mouse buttons using
a simple configuration file, and is independant of the window manager.

%prep
%setup

%build
# --enable-tk == install xbindkeys_show to %_bindir
# but we install it to %_docdir manually, so we need --disable-tk
%configure %{subst_enable guile} --disable-tk
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS BUGS ChangeLog README TODO xbindkeys_show*

%changelog
* Tue Dec  7 2010 Terechkov Evgenii <evg@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Feb 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Fri Apr 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Thu Apr 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Feb 06 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.0-alt1.1
- rebuild

* Sun Jan 21 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.0-alt1
- 1.8.0
- enabled guile support

* Fri Jan 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Sun May 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Sun May 08 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.2-alt1
- 1.7.2
- %%ifdef'ed guile support, still disabled by default
- packaged xbindkeys_show and its manpage as %%doc

* Wed Dec 22 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.1-alt1
- built for Sisyphus
