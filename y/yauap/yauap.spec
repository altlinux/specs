Name: yauap
Version: 0.2.4
Release: alt1

Summary: A simple commandline frontend for GStreamer
Group: Sound
License: LGPL v2 or later

Url: http://savannah.nongnu.org/projects/yauap/

Source0: %name-%version.tar.gz

Patch0: yauap-0.2pre1-alt-as-needed.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Mon Jan 14 2008
BuildRequires: gst-plugins-devel libdbus-glib-devel

%description
yauap is a simple commandline audio player based on GStreamer.

%prep
%setup -q
%patch0 -p1

%build
export RPM_OPT_FLAGS="%optflags"
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m 755 yauap %buildroot%_bindir/

%files
%doc ChangeLog README
%_bindir/%name

%changelog
* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Jan 14 2008 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt1
- 0.2.1 -> 0.2.2
- buildreq

* Sat Nov 24 2007 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- 0.2 -> 0.2.1

* Wed Oct 24 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt2
- 0.2pre1 -> 0.2

* Tue Feb 20 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt1.pre1
- build for Sisyphus

