Name: warsow-data
Version: 1.02
Release: alt1

Summary: Data files for Warsow
Group: Games/Arcade
License: Warsow Data License

Url: http://warsow.net
Source0: warsow_%{version}.tar.gz

BuildArch: noarch

%description
Data files for Warsow.

%prep
%setup -q -n warsow_%{version}

%install
mkdir -p %buildroot%_datadir/warsow
cp -a basewsw %buildroot%_datadir/warsow

%files
%doc docs/license.txt
%dir %_datadir/warsow
%_datadir/warsow/

%changelog
* Sun Mar 17 2013 Igor Zubkov <icesik@altlinux.org> 1.02-alt1
- 0.61 -> 1.02

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Thu Sep 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux.


