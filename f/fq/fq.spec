# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: fq
Version: 0.17.0
Release: alt1
Summary: A tool, language and decoders for working with binary and text formats
License: MIT
Group: Development/Other
Url: https://github.com/wader/fq

Source: %name-%version.tar
BuildRequires: golang

%description
TLDR: it aims to be jq, hexdump, dd and gdb for files combined into one.

fq is inspired by the jq tool and language and allows you to work with
binary formats in the same way. In addition to using jq expressions it
can also present decoded tree structures, transform, slice and concatenate
binary data. It also supports nested formats and features an interactive
REPL with auto-completion of functions and names.

It was originally designed to query, inspect and debug media codecs
and containers like MP4, FLAC and JPEG but has since been extended to
support a variety of formats like executables, packet captures (with
TCP reassembly) and serialization formats like JSON, YAML, XML, CBOR,
protobuf. In addition it also has functions to work with URLs, convert
to/from hex, number bases, search for patterns etc.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags "-X main.version=%version"

%install
install -Dp fq %buildroot%_bindir/fq

%check
%buildroot%_bindir/fq --version | grep -P '^\Q%version\E '
go test ./...

%files
%define _customdocdir %_docdir/%name
%doc CHANGES.md LICENSE README.md doc
%_bindir/fq

%changelog
* Mon Mar 16 2026 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to v0.17.0 (2026-03-15).

* Mon Dec 08 2025 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt1
- Update to v0.16.0 (2025-12-07).

* Sun Aug 10 2025 Vitaly Chikunov <vt@altlinux.org> 0.15.1-alt1
- First import v0.15.1 (2025-07-12).
