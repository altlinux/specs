%define _unpackaged_files_terminate_build 1

Name: alterator-entry
Version: 0.1.1
Release: alt1

Summary: Common files for [Alterator Entry] specification
License: GPLv3+
Group: Other
URL: https://gitlab.basealt.space/alt/alterator-entry

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
Requires: libshell

%ifarch x86_64
BuildRequires: taplo
Requires: taplo
%endif

%description
Common files for Alterator Entry specification:
- specification documents
- source shell alterator-entry-sh-functions

%prep
%setup

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_alterator_datadir/schemas

find ./schemas/ -type f -exec install -v -p -m 644 -D  {} %buildroot%_alterator_datadir/schemas/ \;
install -v -p -m 644 -D alterator-entry-sh-functions %buildroot%_bindir/
install -v -p -m 755 -D alterator-entry %buildroot%_bindir/
sed -i 's/@VERSION@/%version/' %buildroot%_bindir/alterator-entry

%ifarch x86_64
%check
export ALTERATOR_SCHEMAS_DIR=%buildroot%_alterator_datadir/schemas
PATH="$PATH:." find ./examples -type f -exec alterator-entry {} \+
%endif

%files
%doc COPYING
%_bindir/alterator-entry
%_bindir/alterator-entry-sh-functions
%dir %_alterator_datadir/schemas
%_alterator_datadir/schemas/*

%changelog
* Tue Dec 03 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Switch to using toml instead of ini files for Alterator Entry.
- Add json schemas to validate Alterator Entry files.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt3
- alterator-entry: fix version printing.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt2
- alterator-entry: fix debug source and missed help about verbose mode.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
