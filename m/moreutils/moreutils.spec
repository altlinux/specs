%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Summary: A collection of unix tools
Name: moreutils
Version: 0.67
Release: alt1
License: GPLv2+
Group: File tools
Source0: %name-%version.tar
Url: http://joeyh.name/code/moreutils/
Vcs: https://git.joeyh.name/index.cgi/moreutils.git

BuildRequires: docbook2X
BuildRequires: docbook-dtds
BuildRequires: perl-IPC-Run
BuildRequires: perl-podlators
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
}}

%description
A collection of unix tools that nobody thought to write long ago, when
unix was young. Currently it consists of these tools:

 - chronic: runs a command quietly unless it fails
 - combine: combine the lines in two files using boolean operations
 - errno: look up errno names and descriptions
 - ifdata: get network interface info without parsing ifconfig output
 - isutf8: check if a file or standard input is utf-8
 - ifne: run a command if the standard input is not empty
 - lckdo: execute a program with a lock held (deprecated)
 - mispipe: pipe two commands, returning the exit status of the first
 - parallel: run multiple jobs at once (in %name-parallel package)
 - pee: tee standard input to pipes
 - sponge: soak up standard input and write to a file
 - ts: timestamp standard input
 - vidir: edit a directory in your text editor
 - vipe: insert a text editor into a pipe
 - zrun: automatically uncompress arguments to command

%package parallel
Summary: Run multiple jobs at once
Group: File tools
Conflicts: parallel

%description parallel
parallel runs the specified command, passing it a single one of the
specified arguments. This is repeated for each argument. Jobs may be
run in parallel. The default is to run one job per CPU.

%prep
%setup

# Adjust paths for ALT:
sed -i -e 's,"file:///.*docbookx\.dtd","/usr/share/sgml/docbook/dtd/4.4/docbookx.dtd",' *.docbook

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build DOCBOOK2XMAN=db2x_docbook2man CC=gcc CFLAGS="%optflags"

%install
%makeinstall_std
# ts's man conflicts with openssl :
mv %buildroot%_man1dir/ts.1 %buildroot%_man1dir/%{name}_ts.1

%check
make check

%files
%doc README is_utf8/README.md COPYING
%_bindir/*
%_man1dir/*.1*
%exclude %_bindir/parallel
%exclude %_man1dir/parallel.1*

%files parallel
%doc COPYING
%_bindir/parallel
%_man1dir/parallel.1*

%changelog
* Wed Jan 25 2023 Vitaly Chikunov <vt@altlinux.org> 0.67-alt1
- Update to 0.67 (2021-12-21).
- Enabled LFS on 32-bit systems.
- parallel is packaged in %name-parallel instead of renaming the tool.

* Tue Aug  1 2017 Terechkov Evgenii <evg@altlinux.org> 0.61-alt1
- 0.61 (ALT#33713)

* Mon Oct  7 2013 Terechkov Evgenii <evg@altlinux.org> 0.50-alt2
- parallel -> moreutils_parallel due to conflict with gnu parallel (tnx to mike@)

* Sat Oct  5 2013 Terechkov Evgenii <evg@altlinux.org> 0.50-alt1
- Initial build for ALT Linux Sisyphus (based on PLD spec)
