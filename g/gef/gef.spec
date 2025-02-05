Name:    gef
Version: 2025.01
Release: alt1

Summary: GEF (GDB Enhanced Features)
License: MIT
Group:   Development/Debuggers
URL:     https://hugsy.github.io/gef/
VCS:     https://github.com/hugsy/gef/

Requires: gdb

BuildArch: noarch

Source: %name-%version.tar

%description
GEF (pronounced "Jeff") is a set of commands for x86/64, ARM,
MIPS, PowerPC and SPARC to assist exploit developers and
reverse-engineers when using old school GDB. It provides additional
features to GDB using the Python API to assist during the process of
dynamic analysis and exploit development. Application developers will
also benefit from it, as GEF lifts a great part of regular GDB
obscurity, avoiding repeating traditional commands, or bringing out the
relevant information from the debugging runtime.

%prep
%setup
cat <<EOF > gdb-gef
#!/bin/bash

exec gdb -ex "source %_datadir/gdb/gef.py" "$@"
EOF

%install
mkdir -p %buildroot%_datadir/gdb
mv gef.py %buildroot%_datadir/gdb/gef.py

mkdir -p %buildroot/%_bindir
install -m 0755 gdb-gef %buildroot%_bindir/gdb-gef

%postun
echo "Don't forget to revert ~/.gdbinit if needed"

%files
%doc README.md LICENSE docs/*
%_datadir/gdb/gef.py
%_bindir/gdb-gef

%changelog
* Thu Jan 16 2025 Ilya Sorochan <k0tran@altlinux.org> 2025.01-alt1
- Initial build for Sisyphus.
