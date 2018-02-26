Epoch: 0
Name: google-guice
Version: 3.0
Summary: Lightweight dependency injection framework
License: ASL 2.0
Url: http://code.google.com/p/google-guice
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: netbeans-cvsclient
Requires: atinject
Requires: cglib
Requires: java

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: google-guice-3.0-0.6.rc2.fc18.cpio

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_1jpp6
- new version

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.RC2.1jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.RC2.1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.RC2.1jpp5
- converted from JPackage by jppimport script

