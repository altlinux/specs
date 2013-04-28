# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-hello-world
Version:        6
Release:        alt1_4
Summary:        Activity to print "Hello world" on the screen

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4418
Source0:        http://mirrors.rit.edu/sugarlabs/activities/4418/helloworld-%{version}.xo

BuildRequires:  python-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.0
Source44: import.info

%description
Hello World is an activity for sugar and will print out 
"Hello world" on the screen. This is the simplest activity 
possible for sugar. This activity can be used as a starting 
point to examine the activity code and create your own sugar 
activity.

%prep
%setup -q -n HelloWorld.activity

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%files
%doc COPYING
%{sugaractivitydir}/HelloWorld.activity/

%changelog
* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 6-alt1_4
- initial fc import

