Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name guice

Name:           google-%{short_name}
Version:        3.0
Release:        alt1_0.7.rc2jpp7
Summary:        Lightweight dependency injection framework


Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/%{name}

# svn export -r1219 http://google-guice.googlecode.com/svn/trunk/ guice-2.0-1219
# tar caf guice-2.0-1219.tar.xz guice-2.0-1219
Source0:        https://%{name}.googlecode.com/files/%{short_name}-%{version}-rc2-src.zip

# patch from http://github.com/sonatype/sisu-guice
# excluded changes to pom.xml files that changed groupIds
# needed for maven 3 to work
Patch0:         sisu-custom.patch

# bz#704222
Patch1:         0001-Remove-test-and-missing-deps-from-core-pom.xml.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  jarjar => 1.0
BuildRequires:  cglib
BuildRequires:  aqute-bnd
BuildRequires:  objectweb-asm
BuildRequires:  junit
BuildRequires:  atinject
BuildRequires:  zip
BuildRequires:  slf4j
BuildRequires:  jpackage-utils

Requires:       cglib
Requires:       atinject

# extreme hack to fix maven buildroots
Provides:       netbeans-cvsclient = 7.0.0-1
Source44: import.info

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

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-rc2-src
%patch0
%patch1 -p1

# remove parent definition referencing google-parent
sed -ie '/<parent>/,/<\/parent/ {d}' pom.xml

# remove bundled libraries
find . -name '*.class' -delete
find . -name '*.bar' -delete
# we'll repack munge.jar so don't delete it just yet
find . -name '*.jar' -not -name 'munge.jar' -delete

# re-create symlinks
pushd lib/build
build-jar-repository -s -p . aqute-bnd cglib slf4j \
                     jarjar junit objectweb-asm \

mv aqute-bnd*.jar bnd-0.0.384.jar
mv cglib*.jar cglib-2.2.1-snapshot.jar
mv jarjar*.jar jarjar-snapshot.jar
mv objectweb-asmasm-all.jar asm-3.1.jar

popd
ln -sf `build-classpath atinject` lib/javax.inject.jar

# there is munge.jar defining ant task it's a mixture of files, but
# there are sources in jar so we re-compile the jar to verify it
# builds
mkdir munge-repack
unzip lib/build/munge.jar -d munge-repack
rm lib/build/munge.jar

pushd munge-repack
rm *.class
javac -cp `build-classpath ant junit` *.java
zip -r ../lib/build/munge.jar .
popd

rm -rf munge-repack
#end munge.jar repack

%build
# create no-aop build environment
ant no_aop

pushd build/no_aop/
# javadoc fails without this directory
mkdir -p servlet/lib/build

ant -Dversion=%{version} jar
popd

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
pushd build/no_aop
install -pm 644 build/dist/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-parent.pom

install -pm 644 core/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
# provide sisu group/artifact (should be just mavenized google-guice
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.sonatype.sisu:sisu-guice"
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r javadoc/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc COPYING
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%files javadoc
%doc COPYING
%doc %{_javadocdir}/%{name}



%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_0.7.rc2jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_0.6.rc2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

