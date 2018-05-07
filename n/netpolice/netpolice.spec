Name: netpolice
Version: 1.02
Release: alt3.1
Packager: Anton Pischulin <letanton@altlinux.ru>

Summary: Netpolice is content filtering system
License: BSD
Group: System/Servers
Url: http://www.netpolice.ru/

Source0: readme

%description
Netpolice is content filtering system.

%package -n %name-main
Summary: netpolice meta package
Group: System/Servers 
Requires: squid >= 3.0
Requires: memcached
Requires: c-icap 
Requires: netpolice-filter
Requires: squid-conf-host2cat >= 1.01
Requires: host2cat >= 1.01

%description -n %name-main
This package is meta package for %name.

%install
mkdir -p %buildroot%_docdir
install -pD -m644 %SOURCE0 %buildroot%_docdir/%name/%name

%files -n %name-main
%doc %_docdir/%name/%name

%changelog
* Mon May 07 2018 Grigory Ustinov <grenka@altlinux.org> 1.02-alt3.1
- NMU: Fix description (Closes: #26373).

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.02-alt3
- Rebuild with new version if c-icap

* Thu Nov 11 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt2.2
- Fix changelog.

* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt2.1
- Update spec.

* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt1
- Initial ALTLinux release.
