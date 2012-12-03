# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-calendario
Version:        4
Release:        alt1_2
Summary:        Agenda/Calendar activity for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3
URL:            http://wiki.sugarlabs.org/go/Activities/calendario
Source0:        http://yaderv.fedorapeople.org/sugar-activity/Calendario-activity-%{version}.tar.gz

BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
BuildArch:      noarch
Source44: import.info

%description
Calendario is a Sugar Activity for manage tasks in a calendar interface. 
This application helps the development of the organizational skill on the children.

%prep
%setup -q -n Calendario-activity-%{version}

%build

%install
%{__python} setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
%find_lang org.laptop.calendario

%files -f org.laptop.calendario.lang
%doc COPYING LICENSE README
%{sugaractivitydir}/Calendario.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2
- new version; import from fc17 updates

