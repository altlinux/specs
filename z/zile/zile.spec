Name: zile
Version: 2.4.5
Release: alt1

Summary: zile - emacs-like editor
License: GPL
Group: Editors
Url: http://zile.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2005
BuildRequires: libncurses-devel libtinfo-devel libgc-devel

%description
Zile (emacs-like) editor. 

%prep
%setup -q

%build
%configure
%make_build 

%install
%make_install DESTDIR=%buildroot install

%files
#dir %_datadir/zile

%_bindir/*
#_infodir/*
%_man1dir/*
%_datadir/doc/zile/*


%changelog
* Wed Feb 15 2012 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Mon Nov 21 2011 Ilya Mashkin <oddity@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Fri Mar 18 2011 Ilya Mashkin <oddity@altlinux.ru> 2.3.23-alt1
- 2.3.23

* Thu Nov 11 2010 Ilya Mashkin <oddity@altlinux.ru> 2.3.20-alt1
- 2.3.20

* Fri Jul 23 2010 Ilya Mashkin <oddity@altlinux.ru> 2.3.18-alt1
- 2.3.18

* Sat Dec 26 2009 Ilya Mashkin <oddity@altlinux.ru> 2.3.14-alt1
- 2.3.14

* Tue Oct 18 2005 Pavel Mironchik <tibor@altlinux.ru> 2.2.8-alt1
- new release


