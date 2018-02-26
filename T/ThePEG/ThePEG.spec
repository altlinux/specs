# -*- mode: rpm-spec; mode: folding -*-
# vim: set ft=spec:
# vim600: set fdm=marker:


Name:         ThePEG
Version:      1.5.0
Release:      alt3

Summary:      Toolkit for High Energy Physics Event Generation.
License:      GPL
Group:        Sciences/Physics
Url:	      http://projects.hepforge.org/thepeg

Source:	      %name-%version.tar.gz
Source1:      thepeg.png

BuildRequires: gcc-c++ libgsl-devel libreadline-devel 
BuildRequires: java-devel-default

%description
%summary

%package devel
Summary: Toolkit for High Energy Physics Event Generation development files.
Group:   Development/C++
Requires: %name = %version-%release

%description devel
%summary devel

%package gui
Summary: Toolkit for High Energy Physics Event Generation java GUI.
Group:   Sciences/Physics
Requires: %name = %version-%release

%description gui
%summary gui

%prep
%setup -q

%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%configure --with-javagui
%make 

%install
%makeinstall_std

pushd %buildroot%_bindir
for i in *; do
    sed -i s,%buildroot,,g $i
done
popd

install -D -m755 %{SOURCE1} %buildroot%_liconsdir/thepeg.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << 'EOF'
[Desktop Entry]
Terminal=false
Icon=thepeg
Type=Application
Categories=Education;Science;Physics;
Exec=thepeg
Name=The PEG
EOF

%files
%_bindir/runThePEG
%_bindir/setupThePEG
%dir %_datadir/ThePEG
%dir %_datadir/ThePEG/Doc
%_datadir/ThePEG/Doc/fixinterfaces.pl
%_datadir/ThePEG/Doc/refman.h
%_datadir/ThePEG/Doc/refman.conf
%_datadir/ThePEG/Doc/MakeDocs.in
%_datadir/ThePEG/Doc/repository.hlp
%_datadir/ThePEG/MultiLEP.in
%_datadir/ThePEG/TestLHAPDF.in
%_datadir/ThePEG/debugItems.txt
%_datadir/ThePEG/ThePEGParticles.in
%_datadir/ThePEG/LHAPDFDefaults.in
%_datadir/ThePEG/ThePEGDefaults.in
%_datadir/ThePEG/SimpleLEP.in
%_datadir/ThePEG/ThePEG.el
%_datadir/ThePEG/PDFsets.index
%dir %_libdir/ThePEG
%_libdir/ThePEG/ThePEGDefaults-1.5.0.rpo
%_libdir/ThePEG/runThePEG-1.5.0.bin
%_libdir/ThePEG/setupThePEG-1.5.0.bin
%_libdir/ThePEG/setupThePEG.bin
%_libdir/ThePEG/runThePEG.bin
%_libdir/ThePEG/ThePEGDefaults.rpo
%_libdir/ThePEG/*.so.*
%exclude %_libdir/ThePEG/libtool
%exclude %_libdir/ThePEG/Makefile
%exclude %_libdir/ThePEG/Makefile.common

%files devel
%_includedir/ThePEG
%_libdir/ThePEG/*.so
# we need them now due to non-standard library location
%_libdir/ThePEG/*.la

%files gui
%_bindir/thepeg
%_libdir/ThePEG/ThePEG.jar
%_liconsdir/thepeg.png
%_desktopdir/%name.desktop

%changelog
* Fri Oct 23 2009 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3
- add *.la due to the non-standard lib location.

* Fri Oct 23 2009 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2
- fixed .desktop

* Thu Oct 22 2009 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- first build for Sisyphus

