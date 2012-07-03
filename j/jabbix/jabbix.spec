Name: jabbix
Version: 1.0.1
Release: alt2

Summary: The set of Java classes providing Zabbix monitoring system agent functionality
License: LGPLv3
Group: Development/Java
Url: http://altlinux.org/Jabbix
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar.gz

# Common dependencies
BuildPreReq: /proc rpm-build-java jpackage-utils
BuildRequires: java-devel >= 1.6.0

# Apache Ant is used for build
BuildRequires: ant

# Libraries
BuildRequires: jakarta-commons-cli log4j json

# GettextDoclet for Russian documentation
BuildRequires: gettext-doclet >= 1.0.1-alt2

BuildArch: noarch

# Libraries (runtime)
Requires: jakarta-commons-cli log4j json

%description
Jabbix library is a set of Java classes which can be used to add the
functionality of the Zabbix monitoring system agent to your programs.

%package javadoc
Summary: Documentation for %name
Group: Development/Documentation
Requires: java-common

%description javadoc
Jabbix library is a set of Java classes which can be used to add the
functionality of the Zabbix monitoring system agent to your programs.

This package provides Javadoc documentation for %name.

%package javadoc-ru
Summary: Russian documentation for %name
Group: Development/Documentation
Requires: java-common

%description javadoc-ru
Jabbix library is a set of Java classes which can be used to add the
functionality of the Zabbix monitoring system agent to your programs.

This package provides Russian Javadoc documentation for %name.

%package agent
Summary: Shell command to launch the JabbixAgent program
Group: Monitoring
Requires: java-common jabbix log4j jakarta-commons-cli json

%description agent
Jabbix library is a set of Java classes which can be used to add the
functionality of the Zabbix monitoring system agent to your programs.

This package provides a shell command to launch the JabbixAgent program.

%prep
%setup -n %name-%version

%build
%ant dist

OLD_LANG=$LANG
export LANG=en_US.UTF-8; %ant javadoc.en_US
export LANG=ru_RU.UTF-8; %ant javadoc.ru_RU
export LANG=$OLD_LANG

%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 dist/%name.jar %buildroot%_javadir/%name-%version.jar
ln -s %name-%version.jar %buildroot%_javadir/%name.jar

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pR doc/en_US %buildroot%_javadocdir/%name/
cp -pR doc/ru_RU %buildroot%_javadocdir/%name/

# agent
install -D -m 0755 cmd/jabbix %buildroot%_bindir/jabbix

%files
%doc README COPYING COPYING.LESSER
%_javadir/%name-%version.jar
%_javadir/%name.jar

%files javadoc
%doc %_javadocdir/%name/en_US

%files javadoc-ru
%doc %_javadocdir/%name/ru_RU

%files agent
%_bindir/jabbix

%changelog
* Wed Sep 08 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt2
- Build with java >= 1.6 as the implemented methods are marked with @Override.

* Tue Sep 07 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt1
- Add jabbix command shell script to launch JabbixAgent.

* Tue Aug 31 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Protocol description added to the documentation.

* Thu Aug 26 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux.

