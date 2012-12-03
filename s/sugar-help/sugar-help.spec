# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-help
Version:        14
Release:        alt1_1
Summary:        Help and Dokumentation for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Help_(activity)
Source0:        http://activities.sugarlabs.org/en-US/sugar/downloads/file/27487/help-%{version}.xo
BuildArch:      noarch

BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar
Source44: import.info


%description
The Help activity provides a quick interface to help documentation on the XO.
It currently launches a browser and displays html documents describing how
to use the XO and the Sugar interface. 


%prep
%setup -q -n Help.activity

chmod -x {NEWS,LICENSE,README,TODO,help/*.html,help/style.css}
chmod -x {activity/activity.info,activity/activity-help.svg,helpactivity.py}
sed -i 's/\r$//' {help/style.css,activity/activity.info}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}


%files
%doc NEWS LICENSE README TODO
%{sugaractivitydir}/Help.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 14-alt1_1
- new version; import from fc17 updates

