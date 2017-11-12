Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global shortname gossip

Name:             sonatype-gossip
Version:          1.7
Release:          alt1_17jpp8
Summary:          SLF4j Gossip Provider
License:          ASL 2.0
URL:              http://github.com/jdillon/gossip

# git clone git://github.com/jdillon/gossip.git
# cd gossip/ && git checkout gossip-1.7
# git archive --format=tar --prefix=gossip-1.7/ gossip-1.7 | xz > gossip-1.7.tar.xz
Source0:          %{shortname}-%{version}.tar.xz
Patch0:           %{shortname}-%{version}-use-java5-modello.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.mycila.maven-license-plugin:maven-license-plugin)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:    mvn(org.fusesource.jansi:jansi)
BuildRequires:    mvn(org.slf4j:slf4j-api)
BuildRequires:    mvn(org.sonatype.forge:forge-parent:pom:)
Source44: import.info

%description
Gossip is a plugin for SLF4j which has simple and flexible configuration.

%package bootstrap
Group: Development/Other
Summary:          Gossip Bootstrap

%description bootstrap
Contains just enough Gossip to allow the
internal org.sonatype.gossip.Log to function.

%package bootstrap-slf4j
Group: Development/Other
Summary:          Gossip Bootstrap SLF4j

%description bootstrap-slf4j
SLF4j bindings for Gossip Bootstrap.

%package core
Group: Development/Other
Summary:          Gossip Core

%description core
Gossip Core.

%package extra
Group: Development/Other
Summary:          Gossip Extra

%description extra
Gossip Extra.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%package slf4j
Group: Development/Other
Summary:          Gossip SLF4j

%description slf4j
Gossip SLF4j.

%package support
Group: Development/Other
Summary:          Gossip Support

%description support
Gossip Support, helper and utilities.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p1

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-gossip
%doc header.txt

%files bootstrap -f .mfiles-gossip-bootstrap
%doc README.md
%doc header.txt

%files bootstrap-slf4j -f .mfiles-gossip-bootstrap-slf4j
%files core -f .mfiles-gossip-core
%doc header.txt

%files extra -f .mfiles-gossip-extra

%files javadoc -f .mfiles-javadoc
%doc header.txt

%files slf4j -f .mfiles-gossip-slf4j
%files support -f .mfiles-gossip-support

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_16jpp8
- new jpp release

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
