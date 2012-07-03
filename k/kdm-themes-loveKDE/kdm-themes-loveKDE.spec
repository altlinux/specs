%define pkgname loveKDE

Name: kdm-themes-%pkgname
Version: 0.1
Release: alt1
Summary: KDM Theme based on moodwrod's "LoveKDE" Splash Screen 
License: GPL 
Group: Graphical desktop/KDE
Url: http://kde-look.org/content/show.php/LoveKDE+KDM+Theme?content=35843

Buildarch: noarch
Packager: Lebedev Sergey <barabashka@altlinux.org>

Source: kdm-themes-%pkgname-%version.tar
Patch: %name-%version-%release.patch


%description
KDM Theme based on moodwrod's "LoveKDE" Splash Screen 
(you can find it at http://www.kde-look.org/content/show.php?content=25945).


%prep
%setup -q 
%patch -p1

%build

%install
%__install -d -m 755 %buildroot%_datadir/apps/kdm/themes/loveKDE
%__install -d -m 755 %buildroot%_docdir
%__install -D -m 644 *.png  %buildroot%_datadir/apps/kdm/themes/loveKDE
%__install -D -m 644 *.jpg  %buildroot%_datadir/apps/kdm/themes/loveKDE
%__install -D -m 644 KdmGreeterTheme.desktop %buildroot%_datadir/apps/kdm/themes/loveKDE
%__install -D -m 644 LoveKDE.xml %buildroot%_datadir/apps/kdm/themes/loveKDE

%files
%doc GdmGreeterTheme.desktop COPYING
%_datadir/apps/kdm/themes/loveKDE/*

%changelog
* Thu Jan 31 2008 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1
-  first build
