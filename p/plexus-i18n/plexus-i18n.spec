Name: plexus-i18n
Version: 1.0
Summary: Plexus I18N Component
License: ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-i18n
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-i18n) = 1.0.beta.10
Provides: mvn(org.codehaus.plexus:plexus-i18n:pom:) = 1.0.beta.10
Provides: plexus-i18n = 1.0-0.7.b10.4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt6jpp
Source: plexus-i18n-1.0-0.7.b10.4.fc23.cpio

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.b10.2.5jpp7
- rebuild with maven-local

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b10.2.5jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.5jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.2jpp7
- fc version

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp5
- new jpackage release

* Sun Nov 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp1.7
- build with maven2

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b6.5jpp1.7
- bootstrap build for maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.5jpp1.7
- updated to new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.4jpp1.7
- converted from JPackage by jppimport script

