Name: simple-ccsm
Version: 0.8.4
Release: alt4
Epoch: 1
Summary: Simple CompizConfig Settings Manager
License: GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: compiz >= %version compiz-fusion-plugins-main >= %version compiz-fusion-plugins-extra >= %version
%py_requires libglade

BuildArch: noarch
BuildRequires: intltool python-devel

%description
Configure Compiz with CompizConfig

%prep
%setup -q
%patch -p1

%build
%make PREFIX=%_prefix

%install
%make PREFIX=%_prefix DESTDIR=%buildroot install
subst "s|%buildroot||" %buildroot%_bindir/%name
mkdir -p %buildroot%_prefix/libexec
mv %buildroot%_bindir/%name %buildroot%_prefix/libexec/%name

mkdir -p %buildroot%_altdir
cat <<__EOF__ > %buildroot%_altdir/%name
%_bindir/%name	%_prefix/libexec/%name	20
__EOF__

# ccsm and simple-ccsm are alternatives
# and ccsm uses name `simple-ccsm` in it's desktop file
# how should that work?
rm -f %buildroot%_desktopdir/simple-ccsm.desktop

rm %buildroot%python_sitelibdir_noarch/simple_ccsm-*.egg-info
%find_lang %name

%files -f %name.lang
%_altdir/%name
%_prefix/libexec/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.8.4-alt4
- restore compiz in Sisyphus

* Tue Jun 14 2011 Mikhail Efremov <sem@altlinux.org> 1:0.8.4-alt3.M60P.1
- Added support for Shift-Alt-Tab to reverse through windows
    (from upstream git).
- Rollback to 0.8.4.

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Fri Feb 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- requires python-module-pygtk-libglade (closes: #23034)

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- fixed conflict with ccsm

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- initial release

