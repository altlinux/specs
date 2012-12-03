# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-measure
Version:	42
Release:        alt1_1
Summary:        Measure for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Measure
Source0:        http://download.sugarlabs.org/sources/honey/Measure/Measure-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit

Requires:       sugar
Source44: import.info


%description
A tool on the XO that allows kids to indulge in "learning by doing". 
It provides an interface for the kids to connect  sensors (light, heat,
magnetic field etc) and view their signal.


%prep
%setup -q -n Measure-%{version}


%build
%{__python} ./setup.py build


%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.laptop.MeasureActivity


%files -f org.laptop.MeasureActivity.lang
%doc README COPYING
%{sugaractivitydir}/Measure.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 42-alt1_1
- new version; import from fc17 updates

