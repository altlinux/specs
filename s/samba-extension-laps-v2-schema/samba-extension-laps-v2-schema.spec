%define _unpackaged_files_terminate_build 1

%define _laps_schema_dir %_datadir/native-laps-schema

Name: samba-extension-laps-v2-schema
Version: 0.1.0
Release: alt1

Summary: LAPSv2 schema installer for samba DC.
License: GPLv3+
Group: Other
Url: https://github.com/august-alt/samba-extension-laps-v2-schema

BuildArch: noarch

BuildRequires: rpm-build-python3
Requires: ldb-tools

Source0: %name-%version.tar

%description
Installs native LAPS schema extension to samba DC.

%prep
%setup -q

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_laps_schema_dir

install -D install-laps-v2-schema.py %buildroot/%_bindir/install-laps-v2-schema.py

install -D computer.ldif %buildroot/%_laps_schema_dir/computer.ldif
install -D extended-rights.ldif %buildroot/%_laps_schema_dir/extended-rights.ldif
install -D laps-v2-schema-extension.ldif %buildroot/%_laps_schema_dir/laps-v2-schema-extension.ldif

%files
%doc README.md
%doc LICENSE
%_bindir/install-laps-v2-schema.py
%_laps_schema_dir/computer.ldif
%_laps_schema_dir/extended-rights.ldif
%_laps_schema_dir/laps-v2-schema-extension.ldif

%changelog
* Sun Mar 30 2025 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build