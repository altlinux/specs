%define svnrev 202
%define bname mplayer
%define skin_dir %_datadir/%bname/skins
%define excluded_skins standard mini netscape4 trium
Name: %bname-skins
Version: 2.0
Release: alt4
Summary: Skins for MPlayer
License: Like MPlayer
Group: Video
URL: http://%{bname}hq.hu
Source: %name-svn-r%svnrev.tar
BuildArch: noarch
Requires: mplayer-gui >= 0.90
Provides: MPlayer-skins = %version-%release
Obsoletes: MPlayer-skins
Packager: Led <led@altlinux.ru>
AutoProv: no
AutoReq: no

%description
Skins for MPlayer


%prep
%setup -n %name
find . -type d -print0 | xargs -0 chmod 755
find . -type f -print0 | xargs -0 chmod 644
%{?excluded_skins:[ -z "%excluded_skins" ] || rm -rf %excluded_skins}


%install
install -d -m 0755 %buildroot%skin_dir
cp -a * %buildroot%skin_dir/


%files
%dir %skin_dir
%skin_dir/*


%changelog
* Thu Jan 22 2009 Led <led@altlinux.ru> 2.0-alt4
- cleaned up spec

* Sun Oct 14 2007 Led <led@altlinux.ru> 2.0-alt3
- updated skins:
  + Blue
  + Blue-mini
  + smoothwebby
  + webby
- added skins:
  + Ater
  + plastik

* Wed Oct 04 2006 Led <led@altlinux.ru> 2.0-alt2
- updated some skins
- renamed MPlayer-skins to mplayer-skins

* Wed May 24 2006 Led <led@altlinux.ru> 2.0-alt1
- changed package version to 2.0 (because GTK+ 2)
- fixed URL
- fixed spec
- removed ugly skins
- added some skins
- updated some skins

* Fri Aug 22 2003 Grigory Milev <week@altlinux.ru> 1.1.0-alt1
- updated skins
- added more new skins

* Wed Sep 25 2002 Grigory Milev <week@altlinux.ru> 1.0.0-alt1
- moved from MPlayer to separate package
