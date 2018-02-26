Name: alt-license-junior-sl
Version: 0.1
Release: alt2

Summary: Distribution license
License: Distributable
Group: Documentation

Source0: license.sl.ru.html
Source1: license.all.html

Conflicts: alt-license-junior
Conflicts: alt-license-junior-sj
Conflicts: alt-license-junior-sm
Conflicts: alt-license-junior-st

%description
Distribution license

%install
install -pm0644 -D %SOURCE0 %buildroot/%_datadir/alt-license/license.ru.html
install -pm0644 %SOURCE1 %buildroot/%_datadir/alt-license

%files
%_datadir/alt-license

%changelog
* Thu Dec 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- school licenses added

* Wed Sep 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial release
