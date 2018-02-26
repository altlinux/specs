Name: alt-license-office-server
Version: 0.1
Release: alt1
Packager: Grigory Batalov <bga@altlinux.org>

Summary: Distribution license
License: Distributable
Group: Documentation

BuildArch: noarch

Source0: license.ru.html
Source1: license.all.html

%description
Distribution license

%install
%__install -d %buildroot/%_datadir/alt-license
for i in %SOURCE0 %SOURCE1; do
%__install -pm644 $i %buildroot/%_datadir/alt-license/
done

%files
%_datadir/alt-license


%changelog
* Wed Oct 10 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build
