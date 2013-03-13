# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-flip
Version:        5
Release:        alt1_4
Summary:        Simple strategic game of flipping coins

Group:          Graphical desktop/Sugar
License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Flip
Source0:        http://download.sugarlabs.org/sources/honey/Flip/Flip-%{version}.tar.bz2

BuildRequires:  python-devel
BuildRequires:  sugar-base
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar >= 0.96.1

BuildArch:      noarch
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Flip is a simple strategic game where you have to flip coins until 
they are all heads up. Each time you win, the challenge gets more 
difficult. You can play flips with your friends over the net. 

%prep
%setup -q -n Flip-%{version}

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{sugaractivitydir}Flip.activity/setup.py

%find_lang org.sugarlabs.FlipActivity

%files -f org.sugarlabs.FlipActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Flip.activity/

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_4
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_2
- new version; import from fc17 updates

