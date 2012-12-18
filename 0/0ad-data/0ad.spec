Name: 0ad-data
Epoch: 1
Version: 0.0.12.alpha
Release: alt1
BuildArch: noarch

Group: Games/Strategy
Summary: Data for 0ad: free, open-source realtime strategy game of ancient warfare
License: Various (all distributable)
Url: http://www.wildfiregames.com/0ad/
Requires: 0ad = %epoch:%version
Source: %name-%version.tar

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or
rewrite the history of Western civilizations, focusing on the years
between 500 B.C. and 500 A.D. The project is highly ambitious, involving
state-of-the-art 3D graphics, detailed artwork, sound, and a flexible
and powerful custom-built game engine.

The game has been in development by Wildfire Games (WFG), a group of
volunteer, hobbyist game developers, since 2001. The code and data are
available under the GPL license, and the art, sound and documentation
are available under CC-BY-SA. In short, we consider 0 A.D. an an
educational celebration of game development and ancient history.

%prep
%setup

%build

%install
mkdir -p %buildroot/%_datadir/0ad
mv binaries/data/* %buildroot/%_datadir/0ad

%files
%_datadir/0ad

%changelog
* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.12.alpha-alt1
- 0.0.12
- don't relay on bin package release

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.2
- Rebuilt

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.1
- Rebuilt

* Wed Sep 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.11.alpha-alt1
- build 0.0.11 alpha from scratch

