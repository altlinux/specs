%define libname spawn
Name: ocaml-%libname
Version: 0.15.1
Release: alt1
Summary: OCAML SPAWN - spawning system process
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/spawn
VCS: https://github.com/janestreet/spawn
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-odoc-devel


%description
Spawn is a small library exposing only one functionality: spawning sub-process.
It has three main goals:
    1. provide missing features of Unix.create_process such as
       providing a working directory

    2. provide better errors when a system call fails in the sub-process.
       For instance if a command is not found, you get
       a proper [Unix.Unix_error] exception

    3. improve performance by using vfork when available. It is often
    claimed that nowadays fork is as fast as vfork, however in practice fork
    takes time proportional to the process memory while vfork is constant time.
    In application using a lot of memory, vfork can be thousands of times
    faster than fork.


%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install -p %libname

%check
%dune_check -p %libname

%files -f ocaml-files.runtime
%doc LICENSE.md


%files devel -f ocaml-files.devel

%changelog
* Fri Sep 13 2024 Anton Farygin <rider@altlinux.ru> 0.15.1-alt1
- first build for ALT Linux
