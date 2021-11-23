Name: unclutter-xfixes
Version: 1.6
Release: alt1.1

Summary: Hides X11 cursor when idle
License: MIT
Group: System/X11
Url: https://github.com/Airblader/unclutter-xfixes
VCS: git://github.com/Airblader/unclutter-xfixes
Source: %name-%version.tar

Conflicts: unclutter

BuildRequires: pkgconfig(x11) pkgconfig(xi) pkgconfig(xfixes) libev-devel asciidoc-a2x

%description
unclutter hides your X mouse cursor when you don't need it, to prevent
it from getting in the way. You have only to move the mouse to restore
the mouse cursor.

unclutter-xfixes is a rewrite of unclutter using the x11-xfixes extension.

%prep
%setup
sed -i -e 's,__VERSION="\$(shell git describe --all --long --always)",__VERSION="%version-%release",' Makefile

%build
make
#make all

%install
make DESTDIR="$RPM_BUILD_ROOT" install

#mkdir -p %buildroot%_bindir %buildroot%_man1dir
#make install install.man BINDIR=%buildroot%_bindir MANDIR=%buildroot%_man1dir

%files
%_bindir/unclutter
%_man1dir/*

%changelog
* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1.1
- fixed url, added vcs

* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1
- new version

* Fri Mar 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- new version

* Thu Dec 31 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus (closes: #31678)
