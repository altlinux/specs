Name:      vtcl
Version:   1.6.1a1
Release:   alt1

Summary:   Visual Tcl is an integrated development environment for Tcl/Tk 8.3 and later.

License:   GPLv2
Group:     Development/Tcl
URL:       http://vtcl.sourceforge.net

Source:    http://prdownloads.sourceforge.net/vtcl/vtcl-%version.tar.gz
Patch0:    vtcl-tkversion.patch
Patch1:    vtcl-browser.patch

Requires:  tcl tk tcl-tix
BuildArch: noarch

%description
Visual Tcl is a freely-available, cross-platform application development environment for the Tcl/Tk language.
It generates pure Tcl/Tk code and has support for Itcl megawidgets, Tix and the BLT extension.

Visual Tcl is covered by the GNU General Public License. 
Please read the LICENSE file for more information.

%prep
%setup
%patch0
%patch1

%install

mkdir -p %buildroot%_bindir %buildroot%_datadir/%name
cp -a *.tcl images lib %buildroot%_datadir/%name

echo "#!/usr/bin/wish" > ./vtcl
echo "set env(PATH_TO_WISH) \"/usr/bin/wish\"" >>  ./vtcl
echo "set env(VTCL_HOME) \"/usr/share/vtcl\"" >>  ./vtcl

cat vtcl.tcl >> ./vtcl

install -m 755 ./vtcl %buildroot%_bindir/vtcl

%files
%doc ChangeLog LICENSE README demo doc sample
%_bindir/*
%_datadir/*

%changelog
* Mon Oct 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.6.1a1-alt1
- Build new version.
- Add patch for tk version (Closes: #20571).
- Add patch for browser.
- Change license and cleanup spec.

* Mon Oct 26 2003 Pavel Mironchik <tibor@altlinux.ru> 1.6.0-alt1
- adopted for altlinux
- update 1.6.0
