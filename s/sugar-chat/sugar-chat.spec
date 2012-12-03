# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name: sugar-chat
Version: 77
Release: alt1_1
Summary: Chat client for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Chat
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Chat/Chat-%{version}.tar.bz2
 
BuildRequires: sugar-toolkit
BuildRequires: gettext

Requires: sugar
Requires: python-module-telepathy
Requires: telepathy-mission-control

BuildArch: noarch
Source44: import.info
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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 77-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 76-alt1_1
- new version; import from fc17 release

