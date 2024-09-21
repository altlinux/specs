%ifarch %ocaml_native_arch
%global unison_native NATIVE=true
%else
%global unison_native NATIVE=false
%endif

Name: unison
Version: 2.53.5
Release: alt1

Summary: File-synchronization tool

Group: Networking/File transfer
License: GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later
Url: https://github.com/bcpierce00/unison
VCS: https://github.com/bcpierce00/unison
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ocaml >= 1.6.1
BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-lablgtk3-devel
BuildRequires: ocaml-cairo2-devel
BuildRequires: texlive-collection-latexrecommended texlive-collection-basic ghostscript-utils

%description
Unison is a file-synchronization tool. It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

%package gui
Summary: GTK+ version of unison file-synchronization tool
Group: Networking/File transfer

%description gui
Unison is a file-synchronization tool. It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

%prep
%setup
%patch0 -p1

%build
%make_build tui fsmonitor manpage gui docs %unison_native

%install
%makeinstall PREFIX=%_prefix %unison_native

install -Dpm0644 icons/U.svg %buildroot%_iconsdir/hicolor/scalable/apps/unison.svg

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Unison
GenericName=File Synchronizer
Comment=File-synchronization tool
Exec=%{name}-gui
Icon=%name
Terminal=false
Type=Application
Categories=Utility;System;
EOF

%check
make test %unison_native


%files
%doc LICENSE NEWS.md README.md
%_bindir/unison
%_bindir/unison-fsmonitor
%_man1dir/unison.*

%files gui
%doc LICENSE
%_bindir/unison-gui
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/scalable/apps/unison.svg

%changelog
* Sat Sep 21 2024 Anton Farygin <rider@altlinux.ru> 2.53.5-alt1
- 2.53.5

* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 2.51.4-alt1.1
- NMU: support building on architectures that don't have ocamlopt

* Thu Jul 29 2021 Anton Farygin <rider@altlinux.ru> 2.51.4-alt1
- 2.51.4

* Mon Apr 12 2021 Anton Farygin <rider@altlinux.org> 2.51.3-alt2
- fixed build with ocaml 4.12

* Sat Oct 24 2020 Anton Farygin <rider@altlinux.ru> 2.51.3-alt1
- 2.51.3

* Sat Aug 29 2020 Anton Farygin <rider@altlinux.ru> 2.51.2-alt5
- add patches from upstream git

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 2.51.2-alt4
- build 2.51.3

* Thu Aug 08 2019 Anton Farygin <rider@altlinux.ru> 2.51.2-alt3
- rebuild with ocaml-4.08

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 2.51.2-alt2
- added unison-gui package with GTK2 UI (closes: #18455)

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 2.51.2-alt1
- 2.51.2

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.48.4-alt2
- NMU: rebuild with TeXLive instead of TeTeX

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 2.48.4-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 2.45.28-alt1
- new version

* Thu Jul 12 2012 Anton Farygin <rider@altlinux.ru> 2.45.4-alt1
- first build for Sisyphus

