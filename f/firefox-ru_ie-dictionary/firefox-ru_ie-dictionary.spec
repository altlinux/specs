%define rname	ru_ie-dictionary
%define cid	ru_dict_without_io@mozilla-russia.org
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	0.1
Release:	alt1
Summary:	Firefox dictionary without russian letter 'yo' support

License:	GPL
Group:		Networking/WWW	
URL:		http://ftp.mozilla-russia.org/dictionaries/

Source0:	%rname.xpi

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox, unzip
Requires: 		%firefox_name >= 2.0

Packager: LAKostis <lakostis@altlinux.ru>

%description
Russian spellchecking dictionary for Firefox without "IO" support.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir
touch %buildroot/%ciddir/chrome.manifest 

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt1
- first build for Sisyphus.

