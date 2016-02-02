Name: scala
Version: 2.10.4
Summary: A hybrid functional/object-oriented language for the JVM
License: BSD
Url: http://www.scala-lang.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.scala-lang:scala-compiler) = 2.10.4
Provides: mvn(org.scala-lang:scala-compiler:pom:) = 2.10.4
Provides: mvn(org.scala-lang:scala-library) = 2.10.4
Provides: mvn(org.scala-lang:scala-library:pom:) = 2.10.4
Provides: mvn(org.scala-lang:scala-reflect) = 2.10.4
Provides: mvn(org.scala-lang:scala-reflect:pom:) = 2.10.4
Provides: mvn(org.scala-lang:scala-swing) = 2.10.4
Provides: mvn(org.scala-lang:scala-swing:pom:) = 2.10.4
Provides: mvn(org.scala-lang:scalap) = 2.10.4
Provides: mvn(org.scala-lang:scalap:pom:) = 2.10.4
Provides: scala = 2.10.4-8.fc23
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: /usr/bin/env
Requires: /usr/share/java/jansi/jansi.jar
Requires: /usr/share/java/jline/jline.jar
Requires: jansi
Requires: java-headless
Requires: java-headless
Requires: jline
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: scala-2.10.4-8.fc23.cpio

%description
Scala is a general purpose programming language designed to express common
programming patterns in a concise, elegant, and type-safe way. It smoothly
integrates features of object-oriented and functional languages. It is also
fully interoperable with Java.

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

%post
touch --no-create /usr/share/mime/packages &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
update-mime-database /usr/share/mime &> /dev/null || :
fi


%files -f %name-list

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

