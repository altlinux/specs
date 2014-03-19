Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/perl pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-dialogs
Version:        1.8.0
Release:        alt1_1
Summary:        Displays dialog boxes from shell scripts
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz
#Source0: http://raveit65.fedorapeople.org/Mate/git-upstream/%{name}-%{version}.git%{_internal_version}.tar.xz

Source0:        http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildRequires:  mate-common
BuildRequires:  libnotify-devel
Source44: import.info

%description
Displays dialog boxes from shell scripts.

%prep
%setup -q

%build
%configure --disable-scrollkeeper \
           --with-gtk=2.0

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/matedialog
%{_mandir}/man1/*
%{_datadir}/matedialog
%{_datadir}/help/*/matedialog

%changelog
* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_3
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_2
- new fc release

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- dropped gdialog compat script (conflicts with real gdialog)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

