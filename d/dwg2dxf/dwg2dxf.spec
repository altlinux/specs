Name:     dwg2dxf
Version:  2.1
Release:  alt5

Summary:  This program convert DWG files to DXF files
License:  GPL
Group:    Graphics
Url:      http://sourceforge.net/projects/lx-viewer
Packager: Andrey Cherepanov <cas@altlinux.org>
ExclusiveArch: %ix86

Source:   %name-%version.tar.bz2
Patch:    dwg2dxf-2.1-alt-gcc43.patch

BuildRequires: gcc-c++ libstdc++-devel

%description
dwg2fdxf is a command line program that may be used to convert an
AutoCAD drawing file (DWG format) to a Drawing Interchange Format (DXF)
file.

%prep
%setup
%patch -p1

%build
%configure
%make

%install
install -Dm644 dwg2dxf/adinit.dat %buildroot%_libdir/%name/adinit.dat
install -Dm755 dwg2dxf/dwg2dxf %buildroot%_libdir/%name/dwg2dxf
install -d %buildroot%_bindir
cat > %buildroot%_bindir/dwg2dxf <<EOF
#!/bin/sh
%_libdir/%name/%name "\$@"
EOF
chmod 755 %buildroot%_bindir/dwg2dxf

%files
%doc AUTHORS COPYING README dwg2dxf/docs/en
%_bindir/*
%_libdir/%name

%changelog
* Fri Jan 15 2016 Andrey Cherepanov <cas@altlinux.org> 2.1-alt5
- Fix build in Sisyphus (build only i586)

* Wed Oct 29 2008 Igor Vlasenko <viy@altlinux.ru> 2.1-alt4
- fixed build with gcc43

* Wed Feb 01 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt3
- zme'd

* Tue Jan 31 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt2
- picked up; 
- bugfixes; added adinit.dat and docs/en

* Sun Mar 30 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.1-alt1
- First version of RPM package.

