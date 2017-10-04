Name: rpm-build-qml
Version: 0.0.4
Release: alt1

Summary: RPM helper macros to rebuild QML packages
License: GPLv2+
Group: Development/Other

Source: %name-%version.tar

BuildRequires: qt5-declarative-devel
Conflicts: rpm-build < 4.0.4-alt100.91

%description
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%prep
%setup

%build
%make

%install
install -pD -m755 qmlinfo %buildroot%_bindir/qmlinfo
install -pD -m644 qml %buildroot%_rpmmacrosdir/qml
install -pD -m644 qml.env %buildroot%_rpmmacrosdir/qml.env
install -pD -m755 qml.prov %buildroot%_rpmlibdir/qml.prov
install -pD -m755 qml.prov.pl %buildroot%_rpmlibdir/qml.prov.pl
install -pD -m755 qml.prov.files %buildroot%_rpmlibdir/qml.prov.files
install -pD -m755 qml.req %buildroot%_rpmlibdir/qml.req
install -pD -m755 qml.req.files %buildroot%_rpmlibdir/qml.req.files

%files
%_rpmmacrosdir/qml
%_rpmmacrosdir/qml.env
%_rpmlibdir/qml.req
%_rpmlibdir/qml.req.files
%_rpmlibdir/qml.prov
%_rpmlibdir/qml.prov.pl
%_rpmlibdir/qml.prov.files
%_bindir/qmlinfo

%changelog
* Wed Oct 04 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.4-alt1
- Removed pipe

* Wed Oct 04 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.3-alt3
- Fix build in hsh

* Wed Oct 04 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.3-alt2
- Fix macro 

* Tue Oct 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.3-alt1
- Add missing versions (btw min and max)

* Mon Oct 02 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.2-alt1
- Getting provides from .so files (cpp by darktemplar@)

* Fri Sep 01 2017 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- Initial release
