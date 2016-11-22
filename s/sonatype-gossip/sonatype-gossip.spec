Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global shortname gossip

Name:             sonatype-gossip
Version:          1.7
Release:          alt1_14jpp8
Summary:          SLF4j Gossip Provider
Group:            Development/Other
License:          ASL 2.0
URL:              http://github.com/jdillon/gossip

# git clone git://github.com/jdillon/gossip.git
# cd gossip/ && git checkout gossip-1.7
# git archive --format=tar --prefix=gossip-1.7/ gossip-1.7 | xz > gossip-1.7.tar.xz
Source0:          %{shortname}-%{version}.tar.xz
Patch0:           %{shortname}-%{version}-use-java5-modello.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-license-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    slf4j
BuildRequires:    modello
BuildRequires:    jansi
BuildRequires:    fusesource-pom
Source44: import.info

%description
Gossip is a plugin for SLF4j which has simple and flexible configuration.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p1

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md header.txt

%files javadoc -f .mfiles-javadoc
%doc header.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_14jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_13jpp8
- java8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_7jpp7
- new release

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_5jpp7
- new release

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_1jpp6
- fixed build

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build with maven3

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt2.git20090422
- rebuild with libebook-1.2.so.10

* Tue May 12 2009 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1.git20090422
- 0.32 git 20090422 version
- update BuildRequires
- removed libgnomeui and libgnomevfs deps, add libcanberra-gtk

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.31-alt2
- removed obsolete %%post{,in} scripts
- updated buildreqs

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.31-alt1
- 0.31
- rebuild with libgalago-0.5.2 (soname so.3)

* Sat Jul 12 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt3
- fix desktop file

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt2
- add Packager tag

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt1
- 0.28 -> 0.29

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt2
- Update Url
- add %%update_menus to %%post script
- add %%clean_menus to %%postun script

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt1
- 0.26 -> 0.28

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt2
- fix build with new intltool

* Tue Jun 19 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt1
- 0.17 -> 0.26
- buildreq and update build requires

* Wed Dec 27 2006 Igor Zubkov <icesik@altlinux.org> 0.17-alt1.1
- rebuild with new dbus

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.17-alt1
- Updated to 0.17
- Updated versioned dependencies
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12-alt1
- Release 0.12
- Patch0 is obsolete

* Fri Jun 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.2-alt1
- Release 0.11.2

* Tue Jun 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt2
- Patch0: port to libgalago 0.5, from GNOME bug 339333
- Rebuilt with libgalago 0.5

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt1
- Release 0.11.1

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11-alt1
- Release 0.11
- Enabled libnotify back
- Compressed ChangeLog

* Sun Mar 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- Release 0.10.2
- Buildreq

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- Release 0.10.1
- Disabled libnotify support until the API stabilizes

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10-alt1
- 0.10
- Buildreq
- Optional Galago support, enabled by default
- Removed Debian-style menu

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt1
- New upstream release
- Patch0 is obsolete

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt3
- Patch for new dbus from Fedora (thanks Rider) [Patch0]
- Requires dbus 0.34

* Sun Jan 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt2
- Added the common menu entry (bug #5909)

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt1
- New upstream release

* Sat Dec 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt3
- Added /usr/share/gossip directory to the file list

* Mon Oct 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt2
- Stricter installtime versioned dependencies copied from the buildtime
  dependencies, which are in turn copied from configure dependencies
  (bug #5393)

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt1
- Updated to the new upstream release
- Conditionally build with dbus

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.5-alt1
- New upstream release

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.4-alt1
- New upstream release

* Sat Feb 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.2-alt1
- New upstream release
- Run automake

* Fri Jan 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.1-alt1
- New upstream release

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6-alt1
- New upstream release

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.5-alt1
- New version

* Mon Jul 21 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt1
- Ported to ALT Linux
