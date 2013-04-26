# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-fototoon
Version:        14
Release:        alt1_2
Summary:        An activity used to create cartoons

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4253
Source0:        http://mirrors.rit.edu/sugarlabs/activities/4253/fototoon-%{version}.xo

BuildRequires:  python-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.0
Source44: import.info

%description
Fototoon is a sugar activity used to create cartoons using photos 
or drawings. After selecting the images, the user can select globes 
and write text to tell a story.

%prep
%setup -q -n FotoToon.activity
rm po/aym.po
rm po/cpp.po
rm po/nah.po
rm po/son.po

%build
%{__python} ./setup.py build

%install
rm -rf ${buildroot}
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.eq.FotoToon

%files -f org.eq.FotoToon.lang
%doc TODO.txt
%{sugaractivitydir}/FotoToon.activity/

%changelog
* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 14-alt1_2
- initial fc import

