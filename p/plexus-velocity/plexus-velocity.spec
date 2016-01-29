Name: plexus-velocity
Version: 1.1.8
Summary: Plexus Velocity Component
License: ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-velocity
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-velocity) = 1.1.8
Provides: mvn(org.codehaus.plexus:plexus-velocity:pom:) = 1.1.8
Provides: plexus-velocity = 1.1.8-19.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(velocity:velocity)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: plexus-velocity-1.1.8-19.fc23.cpio

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_14jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_11jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_10jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_9jpp7
- fc version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt3_1jpp5
- explicit selection of java5 compiler

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt2_1jpp5
- fixed build with maven 2.0.7

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

