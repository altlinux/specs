Name: rocq
Version: 9.2.0
Release: alt3

Summary: Proof management system

# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %ocaml_native_arch

# The project as a whole is LGPL-2.1-only.  Exceptions:
# - clib/diff2.ml is MIT
# - gramlib is BSD-3-Clause
License: LGPL-2.1-only AND MIT AND BSD-3-Clause
Group: Development/Other
Url: https://rocq-prover.org/
VCS: https://github.com/rocq-prover/rocq

Source0: %name-%version.tar
Source1: org.rocq-prover.rocqide.desktop
Source2: rocq.xml
Source3: org.rocq-prover.rocqide.metainfo.xml

Patch1: rocq-ALT-58676.patch
Patch2: rocq-backport-switch-to-rocq.theory-for-dune.patch

BuildRequires: ocaml
BuildRequires: ocaml-cairo2-devel
BuildRequires: ocaml-dune
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-lablgtk3-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-zarith-devel

BuildRequires(pre): rpm-build-ocaml
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

Provides:  coq = %{version}-%{release}
Obsoletes: coq < 9.0.0

# Already inside coq-core/tools subdir
%add_python3_req_skip TimeFileMaker

%description
rocq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems
together with an environment for semi-interactive development of
machine-checked proofs.

Typical applications include the certification of properties of
programming languages (e.g. the CompCert compiler certification project,
or the Bedrock verified low-level programming library), the formalization
of mathematics (e.g. the full formalization of the Feit-Thompson theorem
or homotopy type theory) and teaching.

%package core
Summary: Core components of the rocq proof management system
Group: Development/Other
Requires: %name = %EVR

Provides:  coq-core = %EVR
Obsoletes: coq-core < 9.0.0

AutoReqProv: nopython

%description core
This package includes the rocq core binaries, plugins, and tools, but not
the vernacular standard library.

%package -n coq-core-compat
Group: Development/Other

Summary:  Compatibility binaries for Coq after the Rocq renaming
Requires: %name-core = %EVR

Provides:  coq-core = %EVR
Obsoletes: coq-core < 9.0.0

%description -n coq-core-compat
This package includes compatibility binaries to call Rocq
through previous Coq commands like coqc coqtop, ...

%package coqide-server
Summary: The coqidetop language server
Group: Development/Other
Requires: %name-core = %EVR

Provides:  coq-coqide-server = %{version}-%{release}
Obsoletes: coq-coqide-server < 9.0.0

%description coqide-server
This package provides the coqidetop language server, an implementation of
Rocq's XML protocol which allows clients, such as RocqIDE, to interact with
Rocq in a structured way.

%package rocqide
Summary: Rocqide IDE for Rocq proof management system
Group: Development/Other
Requires: %name-coqide-server = %EVR
Requires: adwaita-icon-theme
Requires: hicolor-icon-theme
Requires: xdg-utils

Provides:  coq-coqide = %{version}-%{release}
Obsoletes: coq-coqide < 9.0.0

%description rocqide
This package provides RocqIDE, a graphical user interface for the
development of interactive proofs.

%prep
%setup

%patch1 -p1
%patch2 -p1

sed -i "s|python2|python3|g" doc/tools/rocqrst/notations/fontsupport.py

%build
%global rocq_packages rocq-runtime,rocq-core,coq-core,coqide-server,rocqide

./configure -prefix %prefix \
            -libdir %_ocamldir/coq \
            -configdir %_sysconfdir/xdg/%name \
            -docdir %_docdir \
            -browser "xdg-open %%s" \


make dunestrap VERBOSE=1 DUNEOPT="--verbose --profile=release"
%dune_build -p %rocq_packages

%install
%dune_install -p %rocq_packages

mkdir -p %buildroot%_xdgconfigdir/coq/

# Install desktop and file type icons
pushd ide/rocqide/MacOS
icns2png -x coqide.icns
for sz in 256; do
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
  %buildroot%_datadir/metainfo/org.rocq-prover.rocqide.metainfo.xml

# Install the language bindings
mkdir -p %buildroot%_datadir/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %buildroot%_datadir/gtksourceview-3.0/language-specs
done

# Install the style file
mkdir -p %buildroot%_datadir/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %buildroot%_datadir/gtksourceview-3.0/styles

%files
%_ocamldir/coq

%files core
%doc README.md LICENSE
%_ocamldir/rocq-runtime/
%_ocamldir/rocq-core/
%_ocamldir/stublibs/dllcoqperf_stubs.so
%_ocamldir/stublibs/dllcoqrun_stubs.so
%_bindir/rocq
%_bindir/rocq.byte
%_bindir/rocqchk
%_bindir/csdpcert
%_bindir/ocamllibdep
%_bindir/votour
%_mandir/man1/rocq.1*
%_mandir/man1/rocqchk.1*
%_datadir/texmf/tex/latex/misc/*
%_docdir/rocq-runtime/
%_docdir/rocq-core/

%files coqide-server
%_bindir/coqidetop*
%_ocamldir/coqide-server/
%_docdir/coqide-server/

%files rocqide
%doc ide/rocqide/FAQ
%_bindir/rocqide
%_datadir/coq
%_datadir/icons/hicolor/16x16/mimetypes/coqfile.png
%_datadir/icons/hicolor/32x32/mimetypes/coqfile.png
%_datadir/icons/hicolor/128x128/mimetypes/coqfile.png
%_datadir/icons/hicolor/256x256/apps/coq.png
%_datadir/icons/hicolor/256x256/mimetypes/coqfile.png
%_datadir/icons/hicolor/512x512/mimetypes/coqfile.png
%_docdir/rocqide/
%_mandir/man1/rocqide.1*
%_ocamldir/rocqide/
%_datadir/gtksourceview-3.0/language-specs/coq*.lang
%_datadir/gtksourceview-3.0/styles/coq_style.xml
%_datadir/mime/packages/rocq.xml
%_sysconfdir/xdg/coq/
%_datadir/metainfo/org.rocq-prover.rocqide.metainfo.xml
%_desktopdir/org.rocq-prover.rocqide.desktop

%files -n coq-core-compat
%_bindir/coq-tex
%_bindir/coq_makefile
%_bindir/coqc
%_bindir/coqchk
%_bindir/coqdep
%_bindir/coqdoc
%_bindir/coqnative
%_bindir/coqpp
%_bindir/coqtop
%_bindir/coqtop.byte
%_bindir/coqwc
%_bindir/coqworkmgr
%_ocamldir/coq-core
%_docdir/coq-core
%_mandir/man1/coq*

%changelog
* Wed Jul 01 2026 Leonid Znamenok <respublica@altlinux.org> 9.2.0-alt3
- Fixed FTBFS with dune 3.21.

* Mon May 11 2026 Leonid Znamenok <respublica@altlinux.org> 9.2.0-alt2
- Dropped dependency on python2-base (Closes: 59080).

* Fri Apr 10 2026 Leonid Znamenok <respublica@altlinux.org> 9.2.0-alt1
- New Version 9.2.0.
- Renamed coq -> rocq.
- (Closes: 58676, 58680).

* Tue Feb 18 2025 Leonid Znamenok <respublica@altlinux.org> 8.20.1-alt1
- New version 8.20.1.

* Sat Jan 25 2025 Leonid Znamenok <respublica@altlinux.org> 8.20.0-alt1
- Initial build for Sisyphus (Thanks to Fedora).
