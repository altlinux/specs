Name: qpfstmo
Version: 1.0
Release: alt1

Summary: HDR Tone Mapping GUI
License: GPL
Group: Graphics

URL: http://theplaceofdeadroads.blogspot.com/2006/07/qpfstmo-hdr-tone-mapping-gui-for-linux_04.html
Source: http://home.comcast.net/~tpodr/qpfstmo-%version.tar.gz

Requires: pfstools pfstmo

# Automatically added by buildreq on Mon Jun 18 2007
BuildRequires: gcc-c++ kdelibs-devel libqt3-devel libXext-devel

%description
qpfstmo provides a Qt-based GUI for using the pfstmo binaries.

%prep
%setup -q

%build
qmake-qt3
%make_build

%install
install -pD -m755 qpfstmo %buildroot%_bindir/qpfstmo

%files
%doc README
%_bindir/*

%changelog
* Mon Jun 18 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- Initial build.
