Name:		info2www
Version:	1.2.2.9
Release:	alt1
Summary:	CGI gateway between GNU Info Nodes and the WWW
# See Makefile for real source!
Source:		%name-%version.tar
# Note this version is already patched one
Source1:	%name.pl
URL:		http://packages.debian.org/source/sid/info2www
License:	public domain
Group:		Networking/WWW
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Aug 23 2009
BuildRequires: ImageMagick-tools

%description
The info2www script makes your CGI compliant HTTP/1.0 or later server
a gateway to all that information you have "stacked away" in the
GNU Info Nodes (you know - the Info Nodes accessible from Emacs).

The Info Nodes are parsed and formatted on the fly by info2www and present
hyperlinks to other Info Nodes that your WWW browser can use.

%prep
%setup
cp %SOURCE1 %name
# TODO patch a manual

%build
for N in *.gif; do convert $N ${N%%.*}.png; done
rm *.gif

%install
mkdir -p %buildroot%_datadir/%name
install %name %name.html *.png %buildroot%_datadir/%name/
install -D debian/%name.1 %buildroot%_man1dir/%name.1

%files
%doc README ChangeLog
%dir %_datadir/%name
%_datadir/%name/*
%_man1dir/%name.*

%changelog
* Sun Aug 23 2009 Fr. Br. George <george@altlinux.ru> 1.2.2.9-alt1
- Initial build from scratch

