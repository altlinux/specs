Name: alt-license-server
Version: 0.1
Release: alt2

BuildArch: noarch

Summary: Distribution license
License: Distributable
Group: Documentation

Packager: Stanislav Ievlev <inger@altlinux.org>

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
* Fri Oct 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- noarch

* Tue Oct 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
