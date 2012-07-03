%define base gtk2-themes
%define _name gtk2step
%define _bname GTK2-Step

Name: %base-%_name
Version: 1.2
Release: alt1

Summary: The NeXT look of GTK2
License: GPL
Group: Graphical desktop/GNOME

BuildArch: noarch
Requires: gtk-engines-pixmap

Source: %_bname-%version.tar.gz

%description
%_bname theme - the NeXT look of GTK2

%prep
%setup -n %_bname
%__chmod -R a-rwx,u+rwX,a+rX *
find . -name '*~' -delete

%install
%__mkdir_p %buildroot%_datadir/themes/%_bname
%__cp -r gtk-2* %buildroot%_datadir/themes/%_bname

%files
%dir %_datadir/themes/%_bname
%_datadir/themes/%_bname/gtk-2*

%changelog
* Fri Apr 09 2004 Sir Raorn <raorn@altlinux.ru> 1.2-alt1
- [1.2]

* Thu Mar 25 2004 Sir Raorn <raorn@altlinux.ru> 1.1-alt1
- Built for Sisyphus


