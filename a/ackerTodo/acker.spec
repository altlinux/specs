Name: ackerTodo
Version: 4.0
Release: alt1
License: GPL
Summary: TODO list manager (web based)
Group: Networking/Other
URL: http://ackertodo.sourceforge.net/site2/download.html
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version.tar.bz2
Patch0: ackerTodo.patch
BuildArch: noarch

%description
ackerTodo is a light-weight web based todo list manager written 
by Rob Hensley that supports multiple users, groups, categories, 
super categories, recurring tasks (Daily, Weekly, Monthly, Yearly,
Open-Ended), modules, a CLI interface, email notification, file
upload capabilites, and many more features. It is also available
in 15 different languages.


%prep
%setup
%patch0 -p0

%build

#install

mkdir -p %buildroot/var/www/html/%name
cp -a src/* %buildroot/var/www/html/%name

%files
%doc CREDITS ChangeLog README TODO UPGRADE
/var/www/html/%name


%changelog
* Mon Sep 11 2006 Mikhail Pokidko <pma@altlinux.ru> 4.0-alt1
- Initial build

