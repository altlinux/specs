Name: unixbench
Version: 5.1.2
Release: alt2

Summary: The BYTE UNIX Benchmarks
License: Distributable
Group: Monitoring

Url: http://www.hermit.org/Linux/Benchmarking/
Source: %url/%name-%version.tar.gz
Patch0: unixbench-5.1.2-alt-makefile.patch
Patch1: unixbench-5.1.2-alt-nocheck.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Oct 15 2009
BuildRequires: libGL-devel libX11-devel libXext-devel

%description
The BYTE UNIX Benchmarks packaged for Inquisitor

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make

%install
sed -i "s,my \$BINDIR = getDir('UB_BINDIR'\,.*$,my \$BINDIR = getDir('UB_BINDIR'\,\""%_libdir/inquisitor"\")\;," Run
install -pDm755 Run %buildroot%_bindir/%name
mkdir -p        %buildroot%_libdir/inquisitor
cp -a pgms/*    %buildroot%_libdir/inquisitor
mkdir -p        %buildroot%_datadir/inquisitor/unixbench-testdir
cp -a testdir/* %buildroot%_datadir/inquisitor/unixbench-testdir

%files
%_bindir/*
%_libdir/inquisitor/*
%_datadir/inquisitor/unixbench-testdir

# TODO: make less inquisitor-specific?

%changelog
* Fri Feb 12 2010 Michael Shigorin <mike@altlinux.org> 5.1.2-alt2
- finally got around to gratefully accept fixes by vx8400@gmail

* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 5.1.2-alt1
- 5.1.2 built for Sisyphus
- fixed linking
- disabled make check in runtime (rather unneeded)
- minor spec cleanup
- buildreq

* Sat Jul 19 2008 Mikhail Yakshin <greycat@altlinux.org> 5.1.1-alt1
- Initial build

