Name: metacity-themes-finalstep
Version: 1.0
Release: alt1

Summary: Metacity theme - FinalStep
Summary(ru_RU.UTF-8): Тема FinalStep для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: FinalStep.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains FinalStep theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему FinalStep для диспетчера окон Metacity.

%prep
%setup -q -n FinalStep

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/FinalStep/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/FinalStep/metacity-1 

%files
%_datadir/themes/FinalStep/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
