Name: sound-theme-freedesktop
Version: 0.7
Release: alt1

Summary: freedesktop.org sound theme
Group: Graphical desktop/Other
# For details on the licenses used, see README
License: GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url: http://www.freedesktop.org/wiki/Specifications/sound-theme-spec

Source: http://people.freedesktop.org/~mccann/dist/%name-%version.tar.bz2

BuildArch: noarch
BuildRequires: intltool

%description
The default freedesktop.org sound theme following the XDG theming
specification. (http://0pointer.de/public/sound-theme-spec.html)

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%post
/bin/touch --no-create %_datadir/sounds/freedesktop %_datadir/sounds

%postun
/bin/touch --no-create %_datadir/sounds/freedesktop %_datadir/sounds

%files -f %name.lang
%doc README NEWS 
%dir %_datadir/sounds/freedesktop
%dir %_datadir/sounds/freedesktop/stereo
%_datadir/sounds/freedesktop/index.theme
%_datadir/sounds/freedesktop/stereo/*.oga

%changelog
* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- adopted for Sisyphus

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com 0.1-4
- Fix changelog

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com 0.1-3
- Touch root dirs, not just theme dirs

* Mon Aug 11 2008 Jeremy Katz <katzj@redhat.com> - 0.1-2
- require touch for scriptlets to not give errors

* Sun Jun 15 2008 Lennart Poettering <lpoetter@redhat.com> 0.1-1
- Initial package
