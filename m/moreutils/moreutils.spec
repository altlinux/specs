Summary: A collection of unix tools
Name: moreutils
Version: 0.50
Release: alt2
License: GPLv2+
Group: Other
Source0: %{name}-%version.tar
Url: http://joeyh.name/code/moreutils/

BuildRequires: docbook-dtds
BuildRequires: docbook2X
BuildRequires: sed >= 4.0
BuildRequires: perl-podlators perl-IPC-Run

%description
A collection of unix tools that nobody thought to write long ago, when
unix was young. Currently it consists of these tools:

 - chronic: runs a command quietly unless it fails
 - ccombine: combine the lines in two files using boolean operations
 - errno: look up errno names and descriptions
 - ifdata: get network interface info without parsing ifconfig output
 - isutf8: check if a file or standard input is utf-8
 - ifne: run a command if the standard input is not empty
 - lckdo: execute a program with a lock held (deprecated)
 - mispipe: pipe two commands, returning the exit status of the first
 - parallel: run multiple jobs at once
 - pee: tee standard input to pipes
 - sponge: soak up standard input and write to a file
 - ts: timestamp standard input
 - vidir: edit a directory in your text editor
 - vipe: insert a text editor into a pipe
 - zrun: automatically uncompress arguments to command

NB: due to package conflicts, some utils packed with moreutils_ prefix

%prep
%setup

# Adjust paths for ALT:
sed -i -e 's,"file:///.*docbookx\.dtd","/usr/share/sgml/docbook/dtd/4.4/docbookx.dtd",' *.docbook

%build
%make_build DOCBOOK2XMAN=db2x_docbook2man

%install
%makeinstall_std
# ts conflicts with openssl :
mv %buildroot%_man1dir/ts.1 %buildroot%_man1dir/%{name}_ts.1
mv %buildroot%_bindir/ts %buildroot%_bindir/%{name}_ts
# parallel conflicts with gnu parallel:
mv %buildroot%_man1dir/parallel.1 %buildroot%_man1dir/%{name}_parallel.1
mv %buildroot%_bindir/parallel %buildroot%_bindir/%{name}_parallel

%files
%_bindir/chronic
%_bindir/combine
%_bindir/errno
%_bindir/ifdata
%_bindir/ifne
%_bindir/isutf8
%_bindir/lckdo
%_bindir/mispipe
%_bindir/%{name}_parallel
%_bindir/pee
%_bindir/sponge
%_bindir/%{name}_ts
%_bindir/vidir
%_bindir/vipe
%_bindir/zrun
%_man1dir/chronic.1*
%_man1dir/combine.1*
%_man1dir/errno.1*
%_man1dir/ifdata.1*
%_man1dir/ifne.1*
%_man1dir/isutf8.1*
%_man1dir/lckdo.1*
%_man1dir/mispipe.1*
%_man1dir/%{name}_parallel.1*
%_man1dir/pee.1*
%_man1dir/sponge.1*
%_man1dir/%{name}_ts.1*
%_man1dir/vidir.1*
%_man1dir/vipe.1*
%_man1dir/zrun.1*
%doc README

%changelog
* Mon Oct  7 2013 Terechkov Evgenii <evg@altlinux.org> 0.50-alt2
- parallel -> moreutils_parallel due to conflict with gnu parallel (tnx to mike@)

* Sat Oct  5 2013 Terechkov Evgenii <evg@altlinux.org> 0.50-alt1
- Initial build for ALT Linux Sisyphus (based on PLD spec)
