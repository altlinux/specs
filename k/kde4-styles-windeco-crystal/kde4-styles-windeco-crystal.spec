%define _unpackaged_files_terminate_build 1

%define base_name	kde4-styles-windeco
%define theme_name	crystal
%define name		%base_name-%theme_name
%define kdeid		75140

Name: %name
Version: 2.0.5
Release: alt1

Group: Graphical desktop/KDE
Summary: Crystal style for KDE4
License: GPL
Url: http://kde-look.org/content/show.php?content=%kdeid

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %kdeid-%theme_name-%version.tar.bz2

BuildPreReq: gcc-c++ kde4base-workspace-devel

%description
This is the port of the famous Crystal kwin decoration theme to KDE 4.x.

%prep
%setup -n %theme_name-%version

%build
%K4build

%install
%K4install

%files
%doc AUTHORS README
%_K4lib/*.so
%_K4apps/kwin/*.desktop

%changelog
* Fri Aug 14 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Wed Aug 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Sun Feb 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Fri Dec 19 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sat Aug 23 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.1-alt1
- initial build
