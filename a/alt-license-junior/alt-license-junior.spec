Name: alt-license-junior
Version: 0.1
Release: alt2

Summary: Distribution license
License: Distributable
Group: Documentation

Source0: license.ru.html
Source1: license.all.html

Conflicts: alt-license-junior-sl
Conflicts: alt-license-junior-sj
Conflicts: alt-license-junior-sm
Conflicts: alt-license-junior-st

%description
Distribution license

%install
install -d %buildroot%_datadir/alt-license
install -pm0644 %SOURCE0 %SOURCE1 %buildroot/%_datadir/alt-license/

%files
%_datadir/alt-license

%changelog
* Thu Dec 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- school licenses added

* Wed Sep 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial release
