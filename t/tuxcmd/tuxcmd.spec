# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           tuxcmd
Version:        0.6.70
Release:        alt2
Summary:        Tux Commander: file manager with 2 panels side by side using GTK2

Group:          File tools
License:        GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
# FreePascal restrictions
ExcludeArch:    s390 s390x

URL:            http://tuxcmd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-modules-%{version}.tar.bz2

BuildRequires: fpc >= 2.6.2-4%{?dist}
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils
BuildRequires: libgcc

# turn smartlinking off, not needed anymore with fpc-2.2.2-2
Patch4: tuxcmd-disable-smartlinking.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=755320
# Bug 755320 - tuxcmd can not be built due to new libarchive and new glib
Patch5: tuxcmd-module-libarchive_libarchive-3.0.0a.patch
Patch6: tuxcmd-module-gvfs_include-glib.patch

# GCC 4.7 compatibility
Patch7: tuxcmd-module-ziparchive-gcc-4.7.patch
Patch8: tuxcmd-module-ziparchive-gcc-4.7-2.patch

# ARM linking compatibility
Patch9: tuxcmd-arm-gcc_s.so-linking.patch
Source44: import.info

%description
Tux Commander is open-source file manager with 2 panels side by side written
for GTK2. The main goal of this project is to create powerful user-friendly
file manager for Linux. Functionality can be further extended by pluggable
VFS (virtual file system) modules.


%package modules
Summary:        Modules for Tux Commander file manager
Group:          File tools
Requires: %{name} = %{version}-%{release}
BuildRequires: libarchive-devel >= 2.5.5
BuildRequires: bzip2-devel

%description modules
The tuxcmd-modules package contains extra VFS (virtual file system) modules
extending Tux Commander's functionality:
 * libarchive plugin - handles TAR/GZ/BZ2 archives
 * ZIP plugin


%package gvfs
Summary:        GVFS module for Tux Commander file manager
Group:          File tools
Requires: %{name} = %{version}-%{release}
Requires: gvfs

%description gvfs
This package contains networking GVFS module for Tux Commander file manager.




%prep
%setup -q -b 1
%patch4 -p1 -b .disable-smartlinking
# dirty hack to workaround weird linking issue
ln -s %{_libdir}/libgcc_s.so.1 libgcc_s.so
%patch9 -p1 -b .arm-gcc_s.so-linking

pushd ../%{name}-modules-%{version}
%patch5 -p1 -b .libarchive3
%patch6 -p1 -b .glib-include
%patch7 -p1 -b .gcc-4.7
%patch8 -p1 -b .gcc-4.7-2
popd

%build

make final_debug

# build modules
cd ../%{name}-modules-%{version}
make CC="gcc %{optflags}" CPP="g++ %{optflags}" shared


%install
make install DESTDIR=$RPM_BUILD_ROOT/usr
desktop-file-install --delete-original  \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    $RPM_BUILD_ROOT%{_datadir}/applications/tuxcmd.desktop

find $RPM_BUILD_ROOT -name COPYING -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name README -exec rm -f {} ';'

# install modules
cd ../%{name}-modules-%{version}
make install DESTDIR=$RPM_BUILD_ROOT/usr
mkdir -p doc/libarchive
cp -pr libarchive/{COPYING,README} doc/libarchive
mkdir -p doc/zip
cp -pr zip/{COPYING,README} doc/zip



%files
%doc COPYING README
%dir %{_libdir}/tuxcmd
%{_bindir}/tuxcmd
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%files modules
%doc ../%{name}-modules-%{version}/doc/libarchive
%doc ../%{name}-modules-%{version}/doc/zip
%{_libdir}/tuxcmd/libarchive_plugin.so
%{_libdir}/tuxcmd/libzip_plugin.so

%files gvfs
%doc ../%{name}-modules-%{version}/gvfs/README
%doc ../%{name}-modules-%{version}/gvfs/COPYING
%{_libdir}/tuxcmd/libgvfs_plugin.so


%changelog
* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.6.70-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.70-alt1_13
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.70-alt1_12
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.70-alt1_10
- initial fc import

