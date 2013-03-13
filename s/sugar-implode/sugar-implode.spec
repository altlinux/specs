# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%global shortname implode

Name:           sugar-%{shortname}
Version:        15
Release:        alt1_1
Summary:        Implode for Sugar
Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Implode
Source0:        http://download.sugarlabs.org/sources/honey/Implode/Implode-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Implode is a logic game based on the "falling block" model of Tetris. The game
starts with a grid partially filled with blocks. The player makes a move by 
removing adjacent blocks of the same color in groups of three or more. When 
blocks are removed, higher blocks fall to fill their space, and when a column 
is cleared, the blocks on either side close to fill the gap. The object of the
game is to remove all the blocks. Since the patterns of blocks above changes
when lower blocks are removed, the player must carefully decide what order
in which to remove the blocks so that there are no isolated blocks left at
the end of the game. The levels are generated in such a way that there is
always a sequence of removals that clears the board. 

%prep
%setup -q -n Implode-%{version}

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
#executables
find  %{buildroot}%{sugaractivitydir}Implode.activity/*.py -type f | xargs chmod a+x
for file in %{buildroot}%{sugaractivitydir}Implode.activity/{board,boardgen,color,gridwidget,implodeactivity,implodegame,setup}.py; do
   chmod a+x $file
done
%find_lang com.jotaro.ImplodeActivity

%files -f com.jotaro.ImplodeActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Implode.activity/

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 12-alt1_1
- new version; import from fc17 updates

