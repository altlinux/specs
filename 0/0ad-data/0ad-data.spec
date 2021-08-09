Name: 0ad-data
Epoch: 1
Version: 0.0.25
Release: alt1
BuildArch: noarch

Group: Games/Strategy
Summary: Data for 0ad: free, open-source realtime strategy game of ancient warfare
License: Various (all distributable)
Url: http://www.wildfiregames.com/0ad/
Source: 0ad-%version-alpha-unix-data.tar.xz

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
%setup -n 0ad-%version-alpha

%install
mkdir -p %buildroot%_datadir/0ad
mv binaries/data/* %buildroot%_datadir/0ad/

%files
%_datadir/0ad

%changelog
* Mon Aug 09 2021 Alexey Tourbin <at@altlinux.ru> 1:0.0.25-alt1
- 0.0.24b -> 0.0.25

* Tue Feb 23 2021 Alexey Tourbin <at@altlinux.ru> 1:0.0.24b-alt1
- 0.0.23b -> 0.0.24b
- removed Requires: 0ad, to avoid an unmet dependency on ppc64le

* Mon Dec 24 2018 Alexey Tourbin <at@altlinux.ru> 1:0.0.23b-alt1
- official re-release of Alpha 23

* Tue Jun 05 2018 Alexey Tourbin <at@altlinux.ru> 1:0.0.23-alt1
- 0.0.22 -> 0.0.23

* Sun Nov 05 2017 Alexey Tourbin <at@altlinux.ru> 1:0.0.22-alt1
- 0.0.21 -> 0.0.22

* Mon Jan 16 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.0.21-alt1
- Updated to 0.0.21.

* Mon Apr 04 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:0.0.20-alt1
- 0.0.20

* Mon Nov 30 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:0.0.19.alpha-alt1
- 0.0.19

* Sat Mar 14 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.18.alpha-alt1
- 0.0.18

* Wed Oct 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.17.alpha-alt1
- 0.0.17

* Tue May 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.16.alpha-alt1
- 0.0.16

* Wed Dec 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.15.alpha-alt1
- 0.0.15

* Fri Sep 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.14.alpha-alt1
- 0.0.14

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.13.alpha-alt1
- 0.0.13

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.12.alpha-alt1
- 0.0.12
- don't relay on bin package release

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.2
- Rebuilt

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.1
- Rebuilt

* Wed Sep 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.11.alpha-alt1
- build 0.0.11 alpha from scratch

