Name: hid-replay
Version: 0.6
Release: alt1

Summary: HID Input device recorder and replay
Group: Development/Tools
License: GPLv2+
URL: https://github.com/bentiss/%name

Source0:        https://github.com/bentiss/%name/archive/%version/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: asciidoc xmlto

%description
%name is a tool that allow users to capture hidraw description and
events in order to replay them through the uhid kernel module.

%prep
%setup -q

%build
autoreconf -fisv
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README
%_bindir/%name
%_bindir/hid-recorder
%_man1dir/%name.*
%_man1dir/hid-recorder.*

%changelog
* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.6-alt1
- Build for Sisyphus

* Fri Dec 13 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.6-1
- Bumped to version 0.6

* Mon May 27 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.5-1
- Bumped to version 0.5

* Tue Apr 16 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.4-1
- Bumped to version 0.4

* Wed Mar 20 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.3-1
- Bumped to version 0.3

* Thu Nov 15 2012 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1-1
- Initial package
