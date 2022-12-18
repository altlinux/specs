Name: linssid
Release: alt1
Version: 3.6

License: GPL-3
Group: Monitoring
Url: http://sf.net/projects/linssid

Source0: %{name}_%{version}.orig.tar.gz

Summary: Graphical wireless scanner

BuildRequires: boost-devel libqwt6-qt5-devel qt5-svg-devel

Requires: iw, wireless-tools

%description
LinSSID displays locally receivable 802.11 wireless attach points
and ad hoc networks. A table is displayed with various parameters
such as MAC address, channel, and signal strength. Graphs are also
displayed with signal strength by channel and signal strength over
time. This is very useful for finding channels with low interference
for setting up a wireless router.

LinSSID requires root privileges, and PolicyKit is used for it.

%prep
%setup

sed "s|/usr/lib/|%_libdir/|"                   -i linssid-app/linssid-app.pro
sed "s|/usr/include/qwt|/usr/include/qt5/qwt|" -i linssid-app/linssid-app.pro

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot install

%files
%doc linssid-app/license.txt

%_bindir/linssid-pkexec
%_sbindir/linssid
%_desktopdir/linssid.desktop

%dir %_datadir/linssid
%_datadir/linssid/linssid-pause.png
%_datadir/linssid/linssid-start.png
%_datadir/linssid/oui.datc

%_pixmapsdir/linssid-pause.png
%_pixmapsdir/linssid-start.png
%_pixmapsdir/linssid.png
%_pixmapsdir/linssid.svg
%_pixmapsdir/linssid48.png

%_datadir/polkit-1/actions/com.warsev.pkexec.linssid.policy

%changelog
* Sun Dec 18 2022 Sergey Y. Afonin <asy@altlinux.org> 3.6-alt1
- Initial build for ALT Linux
