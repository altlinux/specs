%def_enable shared
%def_enable threads
%def_enable load
%def_disable debug
%def_with man
%def_with demos
%def_with x
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define teaname tile
Name: tcl-tile
Version: 0.8.2
Release: alt1
Summary: The Tile Widget Set
License: %mit
Group: Development/Tcl
URL: http://tktable.sourceforge.net
Source: %teaname-%version.tar.bz2
Provides: %teaname = %version-%release

# Automatically added by buildreq on Mon Jan 28 2008
#BuildRequires: libXt-devel tk-devel xorg-cf-files

BuildRequires: tk-devel
%{?_with_x:BuildRequires: libXt-devel xorg-cf-files}
BuildRequires: rpm-build-licenses

%description
The Tile Widget Set is an experimental reimplementation of some of the
core Tk widgets. The primary purpose is to generate ideas for how to
build the next generation of Tk, when the asteroid strikes and we
prepare for the 9.0 release.
Features:
  - A revised and expanded version of the TIP #48 style engine
  - Native look and feel under Windows XP
  - Native L&F under other Windows versions
  - "Revitalized" look and feel under Unix
  - scrollbar, button, checkbutton, radiobutton, menubutton, label,
    frame, and labelframe widgets, plus a partial implementation of the
    scale widget
  - new notebook and progressbar widgets


%package devel
Summary: Headers for development with Tile Widget Set library
Group: Development/Tcl
Provides: %teaname-devel = %version-%release
Requires: %name = %version-%release

%description devel
Headers for development with Tile Widget Set library.


%package doc
Summary: Documentation for the Tile Widget Set
Group: Development/Tcl
Provides: %teaname-doc = %version-%release

%description doc
Documentation for the Tile Widget Set.


%if_with man
%package man
Summary: Man pages for the Tile Widget Set
Group: Development/Tcl
Provides: %teaname-man = %version-%release
Requires: %name = %version

%description man
Man pages for the Tile Widget Set.
%endif


%if_with demos
%package demos
Summary: Demos of the Tile Widget Set
Group: Development/Tcl
Provides: %teaname-demos = %version-%release

%description demos
Demos of the Tile Widget Set.
%endif


%prep
%setup -n %teaname-%version


%build
%configure \
    %{subst_enable shared} \
    %{subst_enable threads} \
    %{subst_enable load} \
    %{subst_enable_to debug symbols} \
%ifarch x86_64
    --enable-64bit \
%endif
    %{subst_with x}

%make_build

bzip2 --best --force --keep -- ChangeLog
bzip2 --best --force --keep -- generic/TODO


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot{%_tcllibdir,%_datadir/tcl/%teaname%version,%_includedir/%teaname,%_docdir/%name-%version/html}
ln -s %name-%version %buildroot%_docdir/%teaname-%version
%if_enabled shared
mv %buildroot%_libdir/%teaname%version/*.so  %buildroot%_tcllibdir/
%else
mv %buildroot%_libdir/%teaname%version/*.a  %buildroot%_tcllibdir/
%endif
mv %buildroot%_libdir/%teaname%version/*.tcl %buildroot%_datadir/tcl/%teaname%version/
mv %buildroot%_includedir/*.h %buildroot%_includedir/%teaname/
%if_with man
install -d -m 0755 %buildroot{%_mandir/manntile,%_man3dir}
pushd doc
for f in *.n; do
    install -m 0644 "$f" %buildroot%_mandir/manntile/"${f}tile"
done
popd
install -m 0644 doc/*.3 %buildroot%_man3dir/
%endif
install -m 0644 *.txt doc/converting.txt generic/TODO.* ChangeLog.* %buildroot%_docdir/%name-%version/
install -m 0644 doc/html/* %buildroot%_docdir/%name-%version/html/
%if_with demos
install -d -m 0755 %buildroot%_datadir/tcl/%teaname%version/demos
install -m 0644 demos/*.tcl %buildroot%_datadir/tcl/%teaname%version/demos/
%endif
rmdir %buildroot%_libdir/%teaname%version
rm -f %buildroot%_libdir/*.a
cat > %buildroot%_tcldatadir/%teaname%version/pkgIndex.tcl <<__INDEX__
if {[catch {package require Tcl 8.4}]} return
package ifneeded %teaname %version [list load [file join %_tcllibdir %teaname%version.so] %teaname]
package ifneeded ttk:dialog 0.8 [list source [file join \$dir dialog.tcl]]
package ifneeded keynav 1.0 [list source [file join \$dir keynav.tcl]]
__INDEX__



%files
%dir %_docdir/%name-%version
%_docdir/%name-%version/*.txt
%{?_enable_shared:%_tcllibdir/*}
%_tcldatadir/%teaname%version


%files devel
%_includedir/%teaname
%{?_disable_shared:%_tcllibdir/*}


%files doc
%_docdir/%teaname-%version
%dir %_docdir/%name-%version
%_docdir/%name-%version/html
%_docdir/%name-%version/converting.txt
%_docdir/%name-%version/TODO.*
%_docdir/%name-%version/ChangeLog.*


%if_with man
%files man
%_mandir/manntile/*
%_man3dir/*
%endif


%if_with demos
%files demos
%_tcldatadir/%teaname%version/demos
%endif


%changelog
* Mon Jan 28 2008 Led <led@altlinux.ru> 0.8.2-alt1
- 0.8.2
- cleaned up spec

* Mon Oct 09 2006 Led <led@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Jun 14 2006 Led <led@altlinux.ru> 0.7.6-alt2
- fixed spec

* Fri Jun 09 2006 Led <led@altlinux.ru> 0.7.6-alt1
- 0.7.6
- fixed spec

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- NMU: new version
- add Url, path to Source, Packager

* Sat Apr 02 2005 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1
- build
