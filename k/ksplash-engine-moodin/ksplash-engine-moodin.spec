%undefine __libtoolize
%define qtdir %_qt3dir
%define kdedir %_K3prefix
%define ename moodin

Name: ksplash-engine-%ename
Version: 0.4.2
Release: alt4

Group: Graphical desktop/KDE
Summary: Splash Screen Engine for KDE
License: GPL
URL: http://moodwrod.com/files/

BuildRequires(pre): kdebase-devel
Requires: kdelibs >= %{get_version kdelibs}

Source: ksplash-engine-%{ename}_%version.tar.gz
Source1: ksplash%ename.desktop

Patch0: ksplash-engine-moodin-0.4.2-alt-DSO.patch

BuildRequires: automake autoconf
BuildRequires: gcc-c++
BuildRequires: libpng3-devel libjpeg-devel

%description
Heavily customizable engine for various types of themes

%prep
%setup -q -n %ename
%patch0 -p2

# cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
# cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
# make -f admin/Makefile.common

%build
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%add_optflags -I%_includedir/tqtinterface
%K3configure \
	--without-arts \
        --enable-final \
        --disable-rpath \
        --enable-shared \
        --disable-static \
        --disable-debug \
        --program-transform-name=""

%make_build

%install
%K3install
cp -f %SOURCE1 %buildroot%_K3srv/
%files
%doc src/doc/THEMEOPTIONS debian/changelog
%_K3lib/ksplashmoodin.so
%_K3apps/ksplash/Themes/*
%_K3srv/*.desktop

%changelog
* Mon Jul 23 2012 Roman Savochenko <rom_as@altlinux.org> 0.4.2-alt4
- Rebuild for TDE 3.5.13 environment.

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt2.qa1
- Disable aRts support
- Adapt to new KDE3 placement

* Sat Feb 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.4.2-alt2
- Fixed buildrequires
- Spec cleanup (for x86_64 build)

* Mon Jan 08 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.4.2-alt1
- Initial spec (based on kde-styles-activeheart-kwin)

