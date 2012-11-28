# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name:           sugar-imageviewer
Version:        20
Release:        alt1_1
Summary:        Simple Image viewer for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Image_Viewer
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/ImageViewer/ImageViewer-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
BuildRequires: 	gettext

Requires:       sugar
Source44: import.info
Provides: sugar-imageviewer-activity = %version
Obsoletes: sugar-imageviewer-activity < %version
Conflicts: sugar-imageviewer-activity < %version


%description
The Image Viewer activity is a simple and fast image viewer tool for Sugar.
It has features one would expect of a standard image viewer, like zoom,
rotate, etc. 

%prep
%setup -q -n ImageViewer-%{version}

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.laptop.ImageViewerActivity


%files -f org.laptop.ImageViewerActivity.lang
%doc AUTHORS COPYING NEWS
%{sugaractivitydir}/ImageViewer.activity/


%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_1
- new version; import from fc17 release

