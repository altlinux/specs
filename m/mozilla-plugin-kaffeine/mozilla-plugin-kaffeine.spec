%define mozplug %browser_plugins_dir

Name: mozilla-plugin-kaffeine
Version: 0.2
Release: alt10

Summary: This mozilla plugin starts Kaffeine external for media streams
License: GPL
Group: Video
Url: http://kaffeine.sourceforge.net

Source: kaffeine-mozilla-%version.tar.bz2

# may be any kaffine found in PATH
#Requires: kaffeine

Provides: kaffeine-mozilla = %version-%release
Obsoletes: kaffeine-mozilla <= %version-%release
Provides: mozilla-kaffeine = %version-%release
Obsoletes: mozilla-kaffeine <= %version-%release
Provides:  mozilla-plugins-kaffeine = %version-%release
Obsoletes: mozilla-plugins-kaffeine <= %version-%release

# Automatically added by buildreq on Mon Apr 25 2011 (-bi)
# optimized out: elfutils libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libstdc++-devel python-base ruby xorg-xproto-devel
#BuildRequires: gcc-c++ gcc-fortran imake libXaw-devel rpm-build-ruby xorg-cf-files
BuildRequires: gcc-c++ libXaw-devel rpm-macros-browser-plugins

%description
This mozilla plugin starts Kaffeine external for media streams.

%prep
%setup -q -n kaffeine-mozilla-%version
#%__subst 's,\.la,\.so,' configure

%build
%configure --disable-static --prefix=%browser_plugins_path --libdir=%browser_plugins_path
%make_build

%install
%make install DESTDIR=%buildroot libdir=%browser_plugins_path


%files
%doc AUTHORS ChangeLog README
%browser_plugins_path/*.so


%changelog
* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.2-alt10
- fix build requires

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.2-alt9
- fix requires

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.2-alt8
- don't use old netscape plugins placement

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 0.2-alt7
- move to more accessible place

* Mon Nov 10 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt6
- rebuilt

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt5
- built with browser-plugins-npapi-devel

* Wed Jun 30 2004 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt4
- fix libraries placement

* Sat Jun 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt3
- change name of package

* Tue May 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt2
- remove mozilla requires 
- change name of package

* Tue May 18 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt1
- First version of RPM package.

