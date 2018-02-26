%define		_name		claws-mail
%define     theme_name	TangoClaws
Name:		%_name-theme-%theme_name
Version: 0.3
Release: alt2

Summary:	Tango theme for Claws Mail
License: 	GPL
Group: 		Networking/Mail	

Url:		http://www.claws-mail.org/themes.php
Source:		http://www.claws-mail.org/themes/%_name-theme_%theme_name-%version.tar.gz

BuildArch: 	noarch
PreReq: 	%_name

%description
Tango theme for Claws Mail.

%prep
%setup -q -n %theme_name-%version

%build

%install
mkdir -p %buildroot%_datadir/%_name/themes
cp -a ./ %buildroot%_datadir/%_name/themes/%theme_name
rm -f %buildroot%_datadir/%_name/themes/%theme_name/{README,INSTALL}

%files
%doc	README
%dir %_datadir/%_name/themes/%theme_name
%_datadir/%_name/themes/%theme_name/*.xpm
%_datadir/%_name/themes/%theme_name/.*_themeinfo

%changelog
* Sat Feb 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt2
- fixed .*_themeinfo files that were unpackaged without any warning.

* Fri Feb 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt1
- initial version (0.3)

