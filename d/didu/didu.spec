Name:		didu
Version:	1.01
Release:	alt1
License:	GPLv3+
URL:		http://git.altlinux.org/people/george/packages/?p=didu.git
Source:		%name-%version.tar
Summary:	corrupted DIsk DUmper utility
Group:		System/Configuration/Hardware
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Fri Apr 10 2009
BuildRequires: help2man

%description
DIskDUmper (didu) is simple dd(1) replacement, much lighter and more standard by options set. The main feature introduced in didu is that bad sectors are not skipped while dumping, but filled with certain byte pattern.

%prep
%setup

%build
%make

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Apr 10 2009 Fr. Br. George <george@altlinux.ru> 1.01-alt1
- Initial Sisyphus build

