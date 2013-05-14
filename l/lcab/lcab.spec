Name: lcab
Version: 1.0b12
Release: alt1

Summary: A Cabinet File Creation Tool
License: GPL
Group: Archiving/Other

Url: http://ohnopub.net/~ohnobinki/lcab/
Source: ftp://ohnopublishing.net/mirror/%name-%version.tar.gz
# Source0-md5:	9403e08f53fcf262e25641a9b900d4de

Summary(pl.UTF-8): Program tworzący pliki MS-cab

%description
LCAB is a small program written by Rien <rien/geekshop.be>
that creates an uncompressed MS cabinet files.

%description -l pl.UTF-8
LCAB to mały program tworzący nieskompresowane pliki cabinet
Microsoftu.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pDm644 lcab.1 %buildroot%_man1dir/lcab.1

%files
%doc README
%_bindir/%name
%_man1dir/lcab.1*

%changelog
* Tue May 14 2013 Michael Shigorin <mike@altlinux.org> 1.0b12-alt1
- initial build for ALT Linux Sisyphus
  + based on PLD and fedorapeople specs
