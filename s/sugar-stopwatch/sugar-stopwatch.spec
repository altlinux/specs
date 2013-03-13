# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-stopwatch
Version:        18
Release:        alt1_1
Summary:        Simple stopwatch for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Stopwatch
Source0:        http://download.sugarlabs.org/activities/4263/stopwatch-%{version}.xo

BuildRequires: python-devel
BuildRequires: sugar-base
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar >= 0.98.0
BuildArch:      noarch
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
This activity provides multiple stopwatches to time events with. Provide a 
useful timer for races, velocity measurements, etc.  Be accessible to 
innumerate users. Help develop numeracy. Sharing of stopwatch sets, which 
anyone can manipulate. 

%prep
%setup -q -n StopWatch.activity


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.StopWatchActivity

%files -f org.laptop.StopWatchActivity.lang
#%doc AUTHORS COPYING NEWS
%{sugaractivitydir}/StopWatch.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 18-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- new version; import from fc17 updates

