Name: warsow-data
Version: 0.61
Release: alt1
Summary: Data files for Warsow

Group: Games/Arcade
License: Warsow Data License

Url: http://warsow.net
Source0: %name-%version.tar

BuildArch: noarch

%description
Data files for Warsow.

%prep
%setup -q -n %name-%version

%install

mkdir -p %buildroot%_datadir/games/warsow
cp -a basewsw %buildroot%_datadir/games/warsow

%files
%doc docs/license.txt
%_datadir/games/warsow/basewsw

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Thu Sep 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux.


