# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: sugar-turtleart
Version: 170
Release: alt1_1
Summary: Turtle Art activity for sugar

Group: Graphical desktop/Sugar
License: MIT
BuildArch: noarch
URL: http://sugarlabs.org/go/Activities/Turtle_Art
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/TurtleArt/TurtleArt-%{version}.tar.bz2

BuildRequires: sugar-toolkit
BuildRequires: gettext

Requires: sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-turtleart-activity < %version
Conflicts: sugar-turtleart-activity < %version

%description
The Turtle Art activity is an Logo-inspired graphical "turtle" that 
draws colorful  art based on Scratch-like snap-together visual 
programming elements. 

%prep
%setup -q -n TurtleArt-%{version}

%build
python ./setup.py build

%install
mkdir -p %{buildroot}%{sugaractivitydir}
python ./setup.py install --prefix=%{buildroot}%{_prefix}

%find_lang org.laptop.TurtleArtActivity

%files -f org.laptop.TurtleArtActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/TurtleArt.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 170-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 156-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 138-alt1_1
- new version; import from fc17 release

