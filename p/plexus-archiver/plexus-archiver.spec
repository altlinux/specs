Name: plexus-archiver
Version: 3.0.1
Summary: Plexus Archiver Component
License: ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-archiver
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-archiver) = 3.0.1.SNAPSHOT
Provides: mvn(org.codehaus.plexus:plexus-archiver:pom:) = 3.0.1.SNAPSHOT
Provides: plexus-archiver = 0:3.0.1-0.2.gitdc873a4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(org.codehaus.plexus:plexus-io)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.xerial.snappy:snappy-java)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-archiver-3.0.1-0.2.gitdc873a4.fc23.cpio

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_3jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

