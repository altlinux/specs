Name: clipart-sodipodi-flags
Version: 1.6
Release: alt2

Summary: Sodipodi Flag collection
License: Public domain
Group: Graphics

Url: http://sodipodi.sourceforge.net/
Source: http://prdownloads.sourceforge.net/sodipodi/sodipodi-flags-%version.tar.bz2
Patch1: sodipodi-flags-alt-build.patch

Summary(ru_RU.KOI8-R): Коллекция флагов проекта sodipodi

Buildarch: noarch

%define clip_dir %_datadir/design/cliparts/sodipodi-flags
%define flags_dir %_iconsdir/flags

# please do not use buildreq
BuildPreReq: perl-base

%description
This is meant to be a collection of flags which you can freely use for software,
school and University papers, newspapers, books and whatever you could possibly
use flags for.

%description -l ru_RU.KOI8-R
Коллекция флагов, которую вы можете свободно использовать в своих программах,
в школьных и университетских работах, газетах, книгах, и во всём, в чём
только можно использовать флаги. 

%package -n flags
Summary: Flag collection for gswitchit
License: Public domain
Group: Graphics
Provides: gnome-applets-gswitchit-plugins-flags-data
Requires: %name = %version-%release

%description -n flags
Flag collection for gswitchit

%description -n flags -l ru_RU.KOI8-R
Коллекция флагов для gswitchit

%prep
%setup -q -n sodipodi-flags
%patch1 -p1

%build
%__perl gen_cc.pl %clip_dir

%install

%__install -d %buildroot%clip_dir
# separate flags for keyboard switchers
%__install -d %buildroot%flags_dir
%__cp -pr * %buildroot%clip_dir
%__mv %buildroot%clip_dir/cc/* %buildroot%flags_dir
%__rm -rf %buildroot%clip_dir/cc

%files
%dir %clip_dir
%clip_dir/*
%doc README COPYING CREDITS

%files -n flags
%flags_dir
%doc README COPYING CREDITS

%changelog
* Mon Jun 21 2004 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt2
- split switcher's flags into separate package

* Tue Jun  8 2004 Ildar Mulyukov <ildar@users.sourceforge.net> 1.6-alt1
- new version
- now Provides: gnome-applets-gswitchit-plugins-flags-data
- added flags symlinks to /usr/share/icons/flags

* Sun Jan 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- first build for Sisyphus
