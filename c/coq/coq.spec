Name: coq
Version: 8.20.1
Release: alt1

Summary: Proof management system

# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %ocaml_native_arch

# The project as a whole is LGPL-2.1-only.  Exceptions:
# - clib/diff2.ml is MIT
# - gramlib is BSD-3-Clause
License: LGPL-2.1-only AND MIT AND BSD-3-Clause
Group: Development/Other
Url: https://coq.inria.fr/
VCS: https://github.com/coq/coq

Source0: %name-%version.tar
Source1: fr.inria.coqide.desktop
Source2: coq.xml
Source3: fr.inria.coqide.metainfo.xml

BuildRequires: ocaml
BuildRequires: ocaml-cairo2-devel
BuildRequires: ocaml-dune
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-lablgtk3-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-zarith-devel

BuildRequires(pre): rpm-build-ocaml
BuildRequires: rpm-build-python
BuildRequires: rpm-build-xdg
BuildRequires: adwaita-icon-theme
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: findutils
BuildRequires: git-core
BuildRequires: java
BuildRequires: libicns-utils
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: libgtksourceview3-devel

# Already inside coq-core/tools subdir
%add_python3_req_skip TimeFileMaker

%description
Coq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems
together with an environment for semi-interactive development of
machine-checked proofs.

Typical applications include the certification of properties of
programming languages (e.g. the CompCert compiler certification project,
or the Bedrock verified low-level programming library), the formalization
of mathematics (e.g. the full formalization of the Feit-Thompson theorem
or homotopy type theory) and teaching.

%package core
Summary: Core components of the coq proof management system
Group: Development/Other
Requires: %name = %EVR

%description core
This package includes the Coq core binaries, plugins, and tools, but not
the vernacular standard library.

%package coqide-server
Summary: The coqidetop language server
Group: Development/Other
Requires: %name-core = %EVR

%description coqide-server
This package provides the coqidetop language server, an implementation of
Coq's XML protocol which allows clients, such as CoqIDE, to interact with
Coq in a structured way.

%package coqide
Summary: Coqide IDE for Coq proof management system
Group: Development/Other
Requires: %name-coqide-server = %EVR
Requires: adwaita-icon-theme
Requires: hicolor-icon-theme
Requires: xdg-utils

%description coqide
This package provides CoqIDE, a graphical user interface for the
development of interactive proofs.

%prep
%setup

sed -i "s|python2|python3|g" doc/tools/coqrst/notations/fontsupport.py

%build
./configure -prefix %prefix \
            -libdir %_ocamldir/coq \
            -configdir %_sysconfdir/xdg/%name \
            -mandir %_mandir \
            -docdir %_docdir

make dunestrap VERBOSE=1 DUNEOPT="--verbose --profile=release"
%dune_build -p coq-core,coq-stdlib,coq,coqide-server,coqide

%install
%dune_install -p coq-core,coq-stdlib,coq,coqide-server,coqide

mkdir -p %buildroot%_xdgconfigdir/coq/

# Install desktop and file type icons
pushd ide/coqide/MacOS
icns2png -x coqide.icns
for sz in 16 32 256 512; do
  mkdir -p %buildroot%_iconsdir/hicolor/${sz}x${sz}/apps
  mv coqide_${sz}x${sz}x32.png \
    %buildroot%_iconsdir/hicolor/${sz}x${sz}/apps/coq.png
done
icns2png -x coqfile.icns
for sz in 16 32 128 256 512; do
  mkdir -p %buildroot%_iconsdir/hicolor/${sz}x${sz}/mimetypes
  mv coqfile_${sz}x${sz}x32.png \
    %buildroot%_iconsdir/hicolor/${sz}x${sz}/mimetypes/coqfile.png
done
popd

# Make a MIME type for .v files
mkdir -p %buildroot%_xdgmimedir/packages
cp -p %SOURCE2 %buildroot%_xdgmimedir/packages

# Install desktop file
desktop-file-install --dir=%buildroot%_desktopdir %SOURCE1

# Install AppData file
mkdir -p %buildroot%_datadir/metainfo
install -pm 644 %SOURCE3 %buildroot%_datadir/metainfo
appstream-util validate-relax --nonet \
  %buildroot%_datadir/metainfo/fr.inria.coqide.metainfo.xml

# Install the language bindings
mkdir -p %buildroot%_datadir/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %buildroot%_datadir/gtksourceview-3.0/language-specs
done

# Install the style file
mkdir -p %buildroot%_datadir/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %buildroot%_datadir/gtksourceview-3.0/styles

%files
%_ocamldir/coq/
%_ocamldir/coq-stdlib/
%_docdir/coq
%_docdir/coq-stdlib/

%files core
%doc README.md LICENSE
%_ocamldir/coq-core/
%_ocamldir/stublibs/dllcoqperf_stubs.so
%_ocamldir/stublibs/dllcoqrun_stubs.so
%_bindir/coqc*
%_bindir/coqdep
%_bindir/coqdoc
%_bindir/coq_makefile
%_bindir/coqnative
%_bindir/coqpp
%_bindir/coq-tex
%_bindir/coqtimelog2html
%_bindir/coqtop*
%_bindir/coqwc
%_bindir/coqworker*
%_bindir/coqworkmgr
%_bindir/csdpcert
%_bindir/ocamllibdep
%_bindir/votour
%_mandir/man1/coqc.1*
%_mandir/man1/coqchk.1*
%_mandir/man1/coqdep.1*
%_mandir/man1/coqdoc.1*
%_mandir/man1/coq_makefile.1*
%_mandir/man1/coqnative.1*
%_mandir/man1/coq-tex.1*
%_mandir/man1/coqtop.1*
%_mandir/man1/coqtop.byte.1*
%_mandir/man1/coqwc.1*
%_datadir/texmf/tex/latex/misc/*
%_docdir/coq-core/

%files coqide-server
%_bindir/coqidetop*
%_ocamldir/coqide-server/
%_docdir/coqide-server/

%files coqide
%doc ide/coqide/FAQ
%_bindir/coqide
%_datadir/%name/
%_datadir/icons/hicolor/16x16/apps/coq.png
%_datadir/icons/hicolor/16x16/mimetypes/coqfile.png
%_datadir/icons/hicolor/32x32/apps/coq.png
%_datadir/icons/hicolor/32x32/mimetypes/coqfile.png
%_datadir/icons/hicolor/128x128/mimetypes/coqfile.png
%_datadir/icons/hicolor/256x256/apps/coq.png
%_datadir/icons/hicolor/256x256/mimetypes/coqfile.png
%_datadir/icons/hicolor/512x512/apps/coq.png
%_datadir/icons/hicolor/512x512/mimetypes/coqfile.png
%_docdir/coqide/
%_mandir/man1/coqide.1*
%_ocamldir/coqide/
%_datadir/gtksourceview-3.0/language-specs/coq*.lang
%_datadir/gtksourceview-3.0/styles/coq_style.xml
%_datadir/mime/packages/coq.xml
%_sysconfdir/xdg/coq/
%_datadir/metainfo/fr.inria.coqide.metainfo.xml
%_desktopdir/fr.inria.coqide.desktop

%changelog
* Tue Feb 18 2025 Leonid Znamenok <respublica@altlinux.org> 8.20.1-alt1
- New version 8.20.1.

* Sat Jan 25 2025 Leonid Znamenok <respublica@altlinux.org> 8.20.0-alt1
- Initial build for Sisyphus (Thanks to Fedora).
