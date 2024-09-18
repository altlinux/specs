%ifnarch %ix86
%def_with check
%else
%def_without check
%endif
%define ocamlmod tiny_httpd
Name: ocaml-%ocamlmod
Version: 0.17.0
Release: alt1
Summary: Minimal HTTP server using threads
Group: Development/ML
License: MIT
Url: https://github.com/c-cube/tiny_httpd/
VCS: https://github.com/c-cube/tiny_httpd/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml >= 5.2.0
BuildRequires: dune
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-iostream-devel
BuildRequires: ocaml-hmap-devel
BuildRequires: ocaml-odoc-devel
%if_with check
BuildRequires: ocaml-logs-devel
BuildRequires: ocaml-ptime-devel
BuildRequires: ocaml-qcheck-devel
BuildRequires: curl
%endif

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
Minimal HTTP server using good old threads, with stream abstractions, simple
routing, URL encoding/decoding, static asset serving, and optional compression
with camlzip. It also supports server-sent events (w3c).

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %ocamlmod

%install
%dune_install %ocamlmod

%check
%dune_check -p %ocamlmod

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md
%_bindir/http_of_dir
%_bindir/tiny-httpd-vfs-pack

%changelog
* Wed Sep 18 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT
