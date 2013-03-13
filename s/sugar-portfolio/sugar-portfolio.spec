# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-portfolio
Version:        37
Release:        alt1_1
Summary:        A simple tool for generating slide show from starred Journal entries

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Portfolio
Source0:        http://download.sugarlabs.org/sources/honey/Portfolio/Portfolio-%{version}.tar.bz2

BuildRequires:  python-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.6
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Portfolio is a simple tool for generating a slide show from Journal 
entries that have been starred. The title, description, and preview 
image are used to auto-generate a slide. The slide show itself can be 
saved as an HTML document that can be shared.

%prep
%setup -q -n Portfolio-%{version}
rm po/son.po

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.sugarlabs.PortfolioActivity

%files -f org.sugarlabs.PortfolioActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Portfolio.activity/

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 37-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 28-alt1_1
- new version; import from fc17 updates

