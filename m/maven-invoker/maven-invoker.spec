Name: maven-invoker
Version: 2.2
Summary: Fires a maven build in a clean environment
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-invoker/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-invoker = 2.2-2.fc23
Provides: maven-shared-invoker = 2.2-2.fc23
Provides: mvn(org.apache.maven.shared:maven-invoker) = 2.2
Provides: mvn(org.apache.maven.shared:maven-invoker:pom:) = 2.2
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-invoker-2.2-2.fc23.cpio

%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_6jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_0jpp7
- hold obsoletes

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_6jpp7
- new version

