# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-connect
Version:        22
Release:        alt1_10
Summary:        Connect for Sugar
Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Connect
Source0:        Connect-%{version}.tar.bz2
Source1:        %{name}-checkout.sh
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  sugar-toolkit
Requires:       sugar
Source44: import.info

%description
The Connect activity implements the game of Connect-4 as a two-player game.
Additional participants can watch the game, and will have a chance to play
the winner of the current game.  

%prep
%setup -q -n Connect-%{version}

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.Connect

%files -f org.laptop.Connect.lang
%doc AUTHORS COPYING NEWS
%{sugaractivitydir}/Connect.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 22-alt1_10
- new version; import from fc17 updates

