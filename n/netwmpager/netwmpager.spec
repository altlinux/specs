Name: netwmpager
Version: 1.11
Release: alt1.1

Summary: A NetWM/EWMH compatible pager
License: GPLv2+
Url: http://onion.dynserv.net/~timo/netwmpager.html
Group: Graphical desktop/Other

Source0: %name-%version.tar.bz2
Patch0: netwmpager-1.11-alt-DSO.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Fri Mar 07 2008
BuildRequires: libXft-devel

%description
EWMH (NetWM) compatible pager. Works with Openbox and other EWMH
compliant window managers.

%prep
%setup -q
%patch0 -p2

%build
./configure --prefix=%_prefix
%make_build

%install
mkdir -p %buildroot%_bindir/
install -pD -m755 netwmpager %buildroot%_bindir/

%files
%doc README config-example
%_bindir/*

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.1
- Fixed build

* Fri Mar 07 2008 Igor Zubkov <icesik@altlinux.org> 1.11-alt1
- build for Sisyphus


