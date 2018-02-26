Summary: Driver for the Lexmark 2050 printer
Name: c2050
Version: 0.4
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL
URL: http://www.prato.linux.it/~mnencia/lexmark2050

Source:	http://www.prato.linux.it/~mnencia/lexmark2050/%name-%version.tar
Patch: c2050-0.3-mdk-looplimits.patch

%description
Lexmark 2050 Color Jetprinter printer driver.

%prep

%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install

for i in %name ps2lexmark ps2monolexmark; do
%__install -Dpm755 $i %buildroot/%_bindir/$i
done

%files
%doc README COPYING
%_bindir/*


%changelog
* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- Initial build
