Name: netpolice
Version: 1.02
Release: alt2.2
Packager: Anton Pischulin <letanton@altlinux.ru>

Summary: Netpolice is content filtering system
License: BSD
Group: System/Servers
Url: http://www.netpolice.ru/

Source0: readme

%description
Netpolice is content filtering system.

Requires: %name = %version-%release

%package -n %name-main
Summary: netpolice meta package
Group: System/Servers 
Requires: squid >= 3.0
Requires: memcached
Requires: c-icap >= 20080706.01
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
* Thu Nov 11 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt2.2
- Fix changelog.

* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt2.1
- Update spec.

* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.02-alt1
- Initial ALTLinux release.
