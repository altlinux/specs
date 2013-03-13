# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:          sugar-imageviewer
Version:       54
Release:       alt1_1
Summary:       Simple Image viewer for Sugar

Group:         Graphical desktop/Sugar
License:       GPLv2+
URL:           http://wiki.laptop.org/go/Image_Viewer
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/ImageViewer/ImageViewer-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python-devel
BuildRequires: sugar-base
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar >= 0.96.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
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
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 54-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 21-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_1
- new version; import from fc17 release

