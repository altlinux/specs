Name:    ucanaccess
Version: 4.0.4
Release: alt1
Summary: Java JDBC driver to read/write Microsoft Access databases (.accdb, .mdb)

Group:   Development/Java
License: Apache 2.0
URL:     http://ucanaccess.sourceforge.net
Source0: UCanAccess-%version-src.zip
Patch:   ucanaccess-disable-check-java-api.patch

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven-local
BuildRequires:  animal-sniffer
BuildRequires:  hsqldb
BuildRequires:  jackcess
BuildRequires:  mockito
BuildRequires:  unzip

BuildArch: noarch
Requires: java >= 1.6.0

%description
An open-source Java JDBC driver implementation that allows Java
developers and JDBC client programs (e.g., DBeaver, NetBeans, SQLeo,
OpenOffice Base, LibreOffice Base, Squirrel SQL) to read/write Microsoft
Access databases.

Supported Access formats: 2000, 2002/2003, 2007, 2010/2013/2016
databases. (Access 97 format supported for read-only.)

%package javadoc
Summary:  Javadoc for %name
Group:    Documentation
Requires: jpackage-utils

Requires: jpackage-utils
Requires: %name = %EVR

%description javadoc
Javadoc for %name.

%prep
%setup -n UCanAccess-%version-src
%patch -p2
%mvn_file :%name %name

%build
%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc NOTICE.txt README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus.
