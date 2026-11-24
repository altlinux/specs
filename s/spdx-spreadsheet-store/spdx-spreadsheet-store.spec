%define _unpackaged_files_terminate_build 1

Name: spdx-spreadsheet-store
Version: 2.0.4
Release: alt1
Summary: SPDX document storage in spreadsheet formats
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-spreadsheet-store
VCS: https://github.com/spdx/spdx-java-spreadsheet-store.git
Source0: %{name}-%{version}.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: fonts-ttf-dejavu
BuildRequires: mvn(org.spdx:java-spdx-library) = 2.0.5
BuildRequires: mvn(com.opencsv:opencsv) = 5.12.0
BuildRequires: mvn(org.apache.poi:poi) = 6.0.0
BuildRequires: mvn(org.apache.poi:poi-ooxml) = 6.0.0
BuildRequires: mvn(junit:junit) = 4.13.2

BuildArch: noarch

%description
SPDX Spreadsheet Store reads and writes SPDX documents in XLS and XLSX
spreadsheet formats.

%prep
%setup -q
%pom_change_dep org.spdx:java-spdx-library:2.0.4 org.spdx:java-spdx-library:2.0.5
%pom_change_dep org.apache.poi:poi:5.5.1 org.apache.poi:poi:6.0.0
%pom_change_dep org.apache.poi:poi-ooxml:5.4.1 org.apache.poi:poi-ooxml:6.0.0
# Publishing and SBOM plugins do not contribute to the packaged library.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.4-alt1
- Package SPDX Spreadsheet Store for Sisyphus.
