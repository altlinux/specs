# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-fractionbounce
Version:        15
Release:        alt1_3
Summary:        A game which teaches fractions and estimations

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/FractionBounce
Source0:        http://download.sugarlabs.org/sources/honey/FractionBounce/FractionBounce-%{version}.tar.bz2

BuildRequires:  sugar-toolkit-gtk3 gettext python-devel
BuildArch:      noarch
Requires:       sugar >= 0.97.0
Source44: import.info

%description
FractionBounce is a game that prompts the player to nudge a bouncing 
ball to land at a point on the bottom of the screen that is an estimate 
of a given fraction. e.g. if 1/3 is displayed, then the ball must land 
1/3 the distance along the bottom.

%prep
%setup -q -n FractionBounce-%{version}

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}%{_prefix}

%find_lang org.sugarlabs.FractionBounceActivity

%files -f org.sugarlabs.FractionBounceActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/FractionBounce.activity/

%changelog
* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 15-alt1_3
- initial fc import

