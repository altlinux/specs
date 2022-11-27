# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: jid
Version: 0.7.6
Release: alt1
Summary: JSON incremental digger
License: MIT
Group: Development/Other
Url: https://github.com/simeji/jid/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
You can drill down JSON interactively by using filtering queries like jq.
Suggestion and Auto completion of this tool will provide you a very
comfortable JSON drill down.

%prep
%setup

%build
cd cmd/jid
go build -x -v

%install
install -Dp cmd/jid/jid %buildroot%_bindir/jid

%files
%doc LICENSE ChangeLog README.md
%_bindir/jid

%changelog
* Sun Nov 27 2022 Vitaly Chikunov <vt@altlinux.org> 0.7.6-alt1
- First import v0.7.6-7-gdabb3ff (2022-04-16).
