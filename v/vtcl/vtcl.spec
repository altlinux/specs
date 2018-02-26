# vim: set ft=spec: -*- rpm-spec -*-

Name:      vtcl
Version:   1.6.0
Release:   alt1
Copyright: GPL
Group:     Development/Tcl
URL:       http://vtcl.sourceforge.net
Source:    http://prdownloads.sourceforge.net/vtcl/vtcl-%version.tar.gz
Requires:  tcl >= 8.3
Requires:  tk  >= 8.3
BuildArchitectures: noarch

Summary:   Visual Tcl is an integrated development environment for Tcl/Tk 8.3 and later.

%description
Visual Tcl is a freely-available, cross-platform application development environment for the Tcl/Tk language.
It generates pure Tcl/Tk code and has support for Itcl megawidgets, Tix and the BLT extension.

Visual Tcl is covered by the GNU General Public License. 
Please read the LICENSE file for more information.

%prep
%setup -q -n vtcl-%version

%install

DIRECTORY=%buildroot%{_datadir}/vtcl-%{version}

mkdir -p %buildroot%_bindir
mkdir -p $DIRECTORY
mkdir -p $DIRECTORY/images
mkdir -p $DIRECTORY/images/edit
mkdir -p $DIRECTORY/lib
mkdir -p $DIRECTORY/lib/bwidget
mkdir -p $DIRECTORY/lib/bwidget/lang
mkdir -p $DIRECTORY/lib/bwidget/images
mkdir -p $DIRECTORY/lib/Help
mkdir -p $DIRECTORY/lib/Widgets
mkdir -p $DIRECTORY/lib/Widgets/blt
mkdir -p $DIRECTORY/lib/Widgets/bwidget/
mkdir -p $DIRECTORY/lib/Widgets/core
mkdir -p $DIRECTORY/lib/Widgets/itcl
mkdir -p $DIRECTORY/lib/Widgets/table
mkdir -p $DIRECTORY/lib/Widgets/tablelist
mkdir -p $DIRECTORY/lib/Widgets/tix
mkdir -p $DIRECTORY/lib/Widgets/user
mkdir -p $DIRECTORY/lib/Widgets/vtcl
mkdir -p $DIRECTORY/lib/ttd

#install -m 755 vtcl.tcl                  $DIRECTORY
#install -m 755 vtsetup.tcl               $DIRECTORY
install -m 644 images/*.*                $DIRECTORY/images
install -m 644 images/edit/*             $DIRECTORY/images/edit
install -m 644 lib/*.*                   $DIRECTORY/lib
install -m 644 lib/Help/*                $DIRECTORY/lib/Help
install -m 644 lib/bwidget/*.tcl         $DIRECTORY/lib/bwidget
install -m 644 lib/bwidget/lang/*        $DIRECTORY/lib/bwidget/lang
install -m 644 lib/bwidget/images/*      $DIRECTORY/lib/bwidget/images
install -m 644 lib/Widgets/blt/*         $DIRECTORY/lib/Widgets/blt
install -m 644 lib/Widgets/bwidget/*     $DIRECTORY/lib/Widgets/bwidget
install -m 644 lib/Widgets/core/*        $DIRECTORY/lib/Widgets/core
install -m 644 lib/Widgets/itcl/*        $DIRECTORY/lib/Widgets/itcl
install -m 644 lib/Widgets/table/*       $DIRECTORY/lib/Widgets/table
install -m 644 lib/Widgets/tablelist/*   $DIRECTORY/lib/Widgets/tablelist
install -m 644 lib/Widgets/tix/*         $DIRECTORY/lib/Widgets/tix
install -m 644 lib/Widgets/vtcl/*        $DIRECTORY/lib/Widgets/vtcl
install -m 644 lib/ttd/*                 $DIRECTORY/lib/ttd

echo "#!/usr/bin/wish" > ./vtcl
echo "set env(PATH_TO_WISH) \"/usr/bin/wish\"" >>  ./vtcl
echo "set env(VTCL_HOME) \"/usr/share/vtcl-1.6.0\"" >>  ./vtcl

cat vtcl.tcl >> ./vtcl

install -m 755 ./vtcl %buildroot%_bindir/vtcl

%files
%doc ChangeLog LICENSE README demo doc sample
%_bindir/*
%_datadir/*


%changelog
* Mon Oct 26 2003 Pavel Mironchik <tibor@altlinux.ru> 1.6.0-alt1
- adopted for altlinux

* Tue Aug 26 2003 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- update 1.6.0

* Wed Apr 16 2003 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- update 1.6.0b2
- build on RH9

* Thu Mar 13 2003 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- update 1.6.0b1

* Sat Nov 16 2002 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- chang Group section
- rebuild on RH80

* Thu Sep 05 2002 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- update 1.6.0a3

* Mon Mar 11 2002 Fuhito Suguri <bitwalk@jcom.home.ne.jp>
- update 1.6.0a2

* Sat Jan 05 2002 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- apply patch to cheange width of toolbar.

* Fri Dec 28 2001 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- update 1.6.0a1

* Wed Nov 15 2001 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- rebuild on RH 7.2 and rewrite spec

* Wed Oct 31 2001 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- update 1.5.2

* Mon Apr 02 2001 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- applied 1.5.1b4

* Sat Mar 25 2001 Fuhito Suguri <bitwalk@nyc.odn.ne.jp>
- build new spec file for 1.5.1b3. Add patch to enable XIM.

