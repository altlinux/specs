# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-help
Version:        15
Release:        alt1_1
Summary:        Help and Dokumentation for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Help_(activity)
Source0:        http://download.sugarlabs.org/sources/honey/Help/Help-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
The Help activity provides a quick interface to help documentation on the XO.
It currently launches a browser and displays html documents describing how
to use the XO and the Sugar interface. 


%prep
%setup -q -n Help-%{version}

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
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 14-alt1_1
- new version; import from fc17 updates

