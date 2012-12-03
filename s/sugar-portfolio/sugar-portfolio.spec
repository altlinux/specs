# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-portfolio
Version:        28
Release:        alt1_1
Summary:        A simple tool for generating slide show from starred Journal entries

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Portfolio
Source0:        http://download.sugarlabs.org/sources/honey/Portfolio/Portfolio-%{version}.tar.bz2

BuildRequires:  sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Source44: import.info

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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 28-alt1_1
- new version; import from fc17 updates

