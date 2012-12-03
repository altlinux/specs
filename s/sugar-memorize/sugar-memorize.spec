# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-memorize
Version:        41
Release:        alt1_1
Summary:        Memorize for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Memorize
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/Memorize/Memorize-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  sugar-toolkit

Requires:       sugar
Requires:       python-module-olpcsound
Requires:       libxml2-python
Source44: import.info

%description
The game memorize is about finding matching pairs. A pair can consist of any
multimedia object. At the moment these are images, sounds and text but this
could be extended to animations or movie snippets as well. Which pairs do 
match is up to the creator of the game. Memorize is actually more than just
a predefined game you can play, it allows you to create new games yourself
as well.

%prep
%setup -q -n Memorize-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.Memorize


%files -f org.laptop.Memorize.lang
%doc AUTHORS COPYING NEWS
%{sugaractivitydir}/Memorize.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 41-alt1_1
- new version; import from fc17 updates

