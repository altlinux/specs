
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: clojure-spec-alpha
Version: 0.2.187
Summary: Spec is a Clojure library to describe the structure of data and functions
License: EPL-1.0
Url: https://github.com/clojure/spec.alpha/
Group: Development/Java
Release: alt0.1jpp

Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(org.clojure:spec.alpha) = 0.2.187
Provides: mvn(org.clojure:spec.alpha:pom:) = 0.2.187
Requires: java-headless
Requires: javapackages-filesystem

BuildArch: noarch
Source: clojure-spec-alpha-0.2.187-1.fc33.cpio


%description
Spec is a Clojure library to describe the structure of data and functions.
Specs can be used to validate data, conform (destructure) data, explain
invalid data, generate examples that conform to the specs, and automatically
use generative testing to test functions.

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
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.187-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

