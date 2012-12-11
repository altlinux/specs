# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-infoslicer
Version:        15
Release:        alt1_3
Summary:        Downloader for articles from Wikipedia

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://sugarlabs.org/go/Activities/InfoSlicer
Source0:        http://download.sugarlabs.org/sources/honey/InfoSlicer/InfoSlicer-%{version}.tar.bz2
Patch0:         sugar-infoslicer-usejson.patch
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit

Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
InfoSlicer downloads articles from Wikipedia so that you can create new
documents by dragging and dropping content from the Wikipedia articles.
You can then publish the articles as a mini website.


%prep
%setup -q -n InfoSlicer-%{version}
%patch0 -p1 -b .json


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.sugarlabs.InfoSlicer


%files -f org.sugarlabs.InfoSlicer.lang
%doc COPYING NEWS README examples/
%{sugaractivitydir}/InfoSlicer.activity/


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_3
- new version; import from fc18

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- new version; import from fc17 updates

