# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-playgo
Version:        5
Release:        alt1_8
Summary:        Go for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/PlayGo
Source0:        PlayGo-%{version}.tar.bz2
Source1:        %{name}-checkout.sh
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  sugar-toolkit

Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
The PlayGo activity implements Go a strategic board game for two players. Go 
originated in ancient China, centuries before its earliest known references
in 5th century BC writing. It is mostly popular in East Asia but has nowadays
gained some popularity in the rest of the world as well. Go is noted for being
rich in strategic complexity despite its simple rules. 


%prep
%setup -q -n PlayGo-%{version}
rm -rf gnugo/gnugo
chmod -x infopanel.py


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.PlayGo


%files -f org.laptop.PlayGo.lang
%doc NEWS README TODO gnugo/COPYING
%{sugaractivitydir}/PlayGo.activity/


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_8
- new version; import from fc18

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_7
- new version; import from fc17 updates

