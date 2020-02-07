%define sname mediawriter
%define oname ALTMediaWriter

Name:           altmediawriter
Version:        0.1.0
Release:        alt1
Summary:        ALT Media Writer
Group:          System/Configuration/Other

License:        GPLv2+
URL:            https://github.com/altlinux/ALTMediaWriter
Source:         %oname-%version.tar
Patch:          %oname-%version-alt.patch

BuildRequires:  qt5-base-devel
BuildRequires:  qt5-declarative-devel qt5-x11extras-devel
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  liblzma-devel

Requires:       qt5-quickcontrols2
Requires:       polkit

Requires: udisks2

%description
A tool to write images of ALT media to portable drives
like flash drives or memory cards.

%prep
%setup -n %oname-%version
%patch -p1

%build
%qmake_qt5 PREFIX=%_prefix LIBEXECDIR=%_libexecdir/%name MEDIAWRITER_NAME=%name MEDIAWRITER_VERSION=%version-%release
make

%install
make install INSTALL_ROOT=%buildroot
if [ "%name" != "%sname" ]; then
    for i in %buildroot%_datadir/icons/hicolor/*/apps/%sname.png; do
        mv "$i" "$(dirname $i)/%name.png"
    done
    mv %buildroot%_datadir/applications/%sname.desktop %buildroot%_datadir/applications/%name.desktop
    mv %buildroot%_datadir/appdata/%sname.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml
    sed -i 's/=%sname$/=%name/g' %buildroot%_datadir/applications/%name.desktop
    sed -i 's/%sname\.desktop/%name.desktop/' %buildroot%_datadir/appdata/%name.appdata.xml
fi

%check
appstream-util validate-relax --nonet %buildroot/%_datadir/appdata/%name.appdata.xml

%files
%_bindir/%name
%_libexecdir/%name/
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png


%changelog
* Tue Nov 05 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
