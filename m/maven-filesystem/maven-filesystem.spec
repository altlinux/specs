BuildRequires(pre): rpm-macros-java
Name: maven-filesystem
Version: 0.01
Summary: Maven 3 system repository architecture-dependent symlinks.
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
Group: Development/Java
Release: alt2.1
BuildArch: noarch

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

This is auxiliary package for Maven 3 system repository 
architecture-dependent symlinks.

%prep

%build

%install
mkdir -p %buildroot/usr/share/maven/repository-jni/
ln -sf %_jnidir %buildroot/usr/share/maven/repository-jni/JPP

%files
/usr/share/maven/repository-jni/JPP

%changelog
* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.01-alt2.1
- (NMU) Rebuild with rpm-4.0.4-alt100.93 for previously missed deps
  (maven-filesystem on /usr/lib/java).

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- rebuild with new _jnidir location

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build
