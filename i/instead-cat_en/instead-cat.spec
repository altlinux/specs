Name:		instead-cat_en
Version:	1.2
Release:	alt1
Group:		Games/Adventure
Summary:	The return of the quantum cat -- INSTEAD game (english)
License:	Distributable
Source:		http://instead-games.googlecode.com/files/%name-%version.zip
Packager:	Fr. Br. George <george@altlinux.ru>

BuildArch:	noarch
Requires:	instead

%define		instead %_datadir/instead/games
# Automatically added by buildreq on Mon Jan 04 2010
BuildRequires: unzip

%description
The return of the quantum cat -- INSTEAD game

Outside my cabin the snow is white again. The wood crackles in the fireplace just like that day... It's the third winter already.
Two winters have passed, but the events I want to tell about are in front of my eyes as if it was yesterday...

I've been working as a forest warden over ten years. Over ten years I lived in my cabin in the woods, gathering poachers' traps and going to a nearby town once in a week or two... After a Sunday service in the local church I went to a shop to buy the stuff I needed: shotgun ammunition, groats, bread, medicaments...

I used to be a quite good IT specialist... But that doesn't matter anymore... I hadn't seen a computer screen for a decade and didn't regret it.

Now I understand that the root of those events lies as far as the early thirties... But I'd better tell everything step by step...

%prep
%setup -n cat_en

%build

%install
mkdir -p %buildroot%instead
cp -a . %buildroot%instead/cat_en

%files
%instead/cat_en

%changelog
* Sun Mar 21 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch

