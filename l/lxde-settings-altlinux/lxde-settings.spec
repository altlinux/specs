%define _unpackaged_files_terminate_build 1

%define theme_name altlinux
%define theme_fullname lxde-settings-%theme_name

Name: %theme_fullname
Version: 0.4
Release: alt1

BuildArch: noarch

Summary: Provides default configuration for LXDE in ALT Linux
Provides: lxde-settings
Group: Graphical desktop/Other
License: %gpl2plus

BuildPreReq: rpm-build-licenses

## components used in this theme
Requires: fonts-ttf-liberation
Requires: tango-icon-theme tango-icon-theme-extras
Requires: gtk2-theme-Human-lite
Requires: x-cursor-theme-jimmac

Source: lxde.tar.bz2

%description
Default graphics theme for LXDE in ALT Linux

%install
mkdir -p %buildroot/%_datadir
tar xvf %SOURCE0 -C %buildroot/%_datadir
mv %buildroot/%_datadir/lxde %buildroot/%_datadir/%theme_fullname

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme_fullname << __EOF__
%_datadir/lxde %_datadir/%theme_fullname 10
__EOF__

%files 
%config /etc/alternatives/packages.d/%theme_fullname
%_datadir/%theme_fullname

%changelog
* Mon May 30 2011 Mykola Grechukh <gns@altlinux.org> 0.4-alt1
- start filemanager with argument.
- ALT+F6 also do toggleMaximized.
- font updated for desktop.

* Thu Feb 03 2011 Mykola Grechukh <gns@altlinux.ru> 0.3-alt1
- new keybindings:
    - for window controls: MS-like (W-Arrows)
    - start lxrandr on XF86Display
    - lxtask on XF86Launch1
    - logout screen instead of lxtask on C-a-d

* Tue Dec 07 2010 Mykola Grechukh <gns@altlinux.ru> 0.2-alt3
- removed noisy battery alarm

* Thu Nov 18 2010 Mykola Grechukh <gns@altlinux.ru> 0.2-alt2
- deps updated. Hinting fixed (closes: #24582)

* Wed May 19 2010 Mykola Grechukh <gns@altlinux.ru> 0.2-alt1
- updated

* Wed May 05 2010 Mykola Grechukh <gns@altlinux.ru> 0.1-alt2
- spec cleanup

* Wed May 05 2010 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1
- first build
