Name: plexus-cli
Version: 1.6
Summary: Command Line Interface facilitator for Plexus
License: ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-cli
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-cli) = 1.6
Provides: mvn(org.codehaus.plexus:plexus-cli:pom:) = 1.6
Provides: plexus-cli = 0:1.6-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-cli-1.6-2.fc23.cpio

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_17jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_12jpp7
- fc update

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_5jpp6
- new version

* Thu Jan 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp6
- jpp 6 releases

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- converted from JPackage by jppimport script

