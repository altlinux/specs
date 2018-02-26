Name: metacity-themes-helix-sweetpill
Version: 1.0
Release: alt1

Summary: Metacity themes - HeliX-Sweetpill
Summary(ru_RU.UTF-8): Темы HeliX-Sweetpill для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: HeliX-Sweetpill.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains HeliX-Sweetpill themes for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит набор тем HeliX-Sweetpill для диспетчера окон Metacity.

%prep
%setup -q -n HeliX-Sweetpill

%install
for dir in $(ls); do
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/$dir/metacity-1 
%__install -m644 -p $dir/metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/$dir/metacity-1 
done

%files
%_datadir/themes/*/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
