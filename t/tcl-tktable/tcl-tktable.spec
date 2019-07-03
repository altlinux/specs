%define teaname Tktable
%define	major 2.10

Name: tcl-tktable
Version: 2.10
Release: alt1

Summary: tkTable - table/matrix widget extension to Tcl/Tk.
License: BSD
Group: System/Libraries
Url: http://tktable.sourceforge.net/

Source: %name-%version.tar

BuildRequires: imake libXt-devel tk-devel xorg-cf-files

%description
tkTable - table/matrix widget extension to Tcl/Tk

%prep
%setup -q

%build
%__autoconf
%configure --exec-prefix=%buildroot --prefix=%buildroot\
  --with-blt=%_tcldatadir --with-tcl=%_libdir --with-tk=%_libdir --libdir=%_tcllibdir
%make_build

%install
DIRECTORY=%buildroot/%_tcllibdir/%teaname%major
install -d $DIRECTORY
install libTktable%major.so $DIRECTORY/
install -m 644 pkgIndex.tcl library/tkTable.tcl library/tktable.py $DIRECTORY
install -d %buildroot/%_mandir/mann
install -m 644 doc/tkTable.n %buildroot/%_mandir/mann
install -d %buildroot/%_docdir/%name
install -m 644 ChangeLog README.txt README.blt license.txt doc/tkTable.html\
               %buildroot/%_docdir/%name
cp -r demos %buildroot/%_docdir/%name

%files
%_docdir/%name/README.txt
%_docdir/%name/README.blt
%_docdir/%name/ChangeLog
%_docdir/%name/license.txt
%_docdir/%name/tkTable.html
%_docdir/%name/demos/*
%dir %_tcllibdir/%teaname%major
%_tcllibdir/%teaname%major/*
%_mandir/mann/*

%changelog
* Wed Jul 03 2019 Vladislav Zavjalov <slazav@altlinux.org> 2.10-alt1
- v.2.10

