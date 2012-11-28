# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name:		sugar-jukebox
Version:	23
Release:	alt1_2
Summary:	Media player activity for Sugar

Group:		Graphical desktop/Sugar
License:	GPLv2+
URL:		http://wiki.laptop.org/go/Jukebox
Source0:	http://download.sugarlabs.org/sources/sucrose/fructose/Jukebox/Jukebox-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:	sugar-toolkit
BuildArch:	noarch
Requires:	sugar
Source44: import.info
Provides: sugar-jukebox-activity = %version
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
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 23-alt1_2
- new version; import from fc17 release

