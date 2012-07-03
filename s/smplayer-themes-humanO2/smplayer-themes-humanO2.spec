%define		content 97267
%define		subname Human-O2

Name:		smplayer-themes-humanO2
Summary:	Theme icons for SMPlayer
License:	GPL
Group:		Video
Url:		http://qt-apps.org/content/show.php/Human-O2+for+SMplayer?content=%content
Version:	0.0.1
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://qt-apps.org/CONTENT/content-files/%content-HumanO2.Smplayer.tar.gz
BuildArch:	noarch
Requires:	smplayer >= 0.5.29

%description
Theme for SMplayer. Breathless Icons for SMPlayer based on the Breathless Icons for KDE.
Icons taken from http://www.kde-look.org/content/show.php/Breathless?content=60465.

%prep
%setup -q -n %subname

%install
mkdir -p %buildroot%_datadir/smplayer/themes/%subname
cp -r ./* %buildroot%_datadir/smplayer/themes/%subname/ && chmod 0644 %buildroot%_datadir/smplayer/themes/%subname/*.*

%files
%dir %_datadir/smplayer/themes/%subname
%_datadir/smplayer/themes/%subname/*.*

%changelog
* Sun Apr 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux
