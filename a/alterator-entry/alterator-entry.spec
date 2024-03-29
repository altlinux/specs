%define _unpackaged_files_terminate_build 1

Name: alterator-entry
Version: 0.1.0
Release: alt3

Summary: Common files for [Alterator Entry] specification
License: GPLv3+
Group: Other
URL: https://gitlab.basealt.space/alt/alterator-entry

Source0: %name-%version.tar

BuildArch: noarch

Requires: libshell

%description
Common files for [Alterator Entry] specification:
- specification documents
- source shell alterator-entry-sh-functions

%prep
%setup

%install
mkdir -p %buildroot%_bindir

install -v -p -m 644 -D alterator-entry-sh-functions %buildroot%_bindir/
install -v -p -m 755 -D alterator-entry %buildroot%_bindir/
sed -i 's/@VERSION@/%version/' %buildroot%_bindir/alterator-entry

%files
%doc COPYING
%_bindir/alterator-entry
%_bindir/alterator-entry-sh-functions

%changelog
* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt3
- alterator-entry: fix version printing.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt2
- alterator-entry: fix debug source and missed help about verbose mode.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
