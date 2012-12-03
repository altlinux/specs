# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: pkgconfig(gtk+-2.0) pkgconfig(x11) python-devel
# END SourceDeps(oneline)
Name:           sugar-stopwatch
Version:        15
Release:        alt1_1
Summary:        Simple stopwatch for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Stopwatch
Source0:        http://download.sugarlabs.org/activities/4263/stopwatch-%{version}.xo

BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
BuildArch:      noarch
Source44: import.info

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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- new version; import from fc17 updates

