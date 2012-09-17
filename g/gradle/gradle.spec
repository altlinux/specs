BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           gradle
Version:        0.9
Release:        alt1_0.4.20091127gitjpp7
Summary:        Groovy-based build system

Group:          Development/Java
License:        ASL 2.0
URL:            http://www.gradle.org/
# git clone git://github.com/gradle/gradle.git
# (cd gradle; git checkout 72ffff)
# tar czf gradle.tar.gz gradle --exclude .git
Source0:        gradle.tar.gz

BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
A flexible groovy-based build tool.


%package open-api
Summary:        Open API definition for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description open-api
Open API definition for gradle. It provides a simple versioned way to
interact with gradle. The open API jar is all that is needed to
develop/distribute a plugin. It provides some static functions that
dynamically load gradle from a directory you specify to do things like
create the UI or execute gradle commands directly (and I think some gradle
debugger information may soon be accessible there). All you need is the
gradle home directory and the open API jar.


%prep
%setup -q -n %{name}


%build
# Build Open API subpackage
pushd subprojects/gradle-open-api/src/main/groovy
find -name '*.java' |xargs javac
find -name '*.class' |xargs jar cf gradle-open-api.jar
popd

# ...and nothing else (matters)


%install
install -d $RPM_BUILD_ROOT%{_javadir}

# Open API
pushd subprojects/gradle-open-api/src/main/groovy
install -p -m644 gradle-open-api.jar \
        $RPM_BUILD_ROOT%{_javadir}/gradle-open-api-%{version}.jar
ln -s gradle-open-api-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/gradle-open-api.jar
popd


%files open-api
%{_javadir}/gradle-open-api-%{version}.jar
%{_javadir}/gradle-open-api.jar
%doc website/src/content/license.html


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_0.4.20091127gitjpp7
- new version

