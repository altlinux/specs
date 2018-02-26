Name: xmedcon
Version: 0.10.5
Release: alt5.1

Summary: A medical image conversion utility and library
License: (L)GPL
Group: Graphics

Url: http://xmedcon.sourceforge.net

Packager: Andrey Yurkovsky <anyr@altlinux.org>

Source0: %name-%version.tar.bz2
Source1: %name.desktop
Source2: %name.png

BuildRequires: gcc-c++ libgtk+2-devel libpng-devel

%description
This project stands for Medical Image Conversion and is released under the
GNU's (L)GPL license. It bundles the C sourcecode, a library, a flexible
command-line utility and a graphical front-end based on the amazing Gtk+
toolkit.

Its main purpose is image conversion while preserving valuable medical
study information. The currently supported formats are: Acr/Nema 2.0,
Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7, InterFile 3.3
and PNG or Gif87a/89a towards desktop applications.

%package devel
Summary: Static libraries and header files for (X)MedCon development
Group: Development/C
Requires: xmedcon = %version-%release

%description devel

The xmedcon-devel package contains the header files and static libraries
necessary for developing programs that make use of the (X)MedCon library
(libmdc).

%prep
%setup -q

%build
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall
%__install -pD -m744 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%__install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.png
%files
%_bindir/*
%_libdir/*so.*
%_sysconfdir/*
%_man1dir/*
%_liconsdir/%name.png
%_datadir/applications/%name.desktop
%doc ChangeLog COPYING COPYING.LIB README REMARKS AUTHORS

%files devel
%doc README COPYING COPYING.LIB
%_man3dir/*
%_man4dir/*
%_includedir/*
%_libdir/*.a
%_libdir/*.so
%_datadir/aclocal/*

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.5-alt5.1
- Removed bad RPATH

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.5-alt5
- fix build

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.5-alt4.1
- Rebuilt for soname set-versions

* Wed Feb 10 2010 Andrey Yurkovsky <anyr@altlinux.org> 0.10.5-alt4
- rename xmedcon-devel-static to xmedcon-devel

* Wed Nov 25 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.10.5-alt3
- added semicolon (';') as trailing character in desktop file
- %_sysconfdir/* in spec changed to %config %_sysconfdir/*

* Thu Nov 19 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.10.5-alt2
- added desktop and icon files

* Thu Nov 19 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.10.5-alt1
- NIFTI: missing feature added to use slice spacing as slice width
- NIFTI: using nifticlib Version 1.1.0 beta release Aug 2008
- NIFTI: fixed reading for headers with dimensions set to zero
- DICOM: bug writing 8-bit images with odd area
- configure: build LSB friendly; install in /usr & /etc (cfr. OpenSuSE)

* Tue Nov 18 2008 Alexei Mezin <alexei_vm-at-altlinux-dot-ru> 0.10.4-alt1
- Initial build
