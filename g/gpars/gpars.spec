Name: gpars
Version: 1.2.1
Summary: Groovy Parallel Systems
License: ASL 2.0 and Public Domain
Url: http://gpars.codehaus.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: gpars = 1.2.1-4.fc23
Provides: mvn(org.codehaus.gpars:gpars) = 1.2.1
Provides: mvn(org.codehaus.gpars:gpars:pom:) = 1.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.groovy:groovy-all)
Requires: mvn(org.codehaus.jcsp:jcsp)
Requires: mvn(org.codehaus.jsr166-mirror:extra166y)
Requires: mvn(org.jboss.netty:netty:3)
Requires: mvn(org.multiverse:multiverse-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: gpars-1.2.1-4.fc23.cpio

%description
The GPars framework offers Java developers intuitive and safe ways to
handle Java or Groovy tasks concurrently. Leveraging the enormous
flexibility of the Groovy programming language and building on proven
Java technologies, we aim to make concurrent programming for
multi-core hardware intuitive, robust and enjoyable.

GPars is a multi-paradigm concurrency framework, offering several
mutually cooperating high-level concurrency abstractions, such as
Dataflow operators, Promises, CSP, Actors, Asynchronous Functions,
Agents and Parallel Collections.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

