Name: plexus-containers
Version: 1.6
Summary: Containers for Plexus
License: ASL 2.0 and MIT
Url: https://github.com/codehaus-plexus/plexus-containers
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-containers:pom:) = 1.6
Provides: plexus-containers = 1.6-4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-containers-1.6-4.fc23.cpio

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_13jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_11jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_6jpp7
- more symlinks

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt7_6jpp7
- added another compat symlink

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt6_6jpp7
- added compat symlink

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt5_6jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt4_6jpp7
- fixed build

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt3_6jpp7
- fixed deps

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_6jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_5jpp7
- applied repocop patches

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_5jpp7
- fc build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.1.a34.5jpp6
- fixed build

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.1.a34.5jpp6
- fixed build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a34.5jpp6
- fixed build

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a34.5jpp6
- new release a34

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a32.3jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a30.1jpp5
- converted from JPackage by jppimport script

