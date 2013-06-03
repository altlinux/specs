%define svnrev 215
%define bname mplayer
%define skin_dir %_datadir/%bname/skins
Name: %bname-skins
Version: 2.0
Release: alt5
Summary: Skins for MPlayer
License: Like MPlayer
Group: Video
URL: http://%{bname}hq.hu
Source: %name-svn-r%svnrev.tar
Patch: %name-%version-%release.patch
BuildArch: noarch
Requires: mplayer-gui >= 0.90
Provides: MPlayer-skins = %version-%release
Obsoletes: MPlayer-skins
AutoReqProv: no

%description
Skins for MPlayer


%prep
%setup -n %name
%patch -p1


%install
for d in *; do
	install -d -m 0755 %buildroot%skin_dir/$d
	for f in $d/*; do
		[ -d $f ] || install -p -m 0644 $f %buildroot%skin_dir/$d/
	done
done


%files
%dir %skin_dir
%skin_dir/*
%exclude %skin_dir/Noskin
%exclude %skin_dir/standard


%changelog
* Tue Jun 04 2013 Led <led@altlinux.ru> 2.0-alt5
- update to SVR rev. 215
- cleaned up spec
- fixed config for skins:
  + Corelian
  + avifile
  + tvisor
  + xanim

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
