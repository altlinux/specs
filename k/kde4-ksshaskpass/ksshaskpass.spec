%define _kde_alternate_placement 1
%define openssh_askpass_dir %_libexecdir/openssh

%define rname ksshaskpass
Name: kde4-ksshaskpass
Version: 0.5.3
Release: alt2

Group: Networking/Remote access
Summary: A KDE version of ssh-askpass with KWallet support
License: GPLv2
Url: http://www.kde-apps.org/content/show.php?content=50971

PreReq: alternatives >= 0:0.4, %openssh_askpass_dir
PreReq: alternatives >= 0:0.4, %openssh_askpass_dir
Requires: openssh-askpass-common
Provides: %openssh_askpass_dir/ssh-askpass
Provides: openssh-askpass-kde4 = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Apr 24 2014 (-bi)
# optimized out: alternatives automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu50 qt4-designer ruby ruby-stdlibs zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde-common-devel

%description
A KDE version of ssh-askpass with KWallet support

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install

mkdir -p %buildroot/%openssh_askpass_dir/
mv %buildroot/%_kde4_bindir/%rname \
    %buildroot/%openssh_askpass_dir/%name


# setup environment variables
#mkdir -p %buildroot/%_sysconfdir/kde4/env/
#cat > %buildroot/%_sysconfdir/kde4/env/%rname.sh << EOF
#SSH_ASKPASS=%openssh_askpass_dir/%name
#export SSH_ASKPASS
#EOF
#chmod 0755 %buildroot/%_sysconfdir/kde4/env/%rname.sh

# setup alternative
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name<<EOF
%openssh_askpass_dir/ssh-askpass        %openssh_askpass_dir/%name        30
EOF


%files
%doc ChangeLog README
#%config(noreplace) %_sysconfdir/kde4/env/%rname.*
%_altdir/%name
%openssh_askpass_dir/%name
%_kde4_xdg_apps/%rname.desktop

%changelog
* Fri Feb 12 2016 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt2
- rebuild

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt0.M70P.1
- built for M70P

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- initial build
