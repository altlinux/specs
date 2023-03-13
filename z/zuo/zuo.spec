%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: zuo
Version: 1.0.racket8.8
Release: alt1

Summary: A tiny Racket for scripting
License: Apache-2.0 MIT
Group: Development/Other
Url: https://racket-lang.org/
Vcs: https://github.com/racket/zuo

Source: %name-%version.tar

BuildRequires: /proc

%description
Zuo: A Tiny Racket for Scripting

You should use Racket to write scripts. But what if you need something
much smaller than Racket for some reason - or what if you're trying to
script a build of Racket itself? Zuo is a tiny Racket with primitives
for dealing with files and running processes, and it comes with a
make-like embedded DSL.

Zuo is a Racket variant in the sense that program files start with
\#lang, and the module path after #lang determines the parsing and
expansion of the file content. That's how the make-like DSL is defined,
and even the base Zuo language is defined by layers of #langs. One of
the early layers implements macros.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%buildroot%_bindir/%name -X %buildroot%_datadir/%name . check

%files
%doc LICENSE.txt
%_datadir/%name
%_bindir/%name

%changelog
* Sun Mar 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.racket8.8-alt1
- Updated to Racket v8.8.

* Fri Oct 07 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0-alt3.gitd12bbec6
- enable check

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0-alt2.gitd12bbec6
- add %%autoreconf

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0-alt1.gitd12bbec6
- initial build for Sisyphus

