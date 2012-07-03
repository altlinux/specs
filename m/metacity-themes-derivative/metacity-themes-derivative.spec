Name: metacity-themes-derivative
Version: 1.0
Release: alt1

Summary: Metacity theme - Derivative
Summary(ru_RU.UTF-8): Тема Derivative для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Derivative.tar.bz2
Requires: metacity
Buildarch: noarch

%description
Like OPENSTEP, only cooler.

%description -l ru_RU.UTF-8
Похоже на OpenStep, но лучше.

%prep
%setup -q -n Derivative

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Derivative/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Derivative/metacity-1 

%files
%_datadir/themes/Derivative/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
