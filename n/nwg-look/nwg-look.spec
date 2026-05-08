%define _unpackaged_files_terminate_build 1
%def_with check

Name: nwg-look
Version: 1.1.1
Release: alt1

Summary: GTK3 settings editor adapted to work in the wlroots environment
License: MIT
Group: Graphical desktop/Other
VCS: https://github.com/nwg-piotr/nwg-look
Url: https://github.com/nwg-piotr/nwg-look

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: libgtk+3-devel

%description
Nwg-look  is a  GTK  settings  editor, designed  to  work properly  in
wlroots-based  Wayland  environment. The  look  and  feel is  strongly
influenced by LXAppearance, but nwg-look  is intended to free the user
from a few inconveniences:

- It  works natively  on Wayland.  You  no longer  need Xwayland,  nor
  strange env variables for it to run.

- It applies gsettings directly, with  no need to use workarounds. You
  don't need to set gsettings in  the sway config file. You don't need
  the import-gsettings script.

%prep
%setup -a1

%build
%gobuild
mkdir bin
mv nwg-look bin

%install
%makeinstall_std

# Package using %%doc macro
rm %buildroot%_datadir/doc/nwg-look/README.md
rm %buildroot%_datadir/licenses/nwg-look/LICENSE

%files
%doc README.md LICENSE
%_bindir/nwg-look
%_datadir/nwg-look
%_desktopdir/nwg-look.desktop
%_pixmapsdir/nwg-look.svg

%changelog
* Fri May 08 2026 Egor Ignatov <egori@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Wed Jun 25 2025 Egor Ignatov <egori@altlinux.org> 1.0.6-alt1
- New version 1.0.6.

* Thu May 15 2025 Egor Ignatov <egori@altlinux.org> 1.0.5-alt1
- New version 1.0.5.

* Mon May 05 2025 Egor Ignatov <egori@altlinux.org> 1.0.4-alt1
- First build for ALT.
