# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-nutrition
Version:        7
Release:        alt1_1
Summary:        A collection of nutrition games

Group:          Graphical desktop/Sugar
License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Nutrition
Source0:        http://download.sugarlabs.org/sources/honey/Nutrition/Nutrition-%{version}.tar.bz2

BuildRequires:  gettext python-devel sugar-toolkit-gtk3
BuildArch:      noarch
Requires:       sugar >= 0.96.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Nutrition is a collection of nutrition games for sugar. There are 
four games related to nutrition. In all games the user is asked a 
question and provided with options. If he/she picks the correct 
answer a smiley face will appear. It educates the children about 
food and nutrition.

%prep
%setup -q -n Nutrition-%{version}

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.sugarlabs.NutritionActivity

%files -f org.sugarlabs.NutritionActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Nutrition.activity/

%changelog
* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 7-alt1_1
- new version; import from fc18

