# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 libICE-devel libSM-devel libalsa-devel libgtk+3-gir-devel pkgconfig(cairo) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(ice) python-devel
# END SourceDeps(oneline)
Name: sugar-turtleart
Version: 156
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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 156-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 138-alt1_1
- new version; import from fc17 release

