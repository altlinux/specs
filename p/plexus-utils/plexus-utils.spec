Name: plexus-utils
Version: 3.0.22
Summary: Plexus Common Utilities
License: ASL 1.1 and ASL 2.0 and xpp and BSD and Public Domain
Url: https://github.com/codehaus-plexus/plexus-utils
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-utils) = 3.0.22
Provides: mvn(org.codehaus.plexus:plexus-utils:pom:) = 3.0.22
Provides: mvn(plexus:plexus-utils) = 3.0.22
Provides: mvn(plexus:plexus-utils:pom:) = 3.0.22
Provides: plexus-utils = 3.0.22-2.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-utils-3.0.22-2.fc23.cpio

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.22-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.14-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.9-alt1_5jpp7
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

