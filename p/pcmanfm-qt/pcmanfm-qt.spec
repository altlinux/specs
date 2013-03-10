Name:    pcmanfm-qt
Version: 0.1
Release: alt1

Summary: PCManFM-Qt is the Qt port of the LXDE file manager PCManFM
License: GPLv2+
Group:   File tools
Url:     http://blog.lxde.org/?p=966

Source:  %name-%version.tar
Source1: %name.desktop

BuildRequires: gcc-c++ qt4-devel cmake
BuildRequires: libfm-devel
BuildRequires: libXdmcp-devel

Requires: menu-cache

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM.
Libfm-Qt is a companion library providing components to build desktop file managers.

%prep
%setup
subst 's/lib$/lib${LIB_SUFFIX}/' CMakeLists.txt

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
rm -rf %buildroot%_includedir/libfm-qt
install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
#%%find_lang pcmanfm

#%%files -f pcmanfm.lang
%files
%_bindir/*
%_desktopdir/*.desktop
%_libdir/libfm-qt.so*

%changelog
* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus
