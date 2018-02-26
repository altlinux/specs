%define		packname symbols
%define		origname symbols

%define		imagedir %_datadir/nagios/images/logos/%packname
Name:		nagios-imagepack-%packname
Version:	1.1
Release:	alt1
Summary:	%packname image pack for Nagios
License:	GPL
Group:		Graphics
URL:		http://www.nagiosexchange.org/
Source:		%origname-v%version.tar.gz
Requires:	nagios
BuildArch:	noarch

%description
This package contains %packname image pack for Nagios.

%prep
%setup -n %origname

%install
install -d %buildroot%imagedir
shopt -s nullglob
for image in *.{gif,GIF,jpg,JPG,jpeg,JPEG,png,PNG,gd2,GD2}; do
	install -m 644 $image %buildroot%imagedir
done

%files
%dir  %imagedir
%imagedir/*

%changelog
* Fri Dec 16 2005 Denis Ovsienko <pilot@altlinux.ru> 1.1-alt1
- initial ALTLinux build
