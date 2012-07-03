
%define subver 20050907
Name: poster
Version: 1.0.1
Release: alt3.%subver

Group: Publishing
Summary: An utility to scale postscript
Url: http://printing.kde.org
#Url: http://www.ctan.org/tex-archive/support/poster/
License: GPL

Source0: %name-%subver.tar.bz2

Patch1: poster_20050907-1.diff


# Automatically added by buildreq on Thu Sep 11 2008 (-bi)
BuildRequires: libpaper-devel

%description
Poster is utility to scale postscript
images to a larger size, and print them on larger media and/or
tile them to print on multiple sheets.
With respect to the earlier release:
- support is added for foreign (Non European A*) media sizes.
- options for scaling became more flexible
- original restrictions on white margins in your drawing are removed

%prep
%setup -q -n %name-%subver
%patch1 -p1


%build
%make CFLAGS="%optflags"


%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_man1dir

install -m 755 %name %buildroot/%_bindir
install -m 544 %{name}.1 %buildroot/%_man1dir


%files
%doc README*
%_bindir/*
%_man1dir/*


%changelog
* Thu Sep 11 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt3.20050907
- fix #16590
- revert to 20050907
- apply patch from Debian (thanks stanv@alt for link)

* Tue Oct 02 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt2.20060221
- new release (20060221)

* Wed Sep 10 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version
- url changed

* Wed Jan 29 2003 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt2
- rebuild with gcc3.2

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- initial spec

