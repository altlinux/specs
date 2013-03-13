# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-distance
Version:        34
Release:        alt1_1
Summary:        Distance measurement for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Distance
Source0:        http://mirrors.ibiblio.org/pub/mirrors/sugar/activities/4264/distance-%{version}.xo

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar >= 0.97.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Distance (aka Acoustic Tape Measure) determines the physical distance 
between two XOs by measuring how long it takes sound pulses to travel 
between them. 

%prep
%setup -q -n Distance.activity


%build
python ./setup.py build


%install
mkdir -p %{buildroot}%{sugaractivitydir}
./setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot}%{sugaractivitydir}Distance.activity/arange.py -type f -name \* -exec chmod 644 {} \;

%find_lang org.laptop.AcousticMeasure

%files -f org.laptop.AcousticMeasure.lang
%doc NEWS
%{sugaractivitydir}/Distance.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 34-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 31-alt1_1
- new version; import from fc17 updates

