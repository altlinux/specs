%global repo dpa-ext-gnomekeyring

Name: deepin-polkit-agent-ext-gnomekeyring
Version: 5.0.4
Release: alt1
Summary: GNOME keyring extension for Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-tools libgnome-keyring-devel deepin-polkit-agent-devel

%description
%summary.

%prep
%setup -n %repo-%version
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/usr/lib|/usr/libexec|' dpa-ext-gnomekeyring.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %repo

%files -f %repo.lang
%dir %_prefix/libexec/polkit-1-dde/
%dir %_prefix/libexec/polkit-1-dde/plugins/
%_prefix/libexec/polkit-1-dde/plugins/lib%repo.so
%_datadir/%repo/

%changelog
* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus.
