# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-countries
Version:        33
Release:        alt1_2
Summary:        A game to play with identifying countries

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4528
Source0:        http://activities.sugarlabs.org/downloads/file/27834/countries-%{version}.xo

BuildRequires:  sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Source44: import.info

%description
Countries is a game where players have to type in a country for
each letter of the alphabet. Successes are rewarded with the
display of the country's flag. The activity consists of the
English names of 212 countries.

%prep
%setup -q -n Countries.activity
chmod +x Countries.py
sed -i 's/\r//' Countries.py

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%files 
%{sugaractivitydir}/Countries.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 33-alt1_2
- new version; import from fc17 updates

