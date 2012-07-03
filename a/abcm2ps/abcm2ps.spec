Name: abcm2ps
Version: 5.9.3
Release: alt1
Summary: a program to typeset abc tunes into Postscript
License: GPL
Url: http://moinejf.free.fr
Group: File tools

Packager: Yuri Fil <yurifil at altlinux.org>

Source: http://moinejf.free.fr/%{name}-%{version}.tar.gz

%description
abcm2ps is a package which converts music tunes from ABC format to
PostScript. Based on abc2ps version 1.2.5, it was developped mainly to print
barock organ scores which have independant voices played on one or many
keyboards and a pedal-board. abcm2ps introduces many extensions to the ABC
language that make it suitable for classical music.

%prep
%setup -q

%build
%configure --enable-a4
%make_build

%install
%makeinstall docdir=%buildroot%_docdir
rm -rf %buildroot%_docdir/%name/

%files
%doc Changes INSTALL License README *.abc *.txt sample3.eps
%_bindir/abcm2ps
%_datadir/abcm2ps/


%changelog
* Fri Jan 09 2009 Yuri Fil <yurifil@altlinux.org> 5.9.3-alt1
- new version of abcm2ps

