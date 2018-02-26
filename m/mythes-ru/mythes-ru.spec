Name: mythes-ru
Summary: Russian thesarus
Version: 20061016
Release: alt1
Group: Text tools
License: LGPL

Source0: thes_ru_RU_v2.zip

BuildArch: noarch
BuildRequires: unzip

%description
Russian thesarus.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot/%_datadir/mythes
install -m644 th_ru_RU_v2.* %buildroot/%_datadir/mythes

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20061016-alt1
- initial release

