Name: jcsp
Version: 1.1
Summary: Communicating Sequential Processes for Java (JCSP)
License: LGPLv2+
Url: https://xircles.codehaus.org/projects/jcsp
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jcsp = 1.1-0.4.rc5.fc23
Provides: mvn(org.codehaus.jcsp:jcsp) = 1.1.rc5
Provides: mvn(org.codehaus.jcsp:jcsp:pom:) = 1.1.rc5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:org.osgi.core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jcsp-1.1-0.4.rc5.fc23.cpio

%description
JCSP (Communication Sequential Processes for Java) is a
library providing a concurrency model that is a combination
of ideas from Hoare's CSP and Milner's pi-calculus.

Communicating Sequential Processes (CSP) is a mathematical
theory for specifying and verifying complex patterns of
behavior arising from interactions between concurrent
objects.

JCSP provides a base range of CSP primitives plus a rich set of
extensions. Also included is a package providing CSP process
wrappers giving a channel interface to all Java AWT widgets
and graphics operations.  It is extensively (java/documented)
and includes much teaching.

JCSP is an alternative concurrency model to the threads and
mechanisms built into Java. It is also compatible with
it since it is implemented on top of it.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

