
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: clojure-core-specs-alpha
Version: 0.2.44
Summary: Clojure library containing specs to describe Clojure core macros and functions
License: EPL-1.0
Url: https://github.com/clojure/core.specs.alpha
Group: Development/Java
Release: alt0.1jpp

Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(org.clojure:core.specs.alpha) = 0.2.44
Provides: mvn(org.clojure:core.specs.alpha:pom:) = 0.2.44
Requires: java-headless
Requires: javapackages-filesystem

BuildArch: noarch
Source: clojure-core-specs-alpha-0.2.44-4.fc33.cpio


%description
Core.specs.alpha is a Clojure library containing specs to describe Clojure
core macros and functions.

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
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.44-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

