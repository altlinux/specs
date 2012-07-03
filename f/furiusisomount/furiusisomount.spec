Name: furiusisomount
Version: 0.9.0.0
Release: alt4

Summary: Gtk+ Interface to Mount ISO, IMG, BIN, MDF and NRG Image files
Group: File tools
License: GPL
URL: https://launchpad.net/furiusisomount/

Source0: %name-%version.tar.gz

Patch0: furiusisomount-0.9.0.0-alt-fix-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: fuseiso

BuildPreReq: /proc

# Automatically added by buildreq on Wed Mar 25 2009
BuildRequires: libgtk-sharp2 mono-devel mono-mcs

%description
Simple Gtk+ Interface to Mount ISO, IMG, BIN, MDF and NRG Image
files without burning to disk.

An ISO, IMG, BIN, MDF and NRG Image management utility.

* Automatically Mounts ISO, IMG, BIN, MDF and NRG Image Files.
* Automatically creates a mount point in your home directory.
* Automatically Unmounts the Image files.
* Automatically removes the mount directory to return your home
  directory to its previous state.
* Automatically saves the history of the last 10 images mounted.
* Mounts multiple images.
* Burn ISO and IMG Files to optical disk.
* Generate Md5 and SHA1 checksums.
* Automatically retrieves any previously unmounted images.
* Automatically generates a log file of all commands needed to mount
  and unmount images manually.
* Localizable

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%dir %_libdir/furiusisomount
%_libdir/furiusisomount/
%_datadir/applications/furiusisomount.desktop

%changelog
* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.9.0.0-alt4
- fix build

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 0.9.0.0-alt3
- apply patch from repocop
- buildreq

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 0.9.0.0-alt2
- remove deprecated Encoding field from desktop file
  (thanks to repocop)

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.0.0-alt1
- 0.8.4.0 -> 0.9.0.0

* Sun Jun 29 2008 Igor Zubkov <icesik@altlinux.org> 0.8.4.0-alt1
- build for Sisyphus

