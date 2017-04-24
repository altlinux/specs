Name: google-drive-ocamlfuse
Version: 0.6.16
Release: alt1%ubt
License: BSD-2-Clause
Summary: FUSE filesystem for Google Drive
Url: http://gdfuse.forge.ocamlcore.org
Group: Networking/Remote access
Source: %name-%version.tar
BuildRequires: ocaml ocaml-ocamlbuild
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-fuse-devel
BuildRequires: ocaml-gapi-devel
BuildRequires: ocaml-sqlite3 
BuildRequires: ocaml-cryptokit-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-camlidl-devel
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-curl-devel
BuildRequires: ocaml-ocamlnet-devel
BuildRequires: libsqlite3-devel
BuildRequires: libcurl-devel
BuildRequires: zlib-devel
BuildRequires: libfuse-devel
BuildRequires(pre): rpm-build-ubt

%description
google-drive-ocamlfuse is a FUSE-based file system backed by Google Drive,
written in OCaml. It lets you mount your Google Drive on Linux.

On the first time, just run google-drive-ocamlfuse, which will open a
browser for authentication. If that process succeeds, it will print
"Access token retrieved correctly.". Now run google-drive-ocamlfuse
with an empty directory supplied, which is the mount point for your Google
Drive. You can optionally unmount with fusermount -u mount-point.

Further documentation is available here:

  https://github.com/astrada/google-drive-ocamlfuse/wiki

%prep
%setup

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %buildroot%_bindir
cp gdfuse.native %buildroot%_bindir/%name

%files
%doc README.md doc/ LICENSE
%_bindir/%name

%changelog
* Mon Apr 24 2017 Anton Farygin <rider@altlinux.ru> 0.6.16-alt1%ubt
- first build for ALT
