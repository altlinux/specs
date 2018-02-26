BuildRequires: gcc-c++
AutoReq: yes,nopython
Name:           yofrankie-bge
# Upstream developer claims the following:
# The site puts the last "technical demo" before the DVD release at
# version 1.2; that may make the DVD version 1.3.
# Then upstream released versions 1.1, 1.1a, 1.1b; so we introduced
# epoch.
Version:        1.1b
Epoch:          1
Release:        alt1_4.20100605svn
Summary:        3D Game with characters from Big Buck Bunny movie

Group:          Games/Other
# See yofrankie-DVD-license.txt for the full text, and here's some
# clarification:
# Basically, all the game data is CC-BY, but logos are distributed
# under terms that are not dissimilar to ones of Firefox logos.
# Shortly put: They're excluded from CC-BY, but you can redistribute
# them with the game data. (The game DVD license allows the DVDs to
# be "duplicate the DVDs and distribute or sell them", not having to
# modify the contents, but use on cover art is restricted).
License:        CC-BY and Freely redistributable without restriction
URL:            http://www.yofrankie.org/
# svn export -r101 https://svn.blender.org/svnroot/yofrankie/trunk@101 yofrankie-bge
# make -C yofrankie-bge xz
Source0:        yofrankie-%{version}.tar.xz
# This is the license as it is on the Game DVD
# Game developer confirmed that this is the license to be used here
# and was asked to include it in SVN repository
Source1:        yofrankie-DVD-license.txt
Patch0:         yofrankie-bge-1.3-imgcompr.patch
Patch1:         yofrankie-bge-1.1b-wrapper.patch

BuildRequires:  desktop-file-utils
# We don't need blender now that we don't compress images and modify .blend files
BuildRequires:  blender
BuildRequires:  python
BuildRequires:  ImageMagick
Requires:       /usr/bin/blenderplayer
BuildArch:      noarch
Source44: import.info

%description
Yo Frankie! is an open source computer game by the Blender Institute.
It is based on the universe and characters of the open source film Big
Buck Bunny.  In the game, players assume the role of Frank, the sugar
glider who was the antagonist of the film Big Buck Bunny.

The game has been made using free software, partly as a showcase of
what can be achieved with free software.


%prep
%setup -q -n yofrankie-%{version}
# This is (probably temporarily) disabled by upstream, but we may want
# to disable it even once upstream enables it again
#%patch0 -p1 -b .imgcompr
%patch1 -p1 -b .wrapper
install -pm 0644 %{SOURCE1} yofrankie-DVD-license.txt


%build
make %{_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}
install -d $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/games/* $RPM_BUILD_ROOT%{_bindir}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/yofrankie-bge.desktop


%files
%{_bindir}/yofrankie-bge
%{_datadir}/yofrankie-bge
%{_datadir}/icons/*/*/apps/yofrankie-bge.png
%{_datadir}/applications/*.desktop
%{_datadir}/fonts/truetype/yo_frankie.ttf
%attr(0644,-,-) %{_datadir}/man/man6/yofrankie-bge.6*
%doc yofrankie-DVD-license.txt


%changelog
* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1b-alt1_4.20100605svn
- converted from Fedora by srpmconvert script

