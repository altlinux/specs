%def_disable ubuntuicons

Name: nitrokey-app
Version: 0.6.3
Release: alt2
License: %gpl3only
Summary: Nitrokey's Application
Url: https://www.nitrokey.com/
Group: System/Configuration/Other

# git clone https://github.com/Nitrokey/nitrokey-app.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake rpm-build-xdg

# Automatically added by buildreq on Wed Oct 19 2016
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-widgets libstdc++-devel perl pkg-config python-base python-modules
BuildRequires: cmake libusb-devel qt5-base-devel

%description
The implementation is compatible to the Google Authenticator application
which can be used for testing purposes. See google-authenticator.

Using the application under Linux also requires root privileges, or
configuration of device privileges in udev (due to USB communication).

%prep
%setup
%patch -p1
perl -p -i -e 's|\r\n|\n|g' OTP_full_specification.txt
sed -e 's,\<plugdev\>,_cryptodev,g' -i_ data/40-nitrokey.rules
diff -u data/40-nitrokey.rules{_,} ||:

%build
%cmake \
	-DHAVE_LIBAPPINDICATOR:BOOL=FALSE \
	#
%cmake_build V=1 VERBOSE=1

%install
%cmakeinstall_std

mkdir -p %buildroot%_udevrulesdir
mv %buildroot/usr/lib/udev/rules.d/40-nitrokey.rules \
	%buildroot%_udevrulesdir/

mkdir -p %buildroot%_xdgconfigdir/autostart
cat > %buildroot%_xdgconfigdir/autostart/nitrokey-app.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Nitrokey App
Comment=Launch Nitrokey App tray program
Icon=nitrokey-app
Exec=nitrokey-app
@@@

%find_lang %name

%pre
groupadd -r _cryptodev ||:

%files -f %name.lang
%_sysconfdir/bash_completion.d/nitrokey-app
%_bindir/nitrokey-app
%_datadir/applications/nitrokey-app.desktop
%_xdgconfigdir/autostart/nitrokey-app.desktop
%_datadir/icons/hicolor/*/apps/nitrokey-app.*
%if_enabled ubuntuicons
%_datadir/icons/ubuntu-mono-*/apps/*/nitrokey-app.*
%else
%exclude %_datadir/icons/ubuntu-mono-*/apps/*/nitrokey-app.*
%endif
%_datadir/nitrokey/
%_datadir/pixmaps/nitrokey-app.png
%_udevrulesdir/40-nitrokey.rules
%doc OTP_full_specification.txt README.md

%changelog
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt2
- Updated build dependencies.

* Mon Feb 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3.

* Thu Dec 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.1-alt1
- Updated to 0.6.1.

* Wed Oct 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.1-alt1
- Initial build.
