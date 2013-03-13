# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-visualmatch
Version:        47
Release:        alt1_1
Summary:        A visual matching game

Group:          Graphical desktop/Sugar
# namingalert.py is licensed as LGPLv2+
# sprites.py is licensed under the MIT license
# other files are licensed as GPLv3+
License:        GPLv3+ and LGPLv2+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/VisualMatch
Source0:        http://download.sugarlabs.org/sources/honey/Visualmatch/VisualMatch-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	python-devel
BuildRequires:	sugar-toolkit-gtk3-devel
BuildArch:	noarch
Requires:	sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
The object is to find sets of three cards where each attributea..color,
shape, number of elements, and shadinga..either match on all three cards
or are different on all three cards. The current version doesn't yet
support sharing with multiple players or saving to the Journal, but it
can be played by a single player.


%prep
%setup -q -n VisualMatch-%{version}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
chmod 0644 $RPM_BUILD_ROOT/%{sugaractivitydir}/VisualMatch.activity/gencards.py

%find_lang org.sugarlabs.VisualMatchActivity


%files -f org.sugarlabs.VisualMatchActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/VisualMatch.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 47-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 38-alt1_1
- new version; import from fc17 updates

