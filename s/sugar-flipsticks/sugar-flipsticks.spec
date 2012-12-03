# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-flipsticks
Version:        13
Release:        alt1_1
Summary:        A keyframe animation activity for Sugar
Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Flip_Sticks
Source0:        http://download.sugarlabs.org/activities/4044/flip_sticks-%{version}.xo
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
Source44: import.info

%description
Flipsticks is a keyframe animation activity that lets you pose and program
a stick figure to walk, run, rotate, twist, tumble and dance. You can save
your animations to the journal and will soon be able to share them via the
mesh. Flipsticks can be used to explore concepts in geometry, computer
programming and animation; it helps develop spatial and analytical thinking
skills. 

%prep
%setup -q -n FlipSticks.activity

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.worldwideworkshop.olpc.FlipSticks

%files -f org.worldwideworkshop.olpc.FlipSticks.lang
%doc AUTHORS COPYING NEWS TODO
%{sugaractivitydir}/FlipSticks.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 13-alt1_1
- new version; import from fc17 updates

