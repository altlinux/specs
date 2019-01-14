%define oname deadbeef
Name: %oname-etcskel
Version: 0.2
Release: alt1
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Summary: Configuration for %oname
License: Public
Group: Sound
Url: https://git.altlinux.org/people/antohami/packages/%name.git
BuildArch: noarch

Requires: deadbeef-full

%description
Configuration for %oname

%install
mkdir -p %buildroot/%_sysconfdir/skel/.config/%oname
cat >%buildroot%_sysconfdir/skel/.config/%oname/config<<END
gtkui.layout.0.6.2 vbox expand="0 1" fill="1 1" homogeneous=0 {hbox expand="0 1 0" fill="1 1 1" homogeneous=0 {playtb {} seekbar {} volumebar {} } hsplitter locked=1 ratio=0.327116 pos=228 size2=0 {vsplitter locked=0 ratio=0.638814 pos=0 size2=0 {pltbrowser {} coverart {} } playlist hideheaders=0 width=469 {} } }
END

%files
%_sysconfdir/skel/.config/%oname/config

%changelog
* Mon Jan 14 2019 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- clean config

* Fri Feb 10 2017 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus.
