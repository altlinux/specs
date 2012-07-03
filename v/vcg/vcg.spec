Name: vcg
Version: 1.30
Release: alt2

Summary: The VCG visualization tool for compiler graphs

License: GPL
Group: Graphics
Url: http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/%name.tar.bz2
Patch0: %name-LINUX.patch

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: libX11-devel libXext-devel

%description
The VCG tool reads a textual and readable specification of a graph and
visualizes the graph. If not all positions of nodes are fixed, the
tool layouts the graph using several heuristics as reducing the number
of crossings, minimizing the size of edges, centering of nodes. The
specification language of the VCG tool is nearly compatible to GRL,
the language of the edge tool, but contains many extensions. The VCG
tool allows folding of dynamically or statically specified regions of
the graph. It uses colors and runs on X11.

%prep
%setup -q -n %name.%version
%patch0 -p1 -z .pix

%build
make xvcg_gcc_noxmkmf xvcg \
	CFLAGS="-c %optflags" \
	BINDIR=%_bindir \
	MANDIR=%_man1dir

%install
install -d %buildroot{%_bindir,%_man1dir}

# do not override INSTALL
make install \
	SED=sed \
	BINDIR=%buildroot%_bindir \
	MANDIR=%buildroot%_man1dir

cp -f demo/demo.csh expl

%files
%doc README expl
%_bindir/*
%_man1dir/*

%changelog
* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt2
- update buildreqs

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

