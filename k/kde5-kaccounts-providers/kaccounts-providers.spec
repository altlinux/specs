%define rname kaccounts-providers

Name: kde5-%rname
Version: 15.4.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Accounts Providers
Url: http://www.kde.org
License: GPLv2+

BuildArch: noarch
#Requires: signon-ui

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 04 2015 (-bi)
# optimized out: cmake cmake-modules libqt5-core libstdc++-devel perl-Encode perl-XML-Parser pkg-config python-base python3 python3-base
#BuildRequires: extra-cmake-modules gcc-c++ intltool libdb4-devel qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libaccounts-glib-devel intltool

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --with-kde --all-name

%files
%config(noreplace) /etc/signon-ui/webkit-options.d/*.conf
/usr/share/accounts/providers/google.provider


%changelog
* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
