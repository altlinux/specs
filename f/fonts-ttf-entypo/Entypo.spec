Name:		fonts-ttf-entypo
Version:	2014
Release:	alt1
Summary:	Entypo pictograms by Daniel Brucei, www.entypo.com
BuildArch:	noarch
Group:		System/Fonts/True type
URL:		http://www.entypo.com/
PreReq:		fontconfig
BuildRequires:	unzip, rpm-build-fonts
License:	CC-BY-SA 3.0 
Source:		http://dl.dropbox.com/u/4339492/Entypo.zip

%description
Entypo is a set of 250+ carefully crafted pictograms
by Daniel Bruce,  www.entypo.com

%prep
%setup -n Entypo

%install
# TODO pick fontconfig from FC
ln @font-face/*/*ttf .
%ttf_fonts_install Entypo

%files -f Entypo.files
%doc *.rtf

%changelog
* Mon Mar 31 2014 Fr. Br. George <george@altlinux.ru> 2014-alt1
- Initial build from scratch

