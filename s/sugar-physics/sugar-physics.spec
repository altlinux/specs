# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-physics
Version:        10
Release:        alt1_1
Summary:        A physical world simulator and playground for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Physics
Source0:        http://download.sugarlabs.org/sources/honey/Physics/Physics-%{version}.tar.bz2

BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
Requires:       python-module-pybox2d
Requires:       python-module-elements
Requires:       python-module-olpcgames
BuildArch:      noarch
Source44: import.info

%description
You can add squares, circles, triangles, or draw your own shapes in
the Physics Activity, and see them come to life with forces (like gravity),
friction, and inertia.

%prep
%setup -q -n Physics-%{version}

# remove bundled libraries
rm -rf lib olpcgames

%build
python ./setup.py build

%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

# set appropriate permissions
chmod a+x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/physics.py
chmod a-x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/activity/{activity.info,activity-physics.svg}

# remove duplicated files
rm -f $RPM_BUILD_ROOT%{sugaractivitydir}/Physics.activity/DEVELOPING

%find_lang org.laptop.physics

%files -f org.laptop.physics.lang
%doc DEVELOPING COPYING
%{sugaractivitydir}/Physics.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_1
- new version; import from fc17 updates

