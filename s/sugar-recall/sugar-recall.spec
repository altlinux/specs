# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-recall
Version:        2
Release:        alt1_2
Summary:        A series of memory games

Group:          Graphical desktop/Sugar
License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Recall
Source0:        http://download.sugarlabs.org/sources/honey/Recall/Recall-%{version}.tar.bz2

BuildRequires:  sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Source44: import.info

%description
Recall is a series of memory games for sugar. The game becomes 
difficult as the user keeps on playing. This helps to increase 
the memorizing ability of children.

%prep
%setup -q -n Recall-%{version}

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%files 
%doc COPYING NEWS CREDITS
%{sugaractivitydir}/Recall.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2
- new version; import from fc17 updates

