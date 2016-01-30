Name: google-guice
Version: 4.0
Summary: Lightweight dependency injection framework for Java 5 and above
License: ASL 2.0
Url: https://github.com/google/guice
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: google-guice = 4.0-2.fc23
Provides: guice = 4.0-2.fc23
Provides: mvn(com.google.inject:guice) = 4.0
Provides: mvn(com.google.inject:guice::no_aop:) = 4.0
Provides: mvn(com.google.inject:guice:pom:) = 4.0
Provides: mvn(org.sonatype.sisu:sisu-guice) = 4.0
Provides: mvn(org.sonatype.sisu:sisu-guice::no_aop:) = 4.0
Provides: mvn(org.sonatype.sisu:sisu-guice:pom:) = 4.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(aopalliance:aopalliance)
Requires: mvn(com.google.guava:guava)
Requires: mvn(javax.inject:javax.inject)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: google-guice-4.0-2.fc23.cpio

%description
Put simply, Guice alleviates the need for factories and the use of new
in your Java code. Think of Guice's @Inject as the new new. You will
still need to write factories in some cases, but your code will not
depend directly on them. Your code will be easier to change, unit test
and reuse in other contexts.

Guice embraces Java's type safe nature, especially when it comes to
features introduced in Java 5 such as generics and annotations. You
might think of Guice as filling in missing features for core
Java. Ideally, the language itself would provide most of the same
features, but until such a language comes along, we have Guice.

Guice helps you design better APIs, and the Guice API itself sets a
good example. Guice is not a kitchen sink. We justify each feature
with at least three use cases. When in doubt, we leave it out. We
build general functionality which enables you to extend Guice rather
than adding every feature to the core framework.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt2_6jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_6jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

