%define visdir xmms-config --visualization-plugin-dir
%define plugloc %(%visdir)

Summary: OpenGL plugin for xmms
Name: lemuria
Version: 2.1.0
Release: alt2
License: GPL
Group: Video
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: %name-%version-autotools.patch

Url: http://gmerlin.sf.net/lemuria

BuildRequires(pre): xmms-devel

# Automatically added by buildreq on Mon Apr 26 2010
BuildRequires: imake libGL-devel libICE-devel libXext-devel 
BuildRequires: libXinerama-devel libgmerlin-devel libxmms-devel xorg-cf-files
BuildRequires: libGLU-devel

%description
Lemuria is an OpenGL visualization plugin with weird shapes, animated
textures and other fun stuff

%prep
%setup
%patch0 -p1

%build
AUTOPOINT=true %autoreconf
%configure

%make_build

%install
%makeinstall_std

%find_lang %name

%ifarch x86_64
 mv %buildroot/%_libexecdir/gmerlin   %buildroot/%_libdir/gmerlin
%endif

install -dp -m755 %buildroot/%xmms_effectdir/
mv %buildroot/%_libdir/*.so*  %buildroot/%xmms_effectdir/

rm -f %buildroot/%_libdir/liblemuria.la
rm -f %buildroot/%_libdir/gmerlin/plugins/*.la


%files  -f %name.lang
%doc README NEWS AUTHORS COPYING ChangeLog INSTALL
%_libdir/gmerlin/plugins/*.so
%xmms_effectdir/*.so*

%changelog
* Sun Dec 05 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.0-alt2
- add BuildRequires libGLU-devel

* Sun Apr 25 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Jul 05 2003 Burkhard Plaum <gmerlin@users.sourceforge.net>
- Initial spec file
