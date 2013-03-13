# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: sugar-chat
Version: 78
Release: alt1_1
Summary: Chat client for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Chat
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Chat/Chat-%{version}.tar.bz2
 
BuildRequires: sugar-toolkit
BuildRequires: gettext

Requires: sugar
Requires: telepathy-mission-control

BuildArch: noarch
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-chat-activity < %version
Conflicts: sugar-chat-activity < %version

%description
The chat activity provides a chat client for the Sugar interface.

%prep
%setup -q -n Chat-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.Chat


%files -f org.laptop.Chat.lang
%doc NEWS
%{sugaractivitydir}/Chat.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 78-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 77-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 76-alt1_1
- new version; import from fc17 release

