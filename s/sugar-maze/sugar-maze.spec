# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-maze
Version:        22
Release:        alt1_1
Summary:        Maze for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Maze
Source0:        http://activities.sugarlabs.org/sugar/downloads/file/25982/maze-%{version}.xo
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  sugar-toolkit

Requires:       sugar
Requires:       python-module-olpcgames
Source44: import.info

%description
A simple maze game for the XO laptop. You can play by yourself or race
to solve it with your buddies. Up to 3 people can play on a single XO
laptop and lots more can play when shared over the network.

%prep
%setup -q -n Maze.activity
# remove olpcgames library
rm -rf olpcgames

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{buildroot}/%{_prefix}
find  %{buildroot}%{sugaractivitydir}Maze.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
mv player.py %{buildroot}%{sugaractivitydir}/Maze.activity/player.py

%find_lang vu.lux.olpc.Maze

%files -f vu.lux.olpc.Maze.lang
%doc COPYING
%{sugaractivitydir}/Maze.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 22-alt1_1
- new version; import from fc17 updates

