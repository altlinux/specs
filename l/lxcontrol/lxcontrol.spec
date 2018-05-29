Name: lxcontrol
Version: 1.3
Release: alt1
License: GPL
Group: System/Configuration/Printing
BuildArch: noarch

Url: http://www.powerup.com.au/~pbwest/lexmark/
# Source: http://www.powerup.com.au/~pbwest/lexmark/lexmark.html/lxcontrol.tar.bz2
# Source1: http://209.233.17.85/lexmark/lm1100maint.tar.bz2

Source: %name.tar
Source1: lm1100maint.tar
Source2: http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/changecartridge
Source3: README.changecartridge
Source4: README.Lexmark-Maintenance
Source5: lx.control.sh
Source6: headalign.desktop
Source7: headclean.desktop
Source8: hidecartridges.desktop
Source9: showcartridges.desktop
Patch: lxcontrol-lx.control-cups.patch
Requires: cups

Summary: Lexmark printer management commands
%description
Tools for show and hide catridges, and align and clean heads in a Lexmark
printer. Used with Lexmark 5xxx, 7xxx and 11xx, possible with others.

%prep
%setup -n %name -a1 -D
cp %SOURCE2 changecartridge
mv README.Lexmark README.Lexmark5xxx_7xxx
mv lm1100maint/README README.Lexmark1xxx
cp %SOURCE3 .
cp %SOURCE4 .
%patch0 -p1

%build
#nothing

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/lxcontrol
install -d %buildroot%_datadir/lm1100maint
install -d %buildroot%_desktopdir

# Lexmark printer maintenance
# Program and data files
install -m 755 lx.control %buildroot%_bindir/
install -m 755 %SOURCE5 %buildroot%_bindir/
install -m 755 lm1100maint/lm1100change %buildroot%_bindir/
install -m 755 lm1100maint/lm1100back %buildroot%_bindir/
install -m 755 changecartridge %buildroot%_bindir/
cp -f *.out %buildroot%_datadir/lxcontrol/
( cd %buildroot%_bindir
  ln -s lx.control headclean
  ln -s lx.control headalign
  ln -s lx.control showcartridges
  ln -s lx.control hidecartridges
  ln -s lx.control.sh headclean.sh
  ln -s lx.control.sh headalign.sh
  ln -s lx.control.sh showcartridges.sh
  ln -s lx.control.sh hidecartridges.sh
)
cp -f lm1100maint/lexmark* \
%buildroot%_datadir/lm1100maint/

# XDG menu
install -d %buildroot%_desktopdir
sed -i 's#@BINDIR@#%{_bindir}#g' %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9
cp %SOURCE6 %buildroot%_desktopdir/
cp %SOURCE7 %buildroot%_desktopdir/
cp %SOURCE8 %buildroot%_desktopdir/
cp %SOURCE9 %buildroot%_desktopdir/

%files
%_bindir/*
%_datadir/lm1100maint
%_datadir/lxcontrol
%_desktopdir/*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt1
- Initial build for ALT

