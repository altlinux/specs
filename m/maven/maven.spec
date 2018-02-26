#Conflicts: maven2 < 2.1
#Provides: maven2-bootstrap = 3.0
#Provides:  maven2 = 3.0

# for /etc/mavenrc
%add_findreq_skiplist /usr/share/maven/bin/*

BuildRequires(pre): rpm-build-java
#BuildArch: noarch
Epoch: 0
Name: maven
Version: 3.0.4
Summary: Java project management and project comprehension tool
License: ASL 2.0 and MIT and BSD
Url: http://maven.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
#Requires: /bin/sh

# to fix builds, tmp?
#Requires: maven-clean-plugin maven-dependency-plugin

# bs'ed
Requires: aether
Requires: google-guice
Requires: guava
Requires: plexus-cipher
Requires: plexus-sec-dispatcher
Requires: sisu

Requires: animal-sniffer
Requires: apache-commons-cli
#Requires: apache-commons-parent
Requires: async-http-client
Requires: atinject
Requires: hamcrest
#Requires: java
Requires: maven-parent
Requires: maven-wagon

####Requires: maven3-common-poms
Requires: maven2-common-poms

#Requires: mojo-parent
#Requires: nekohtml
Requires: plexus-classworlds
Requires: plexus-containers-component-annotations
Requires: plexus-containers-container-default
Requires: plexus-interpolation
Requires: plexus-utils
#Requires: sonatype-oss-parent
#Requires: xbean
#Requires: xerces-j2

#BuildArch: noarch
Group: Development/Java
Release: alt0.3jpp
Source: maven-3.0.4-2.fc17.cpio

Source8: maven3bs-jarlist.txt
Source9: maven3bs-bootstrap-jarpack.tar

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

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

pushd $RPM_BUILD_ROOT
      rm -f `cat %{SOURCE8}`
      tar xf %{SOURCE9}
popd

#touch %buildroot/etc/mavenrc

rm %buildroot/usr/share/maven/repository-jni/JPP
ln -sf %_jnidir %buildroot/usr/share/maven/repository-jni/JPP

%files -f %name-list
#exclude 
#%config(noreplace,missingok) /etc/mavenrc

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.3jpp
- restored mvn

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.2jpp
- use system atinject

* Sat Mar 03 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.1jpp
- bootstrap maven3 package
