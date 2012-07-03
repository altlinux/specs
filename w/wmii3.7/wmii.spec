Name: wmii3.7
Version: 3.7
Release: alt1

Summary: Window manager improved 2
License: MIT
Group: Graphical desktop/Other
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

URL: http://wmii.de
Source: %name-%version-%release.tar

Requires: ixpc0 dmenu
Conflicts: wmii

# Automatically added by buildreq on Tue Apr 03 2007
BuildRequires: libXt-devel libixp0-devel

%description
Wimp is dead!! - wmii is a dynamic window manager for X11.  It supports
classic and dynamic window management with extended keyboard, mouse, and
filesystem based remote control.  It replaces the workspace paradigm with
a new tagging approach.

%prep
%setup -n %name-%version-%release

%build
gcc %optflags -DVERSION=\"%version-%release\" -Iinclude cmd/wmii/*.c cmd/util.c -o wmii -lX11 -lixp -lm
gcc %optflags cmd/wmii9menu.c -o wmii9menu -lX11

%install
install -pD -m755 wmii %buildroot%_bindir/wmii
install -pD -m755 wmii9menu %buildroot%_bindir/wmii9menu
install -pD -m755 cmd/wmiir.sh %buildroot%_bindir/wmiir
install -pD -m755 cmd/wmiistartrc.sh %buildroot%_bindir/wmiistartrc
install -pD -m755 cmd/wmiiloop.awk %buildroot%_bindir/wmiiloop

%define wmiidir /etc/wmii-3.5
install -pD -m755 rc/wmiirc.sh %buildroot%wmiidir/wmiirc
install -pD -m755 rc/welcome.sh %buildroot%wmiidir/welcome

mkdir -p %buildroot%_man1dir
install -p -m744 man/wmii*.1 %buildroot%_man1dir/

install -pD -m644 wmii.png %buildroot%_niconsdir/wmii.png
mkdir -p %buildroot/etc/X11/wmsession.d
cat >%buildroot/etc/X11/wmsession.d/11wmii <<EOF
NAME=wmii
ICON=%_niconsdir/wmii.png
DESC=%summary
EXEC=%_bindir/wmii
SCRIPT:
exec %_bindir/wmii
EOF

%files
%doc LICENSE README
%config %wmiidir/
%_bindir/wmii*
%_man1dir/wmii*
%config /etc/X11/wmsession.d/11wmii
%_niconsdir/wmii.png

%changelog
* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1
- Rebuilt old version as %name

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.7-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for wmii
  * postclean-05-filetriggers for spec file

* Tue Apr 03 2007 Alexey Tourbin <at@altlinux.ru> 3.7-alt0.1
- imported sources from suckless.org mercurial repo into git
- updated to most recent snapshot and set version to 3.7
- wmiirc: changed default MODKEY from Alt to Win
- wmiirc: changed default terminal emulator form xterm to xvt

* Sun Jun 18 2006 Alexey Tourbin <at@altlinux.ru> 3.1-alt1
- initial revision
- sync debian wmii_3.0-1.diff.gz
- wmiirc: 
  + always regenerate proglist
  + changed /tmp/ns.$USER.$DISPLAY to ${TMPDIR:-/tmp}/ns.$USER.$DISPLAY
