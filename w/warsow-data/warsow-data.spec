Name: warsow-data
Version: 2.1
Release: alt1

Summary: Data files for Warsow
Group: Games/Arcade
License: Warsow Data License

Url: http://warsow.net
Source0: warsow_21_unified.tar

BuildArch: noarch

BuildRequires: /usr/bin/dos2unix

%description
Data files for Warsow.

%prep
%setup -q -n warsow_21

dos2unix docs/license.txt

%install
mkdir -p %buildroot%_datadir/warsow
cp -a basewsw %buildroot%_datadir/warsow

%files
%doc docs/license.txt
%dir %_datadir/warsow
%_datadir/warsow/

%changelog
* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Sun Mar 17 2013 Igor Zubkov <icesik@altlinux.org> 1.02-alt1
- 0.61 -> 1.02

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Thu Sep 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux.


