# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:		sugar-jukebox
Version:	29
Release:	alt1_1
Summary:	Media player activity for Sugar

Group:		Graphical desktop/Sugar
License:	GPLv2+
URL:		http://wiki.laptop.org/go/Jukebox
Source0:	http://download.sugarlabs.org/sources/sucrose/fructose/Jukebox/Jukebox-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer1.0-devel
BuildRequires:	gst-plugins1.0-devel
BuildRequires:	python-devel
BuildRequires:	sugar-toolkit-gtk3-devel
BuildArch:	noarch
Requires:	sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-jukebox-activity < %version
Conflicts: sugar-jukebox-activity < %version

%description
The jukebox activity is an audio/video player that will play
different kind of files bases on the installed gstreamer plugins.


%prep
%setup -q -n Jukebox-%{version}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.sugar.Jukebox


%files -f org.laptop.sugar.Jukebox.lang
%doc AUTHORS COPYING NEWS MANIFEST TODO
%{sugaractivitydir}/Jukebox.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 29-alt1_1
- update from fc18 release

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 23-alt1_2
- new version; import from fc17 release

