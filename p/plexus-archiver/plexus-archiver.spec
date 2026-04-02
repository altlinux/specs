Name:           plexus-archiver
Version:        4.11.0
Release:        alt2

Summary:        Plexus Archiver Component
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-archiver/
VCS:            https://github.com/codehaus-plexus/plexus-archiver

Source0:        %name-%version.tar

Patch0:         0001-Removed-unsupported-zstd.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)

BuildArch:      noarch

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_dep :zstd-jni
rm -r src/main/java/org/codehaus/plexus/archiver/zstd
rm src/main/java/org/codehaus/plexus/archiver/tar/ZstdTarFile.java
rm src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarZstdFileResourceCollection.java
rm src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTZstdFileResourceCollection.java

# Tests
rm -r src/test/java/org/codehaus/plexus/archiver/zstd
rm src/test/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiverTest.java
rm src/test/java/org/codehaus/plexus/archiver/manager/ArchiverManagerTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md LICENSE

%changelog
* Thu Mar 19 2026 Evgeniy Serov <scala@altlinux.org> 4.11.0-alt2
- Cosmetic fixes.
- Fix build with new guava.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 4.11.0-alt1
- Updated to 4.11.0 (without zstd-jni).

* Tue Sep 09 2025 Ivan Khanas <xeno@altlinux.org> 0:4.2.7-alt2
- Fix FTBFS: plexus-io API incompatibility.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:4.2.7-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.4-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.4-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.2-alt1_3jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.1-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:4.1.0-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_3jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_1jpp8
- java update

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_5jpp8
- unbootstrap build

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.3.gitdc873a4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.2.gitdc873a4jpp8
- new version

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

