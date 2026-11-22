%define _unpackaged_files_terminate_build 1

Name: jackson3-dataformats-binary
Version: 3.3.0
Release: alt1

Summary: Jackson 3 binary data format backends
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-dataformats-binary
VCS: https://github.com/FasterXML/jackson-dataformats-binary.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.amazon.ion:ion-java)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(com.squareup:protoparser)
BuildRequires: mvn(org.apache.avro:avro)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

BuildArch: noarch

%description
Parent POM for the Jackson 3 binary data format modules.

%package -n jackson3-dataformat-cbor
Group: Development/Java
Summary: Jackson 3 backend for Concise Binary Object Representation (CBOR)

%description -n jackson3-dataformat-cbor
Read and write Concise Binary Object Representation (CBOR) data using Jackson 3.

%package -n jackson3-dataformat-smile
Group: Development/Java
Summary: Jackson 3 backend for Smile binary JSON

%description -n jackson3-dataformat-smile
Read and write Smile binary JSON data using Jackson 3.

%package -n jackson3-dataformat-avro
Group: Development/Java
Summary: Jackson 3 backend for Apache Avro

%description -n jackson3-dataformat-avro
Read and write Apache Avro data using Jackson 3.

%package -n jackson3-dataformat-protobuf
Group: Development/Java
Summary: Jackson 3 backend for Protocol Buffers

%description -n jackson3-dataformat-protobuf
Read and write Protocol Buffers data using Jackson 3.

%package -n jackson3-dataformat-ion
Group: Development/Java
Summary: Jackson 3 backend for Amazon Ion

%description -n jackson3-dataformat-ion
Read and write Amazon Ion data using Jackson 3.

%javadoc_package

%prep
%setup

%pom_change_dep org.hamcrest:hamcrest-all org.hamcrest:hamcrest ion
# The system AssertJ JAR derives its automatic module name from its filename.
sed -i 's/requires org\.assertj\.core;/requires assertj.core;/' avro/src/test/java/module-info.java
# Avro 1.11.5 has no 1.12.2 allow-list API to configure for test classes.
sed -i -e '/^import org\.apache\.avro\.util\.ClassSecurityValidator;$/d' \
    -e '/^    static {$/,/^    }$/d' \
    avro/src/test/java/tools/jackson/dataformat/avro/interop/ApacheAvroInteropUtil.java

%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%mvn_file ":{*}" %name/@1

%build
%mvn_build -s

%install
%mvn_install
install -Dm644 LICENSE %buildroot%_docdir/%name-%version/LICENSE
for module in avro cbor ion protobuf smile; do
    install -Dm644 "$module/src/main/resources/META-INF/NOTICE" \
        %buildroot%_docdir/%name-%version/$module-NOTICE
done

%files -f .mfiles-jackson-dataformats-binary
%doc %_docdir/%name-%version

%files -n jackson3-dataformat-cbor -f .mfiles-jackson-dataformat-cbor

%files -n jackson3-dataformat-smile -f .mfiles-jackson-dataformat-smile

%files -n jackson3-dataformat-avro -f .mfiles-jackson-dataformat-avro

%files -n jackson3-dataformat-protobuf -f .mfiles-jackson-dataformat-protobuf

%files -n jackson3-dataformat-ion -f .mfiles-jackson-dataformat-ion

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
