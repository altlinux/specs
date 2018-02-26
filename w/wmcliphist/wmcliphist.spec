Name: wmcliphist
Version: 1.0
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Clipboard history dockable application for Window Maker
License: GPLv2+
Group: Graphical desktop/Window Maker

URL: http://linux.nawebu.cz/wmcliphist/
Source: %url/wmcliphist-%version.tar.gz
Source1: wmcliphist.README
Patch: wmcliphist-1.0-alt-DSO.patch

# Automatically added by buildreq on Thu Jul 30 2009
BuildRequires: libgtk+2-devel

%description
wmcliphist keeps history of clipboard operations and allows you to put
previously copied items back to clipboard for pasting to other applications.

%prep
%setup -n %name
%patch -p2

cp -a %SOURCE1 README.first

%build
%make_build CC="gcc %optflags"

%install
install -pD -m 755 wmcliphist %buildroot%_bindir/wmcliphist

%files
%doc AUTHORS ChangeLog README README.first wmcliphistrc
%_bindir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build

* Thu Jul 30 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- 1.0

* Thu Feb 08 2007 Victor Forsyuk <force@altlinux.org> 0.6-alt3
- Added readme file describing configuration option that fixes problem with
  selection resetting (reported in ALT#7910).

* Thu Mar 09 2006 Victor Forsyuk <force@altlinux.ru> 0.6-alt2
- Fixed build with --as-needed.

* Wed Apr 06 2005 Victor Forsyuk <force@altlinux.ru> 0.6-alt1
- 0.6

* Sat Jun 28 2003 Alex Ott <ott@altlinux.ru> 0.5-alt1
- New version

* Sat Jun 07 2003 Ott Alex <ott@altlinux.ru> 0.4-alt1
- Initial build
