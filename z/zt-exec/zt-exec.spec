Name:           zt-exec
Version:        1.12
Release:        alt2

Summary:        ZeroTurnaround Process Executor
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/zeroturnaround/zt-exec
VCS:            https://github.com/zeroturnaround/zt-exec

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(ch.qos.logback:logback-classic)

BuildArch:      noarch

%description
The project was created to merge similar functionality of projects at
ZeroTurnaround into a single codebase. It's designed to be powerful but still
simple to use. By using a single class ProcessExecutor the user gets the
functionality from both java.lang.ProcessBuilder and Apache Commons Exec.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# java-version-specific tests
rm src/test/java/org/zeroturnaround/exec/test/ProcessListenerThrowTest.java

%build
%mvn_build -- -Dmaven.compiler.release=17

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE.txt README.md

%changelog
* Mon Jun 29 2026 Evgeniy Serov <scala@altlinux.org> 1.12-alt2
- Fixed FTBFS: switch build to Java 17.

* Thu May 07 2026 Evgeniy Serov <scala@altlinux.org> 1.12-alt1
- Initial build for Sisyphus.
