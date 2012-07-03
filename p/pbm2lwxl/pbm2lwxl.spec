Summary: A driver for the CoStar Labelwriter XL

Name: pbm2lwxl
Version: 0
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

License: GPL
Group: Publishing
URL: http://www.freelabs.com/~whitis/software/pbm2lwxl

Source: http://www.freelabs.com/~whitis/software/pbm2lwxl/%name-%version.tar
Patch:	pbm2lwxl-20040515-mdk-path.patch

%description
A driver for the CoStar printers:
 o LabelWriter II
 o LabelWriter XL+
 o Labelwriter XL
 o EL40
 o EL60
 o Turbo
 o SE250
 o SE250+
 o ASCII
 o ASCII+
 o LW300
 o LW330
 o LW330 Turbo

And Avery Printers:
 o Personal Label Printer and Personal Label Printer+???

%prep

%setup -q
%patch -p1

%build
make CFLAGS="%optflags"

%install

for i in pbm2lwxl ps2lwxl txt2lwxl small2lwxl; do
%__install -Dpm755 $i %buildroot/%_bindir/$i
done

%files
%doc README index.html license.html
%_bindir/*

%changelog
* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0-alt1
- Initial build
