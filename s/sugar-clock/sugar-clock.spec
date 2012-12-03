# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-clock
Version:        8
Release:        alt1_1
Summary:        Clock activity for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Clock
Source0:        http://download.sugarlabs.org/sources/honey/Clock/Clock-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  sugar-toolkit

Requires:       sugar
Source44: import.info


%description
This activity displays time in analog, digital, and "natural" forms.
The "natural" form will be an image of a sun or moon arcing across
the sky, rising and setting as the day progresses. This is more than
a simple clock; the user will be able to grab any element and readjust
it, which will update each of the other elements. In this manner,
hopefully the children can explore and understand different methods of
telling time. 


%prep
%setup -q -n Clock-%{version}
#sed -i 's/\r$//' {icons/*,activity/activity-clock.svg,misc/activity-clock.svg}
#chmod -x {icons/*,activity/activity-clock.svg,misc/activity-clock.svg}
#chmod +x {test_timewriter/*.py,speaker.py,timewriter.py,pgettext.py}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang tv.alterna.Clock


%files -f tv.alterna.Clock.lang
%doc NEWS README
%{sugaractivitydir}/Clock.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_1
- new version; import from fc17 updates

