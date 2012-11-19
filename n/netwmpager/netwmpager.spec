Name: netwmpager
Version: 2.04
Release: alt1

Summary: A NetWM/EWMH compatible pager
License: GPLv2+
Url: http://freecode.com/projects/netwmpager
Group: Graphical desktop/Other

Source0: %name-%version.tar.bz2

Patch0: netwmpager-1.11-alt-DSO.patch
Patch1: netwmpager-2.04-alt.patch
Patch2: netwmpager-2.04-alt-optflags.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Mon Nov 19 2012
BuildRequires: libXft-devel

%description
EWMH (NetWM) compatible pager. Works with Openbox and other EWMH
compliant window managers.

%prep
%setup -q
%patch0 -p2
%patch1 -p1
%patch2 -p1

%build
sed -i "s#@RPM_OPT_FLAGS@#$RPM_OPT_FLAGS#" config.mk
%make_build V=2

%install
mkdir -p %buildroot%_bindir/
install -pD -m755 netwmpager %buildroot%_bindir/

%files
%doc AUTHORS Changelog README config-example
%_bindir/*

%changelog
* Mon Nov 19 2012 Igor Zubkov <icesik@altlinux.org> 2.04-alt1
- 1.11 -> 2.04
- Update Url
- Respect RPM_OPT_FLAGS

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.1
- Fixed build

* Fri Mar 07 2008 Igor Zubkov <icesik@altlinux.org> 1.11-alt1
- build for Sisyphus


