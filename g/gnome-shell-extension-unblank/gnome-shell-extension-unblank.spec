%global _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-unblank
Version: 20260317
Release: alt1
Summary: Unblank screen when screen saver becomes active
License: MIT
Group: Graphical desktop/GNOME
URL: https://extensions.gnome.org/extension/1414/unblank
VCS: https://github.com/sunwxg/gnome-shell-extension-unblank

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
# not needed

%install
%makeinstall_std

%files
%_datadir/gnome-shell/extensions/unblank@sun.wxg@gmail.com
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.unblank.gschema.xml

%changelog
* Wed Aug 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 20260317-alt1
- Initial build for ALT.
