# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-pukllanapac
Version:        11
Release:        alt1_1
Summary:        A sliding puzzle game

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Pukllanapac
Source0:        http://download.sugarlabs.org/sources/honey/Pukllanapac/Pukllanapac-%{version}.tar.bz2

BuildRequires:  python-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.96.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Pukllanapac is a sliding puzzle game; the objective is to rearrange 
tiles so that all of the circles (and semicircles) are composed 
of sectors of the same color. There are three different patterns: 
circles, triangles and hexagons. Drag tiles to swap their position; 
click on tiles to rotate them.

%prep
%setup -q -n Pukllanapac-%{version}

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.sugarlabs.PukllanapacActivity

%files -f org.sugarlabs.PukllanapacActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Pukllanapac.activity/

%changelog
* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 11-alt1_1
- new version; import from fc18

