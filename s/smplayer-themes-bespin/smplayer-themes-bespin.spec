%define		content 119113
%define		subname Bespin

Name:		smplayer-themes-bespin
Summary:	Theme icons for SMPlayer
Summary(ru_RU.UTF-8): Тема иконок для SMPlayer
License:	GPLv2
Group:		Video
Url:		http://kde-look.org/content/show.php/SMplayer+Bespin+theme?content=%content
Version:	0.2
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source:		http://kde-look.org/CONTENT/content-files/%content-Bespin-0.2.tar.gz
BuildArch:	noarch
PreReq:		smplayer >= 0.6.9

%description
Bespin SMplayer theme created to match Bespin desktop icons. Only GUI icons (no menus or preferences).

%description -l ru_RU.UTF-8
Тема иконок Bespin для SMPlayer, создана соответственно на базе темы
Bespin иконок рабочего стола. Только GUI иконки (иконки меню и настроек не включены).

%prep
%setup -q -n %subname

%install
mkdir -p %buildroot%_datadir/smplayer/themes/%subname
cp -r ./* %buildroot%_datadir/smplayer/themes/%subname/ 
chmod 0644 %buildroot%_datadir/smplayer/themes/%subname/*

%files
%dir %_datadir/smplayer/themes/%subname
%_datadir/smplayer/themes/%subname/*

%changelog
* Tue May 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1
- build for ALT Linux. Thanx to Vladimir aka Queq for full src.rpm
