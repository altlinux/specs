# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-view-slides
Version:        8
Release:        alt1_8
Summary:        Image serie viewer for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/View_Slides
Source0:        http://download.sugarlabs.org/sources/honey/ViewSlides/ViewSlides-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires:       sugar
Requires:       python-module-pygame
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
The View Slides activity is meant to allow the XO laptop to read
view the contents of a Zip file containing images named sequentially.
Project Gutenberg has a few books as raw scanned images, and this can
be a useful format for picture books, comic books, magazine articles,
photo essays, etc.

The interface to View Slides is similar to the core Read activity,
which should not be surprising as the toolbar code was adapted from
Read's toolbar. You can use the up and down arrows or the game
controller to move from page to page.


%prep
%setup -q -n ViewSlides-%{version}
chmod +x xopower.py

%build
%{__python} setup.py build


%install
%{__python} setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.ViewSlidesActivity


%files -f org.laptop.ViewSlidesActivity.lang
%doc NEWS
%{sugaractivitydir}/ViewSlides.activity/


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_8
- new version; import from fc18

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_7
- new version; import from fc17 updates

