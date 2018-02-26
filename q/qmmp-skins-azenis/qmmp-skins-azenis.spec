%define		src Qmmp_Azenis

Version:	0.1
Epoch:		1
Name:		qmmp-skins-azenis
Release:	alt1
Summary:	Azenis skin for QMMP
License: 	GPLv3+
Group: 		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		git://git.altlinux.org/people/drool/packages/qmmp-skins-azenis
Source0:	%src-%version.tar.bz2

BuildArch:	noarch
Requires:	winamplike-skins

BuildRequires:	rpm-build-wlskins

Conflicts:	qmmp < 0.2.3-alt1.M40.1

%description
Azenis skin for QMMP media player.

Based on Audacious Azenis skin:
http://kde-look.org/content/show.php/Azenis?content=77150

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_wlskindir/%src.tar.bz2

%files
%_wlskindir/*

%changelog
* Wed May 06 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.1-alt1
- another project packed

* Wed Apr 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4-alt1
- initial packing
