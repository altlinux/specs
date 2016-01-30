Name: plexus-resources
Version: 1.0
Summary: Plexus Resource Manager
License: MIT
Url: https://github.com/codehaus-plexus/plexus-resources
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-resources) = 1.0.alpha.7
Provides: mvn(org.codehaus.plexus:plexus-resources:pom:) = 1.0.alpha.7
Provides: plexus-resources = 1.0-0.19.a7.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt6jpp
Source: plexus-resources-1.0-0.19.a7.fc23.cpio

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.14.a7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a7jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.9.a7jpp7
- rebuild with maven-local

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.9.a7jpp7
- new fc release

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a7jpp7
- fixed plexus component generation

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.8.a7jpp7
- fc version

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a4.4jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a4.4jpp6
- rebuild w/new maven2; disabled tests

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a3.1jpp1.7
- converted from JPackage by jppimport script

