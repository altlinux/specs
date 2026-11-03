%define _unpackaged_files_terminate_build 1

Name: osgi-api8
Version: 8.1.0
Release: alt1

Summary: Individual OSGi Core and Compendium Release 8.1 APIs
License: Apache-2.0
Group: Development/Java
Url: https://github.com/osgi/osgi
Vcs: https://github.com/osgi/osgi.git

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: aqute-bnd
BuildRequires: unzip
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: osgi-annotation

# The main RPM contains org.osgi.util.promise.
Requires: %name-function = %version-%release

%description
Individually versioned OSGi API bundles built from Release 8.1 sources.
Promise is provided by the main package; the other APIs are subpackages.

%package function
Summary: OSGi Function API
Group: Development/Java

%description function
OSGi Function API (org.osgi.util.function 1.2.0).

%package dto
Summary: OSGi Data Transfer Object API
Group: Development/Java

%description dto
OSGi Data Transfer Object API (org.osgi.dto 1.1.1).

%package resource
Summary: OSGi Resource and Capability API
Group: Development/Java
Requires: %name-dto = %version-%release

%description resource
OSGi Resource and Capability API (org.osgi.resource 1.0.1).

%package namespace-implementation
Summary: OSGi Implementation Namespace API
Group: Development/Java
Requires: %name-resource = %version-%release

%description namespace-implementation
OSGi Implementation Namespace API (org.osgi.namespace.implementation 1.0.0).

%package namespace-extender
Summary: OSGi Extender Namespace API
Group: Development/Java
Requires: %name-resource = %version-%release

%description namespace-extender
OSGi Extender Namespace API (org.osgi.namespace.extender 1.0.1).

%package service-condition
Summary: OSGi Condition Service API
Group: Development/Java

%description service-condition
OSGi Condition Service API (org.osgi.service.condition 1.0.0).

%package service-component
Summary: OSGi Declarative Services API
Group: Development/Java
Requires: %name-dto = %version-%release
Requires: %name-namespace-extender = %version-%release
Requires: %name-function = %version-%release
Requires: %name = %version-%release

%description service-component
OSGi Declarative Services API (org.osgi.service.component 1.5.1).

%package service-component-annotations
Summary: OSGi Declarative Services Annotations API
Group: Development/Java

%description service-component-annotations
OSGi Declarative Services Annotations API (org.osgi.service.component.annotations 1.5.1).

%package service-cm
Summary: OSGi Configuration Admin API
Group: Development/Java
Requires: %name-namespace-implementation = %version-%release

%description service-cm
OSGi Configuration Admin API (org.osgi.service.cm 1.6.1).

%package service-log
Summary: OSGi Log Service API
Group: Development/Java

%description service-log
OSGi Log Service API (org.osgi.service.log 1.5.0).

%package service-metatype
Summary: OSGi Metatype Service API
Group: Development/Java
Requires: %name-namespace-extender = %version-%release
Requires: %name-namespace-implementation = %version-%release

%description service-metatype
OSGi Metatype Service API (org.osgi.service.metatype 1.4.1).

%package service-metatype-annotations
Summary: OSGi Metatype Annotations API
Group: Development/Java

%description service-metatype-annotations
OSGi Metatype Annotations API (org.osgi.service.metatype.annotations 1.4.1).

%package service-prefs
Summary: OSGi Preferences Service API
Group: Development/Java

%description service-prefs
OSGi Preferences Service API (org.osgi.service.prefs 1.1.2).

%package service-event
Summary: OSGi Event Admin API
Group: Development/Java
Requires: %name-namespace-implementation = %version-%release

%description service-event
OSGi Event Admin API (org.osgi.service.event 1.4.1).

%package service-repository
Summary: OSGi Repository Service API
Group: Development/Java
Requires: %name-resource = %version-%release
Requires: %name-function = %version-%release
Requires: %name = %version-%release

%description service-repository
OSGi Repository Service API (org.osgi.service.repository 1.1.0).

%package service-resolver
Summary: OSGi Resolver Service API
Group: Development/Java
Requires: %name-resource = %version-%release

%description service-resolver
OSGi Resolver Service API (org.osgi.service.resolver 1.1.1).

%package util-tracker
Summary: OSGi Service Tracker API
Group: Development/Java

%description util-tracker
OSGi Service Tracker API (org.osgi.util.tracker 1.5.4).

%prep
%setup -q

%mvn_package org.osgi:org.osgi.util.function function
%mvn_package org.osgi:org.osgi.util.promise
%mvn_package org.osgi:org.osgi.dto dto
%mvn_package org.osgi:org.osgi.resource resource
%mvn_package org.osgi:org.osgi.namespace.implementation namespace-implementation
%mvn_package org.osgi:org.osgi.namespace.extender namespace-extender
%mvn_package org.osgi:org.osgi.service.condition service-condition
%mvn_package org.osgi:org.osgi.service.component service-component
%mvn_package org.osgi:org.osgi.service.component.annotations service-component-annotations
%mvn_package org.osgi:org.osgi.service.cm service-cm
%mvn_package org.osgi:org.osgi.service.log service-log
%mvn_package org.osgi:org.osgi.service.metatype service-metatype
%mvn_package org.osgi:org.osgi.service.metatype.annotations service-metatype-annotations
%mvn_package org.osgi:org.osgi.service.prefs service-prefs
%mvn_package org.osgi:org.osgi.service.event service-event
%mvn_package org.osgi:org.osgi.service.repository service-repository
%mvn_package org.osgi:org.osgi.service.resolver service-resolver
%mvn_package org.osgi:org.osgi.util.tracker util-tracker

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$JAVA_HOME/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

# Aggregate APIs are used only to compile against the packaged OSGi APIs.
api_cp=%_javadir/osgi-core/osgi.core.jar:%_javadir/osgi-compendium/osgi.cmpn.jar:%_javadir/osgi-annotation/osgi.annotation.jar
mkdir -p target/classes target/raw target/poms target/bnd

# Build locally supplied API classes first; do not copy aggregate API classes
# into the published bundles.
classpath=$api_cp
for entry in \
    'org.osgi.util.function 1.2.0' \
    'org.osgi.util.promise 1.3.0' \
    'org.osgi.dto 1.1.1' \
    'org.osgi.resource 1.0.1' \
    'org.osgi.namespace.implementation 1.0.0' \
    'org.osgi.namespace.extender 1.0.1' \
    'org.osgi.service.condition 1.0.0' \
    'org.osgi.service.component 1.5.1' \
    'org.osgi.service.component.annotations 1.5.1' \
    'org.osgi.service.cm 1.6.1' \
    'org.osgi.service.log 1.5.0' \
    'org.osgi.service.metatype 1.4.1' \
    'org.osgi.service.metatype.annotations 1.4.1' \
    'org.osgi.service.prefs 1.1.2' \
    'org.osgi.service.event 1.4.1' \
    'org.osgi.service.repository 1.1.0' \
    'org.osgi.service.resolver 1.1.1' \
    'org.osgi.util.tracker 1.5.4'
do
    set -- $entry
    module=$1
    version=$2
    classes="$PWD/target/classes/$module"
    mkdir -p "$classes"

    case "$module" in
        org.osgi.service.component.annotations|org.osgi.service.metatype.annotations)
            # Annotation classes were compiled from the owning API sources.
            ;;
        *)
            find "$module/src" -name '*.java' -type f \
                ! -name module-info.java | sort > "target/$module.sources"
            javac --release 8 -encoding UTF-8 -cp "$classpath" \
                -d "$classes" "@target/$module.sources"
            case "$module" in
                org.osgi.service.component)
                    dest="$PWD/target/classes/org.osgi.service.component.annotations/org/osgi/service/component"
                    mkdir -p "$dest"
                    mv "$classes/org/osgi/service/component/annotations" "$dest/"
                    ;;
                org.osgi.service.metatype)
                    dest="$PWD/target/classes/org.osgi.service.metatype.annotations/org/osgi/service/metatype"
                    mkdir -p "$dest"
                    mv "$classes/org/osgi/service/metatype/annotations" "$dest/"
                    ;;
            esac
            ;;
    esac

    jar -cf "target/raw/$module.jar" -C "$classes" .

    # Export only packages present in THIS JAR, including the root package.
    # Bnd obtains package versions from the compiled @Version package-info.
    packages=$(find "$classes" -type f -name '*.class' | \
        sed -e "s|^$classes/||" -e 's|/[^/]*$||' -e 's|/|.|g' | \
        sort -u | paste -sd, -)
    test -n "$packages"

    bnd_cp=$(printf '%%s' "$classpath" | tr ':' ',')
    resources="@$PWD/target/raw/$module.jar"
    case "$module" in
        org.osgi.service.component)
            resources="$resources,xmlns/scr=$PWD/xmlns/scr" ;;
        org.osgi.service.metatype)
            resources="$resources,xmlns/metatype=$PWD/xmlns/metatype" ;;
        org.osgi.service.repository)
            resources="$resources,xmlns/repository=$PWD/xmlns/repository" ;;
    esac
    cat > "target/bnd/$module.bnd" <<EOF
-classpath: $PWD/target/raw/$module.jar,$bnd_cp
-output: $PWD/target/$module.jar
-includeresource: $resources
-exportcontents: $packages
-noextraheaders: true
-reproducible: true
Bundle-ManifestVersion: 2
Bundle-SymbolicName: $module
Bundle-Version: $version
Automatic-Module-Name: $module
Import-Package: *
EOF
    (cd target/bnd && bnd do "$module.bnd")

    # Provide original-style Maven coordinates with the local ALT OSGi
    # annotation API. Other dependencies are declared for each module below.
    pom="target/poms/$module.pom"
    annotation_scope=provided
    case "$module" in
        org.osgi.service.component|org.osgi.service.component.annotations|org.osgi.service.cm|org.osgi.service.event)
            annotation_scope=compile ;;
    esac
    cat > "$pom" <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.osgi</groupId>
  <artifactId>$module</artifactId>
  <version>$version</version>
  <packaging>jar</packaging>
  <dependencies>
    <dependency><groupId>org.osgi</groupId><artifactId>osgi.annotation</artifactId><version>8.0.1</version><scope>$annotation_scope</scope></dependency>
EOF
    case "$module" in
        org.osgi.util.promise)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.function</artifactId><version>1.2.0</version></dependency>' >> "$pom" ;;
        org.osgi.resource)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.dto</artifactId><version>1.1.1</version></dependency>' >> "$pom" ;;
        org.osgi.namespace.implementation|org.osgi.namespace.extender|org.osgi.service.repository|org.osgi.service.resolver)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.resource</artifactId><version>1.0.1</version><scope>provided</scope></dependency>' >> "$pom" ;;
    esac
    case "$module" in
        org.osgi.service.component|org.osgi.service.component.annotations|org.osgi.service.cm|org.osgi.service.log|org.osgi.service.metatype|org.osgi.service.metatype.annotations|org.osgi.service.event|org.osgi.service.resolver|org.osgi.util.tracker)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.core</artifactId><version>8.0.0</version><scope>provided</scope></dependency>' >> "$pom" ;;
    esac
    case "$module" in
        org.osgi.service.cm|org.osgi.service.event)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.implementation</artifactId><version>1.0.0</version></dependency>' >> "$pom" ;;
        org.osgi.service.metatype|org.osgi.service.component)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.extender</artifactId><version>1.0.1</version></dependency>' >> "$pom" ;;
    esac
    case "$module" in
        org.osgi.service.metatype)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.implementation</artifactId><version>1.0.0</version></dependency>' >> "$pom" ;;
        org.osgi.service.component|org.osgi.service.repository)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.function</artifactId><version>1.2.0</version></dependency>' >> "$pom"
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.promise</artifactId><version>1.3.0</version></dependency>' >> "$pom" ;;
    esac
    case "$module" in
        org.osgi.service.metatype.annotations)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.service.metatype</artifactId><version>1.4.1</version><scope>provided</scope></dependency>' >> "$pom" ;;
    esac
    # Complete the documented API dependencies in the generated POMs.
    case "$module" in
        org.osgi.service.component|org.osgi.service.component.annotations)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.dto</artifactId><version>1.1.1</version><scope>provided</scope></dependency>' >> "$pom"
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.service.condition</artifactId><version>1.0.0</version><scope>provided</scope></dependency>' >> "$pom" ;;
    esac
    case "$module" in
        org.osgi.service.component.annotations)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.extender</artifactId><version>1.0.1</version></dependency>' >> "$pom"
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.function</artifactId><version>1.2.0</version></dependency>' >> "$pom"
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.promise</artifactId><version>1.3.0</version></dependency>' >> "$pom" ;;
        org.osgi.service.event)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.service.component.annotations</artifactId><version>1.5.1</version><scope>provided</scope></dependency>' >> "$pom" ;;
        org.osgi.service.metatype.annotations)
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.extender</artifactId><version>1.0.1</version><scope>provided</scope></dependency>' >> "$pom"
            echo '    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.namespace.implementation</artifactId><version>1.0.0</version><scope>provided</scope></dependency>' >> "$pom" ;;
    esac
    cat >> "$pom" <<EOF
  </dependencies>
</project>
EOF

    # Keep every locally built module ahead of the aggregate JARs.
    classpath="$classes:$classpath"
done

# Dependencies between these artifacts are supplied by the matching RPMs.
# XMvn installs the Maven models while the RPM OSGi generator supplies
# bundle requirements from the final Bnd manifests.
%mvn_artifact --skip-dependencies target/poms/org.osgi.util.function.pom target/org.osgi.util.function.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.util.promise.pom target/org.osgi.util.promise.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.dto.pom target/org.osgi.dto.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.resource.pom target/org.osgi.resource.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.namespace.implementation.pom target/org.osgi.namespace.implementation.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.namespace.extender.pom target/org.osgi.namespace.extender.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.condition.pom target/org.osgi.service.condition.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.component.pom target/org.osgi.service.component.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.component.annotations.pom target/org.osgi.service.component.annotations.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.cm.pom target/org.osgi.service.cm.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.log.pom target/org.osgi.service.log.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.metatype.pom target/org.osgi.service.metatype.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.metatype.annotations.pom target/org.osgi.service.metatype.annotations.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.prefs.pom target/org.osgi.service.prefs.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.event.pom target/org.osgi.service.event.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.repository.pom target/org.osgi.service.repository.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.service.resolver.pom target/org.osgi.service.resolver.jar
%mvn_artifact --skip-dependencies target/poms/org.osgi.util.tracker.pom target/org.osgi.util.tracker.jar

%install
%mvn_install

%check
for file in target/org.osgi.*.jar; do
    unzip -p "$file" META-INF/MANIFEST.MF | grep -q '^Bundle-SymbolicName:'
done

%files function -f .mfiles-function
%doc LICENSE NOTICE

%files -f .mfiles
%doc LICENSE NOTICE README.md

%files dto -f .mfiles-dto
%doc LICENSE NOTICE

%files resource -f .mfiles-resource
%doc LICENSE NOTICE

%files namespace-implementation -f .mfiles-namespace-implementation
%doc LICENSE NOTICE

%files namespace-extender -f .mfiles-namespace-extender
%doc LICENSE NOTICE

%files service-condition -f .mfiles-service-condition
%doc LICENSE NOTICE

%files service-component -f .mfiles-service-component
%doc LICENSE NOTICE

%files service-component-annotations -f .mfiles-service-component-annotations
%doc LICENSE NOTICE

%files service-cm -f .mfiles-service-cm
%doc LICENSE NOTICE

%files service-log -f .mfiles-service-log
%doc LICENSE NOTICE

%files service-metatype -f .mfiles-service-metatype
%doc LICENSE NOTICE

%files service-metatype-annotations -f .mfiles-service-metatype-annotations
%doc LICENSE NOTICE

%files service-prefs -f .mfiles-service-prefs
%doc LICENSE NOTICE

%files service-event -f .mfiles-service-event
%doc LICENSE NOTICE

%files service-repository -f .mfiles-service-repository
%doc LICENSE NOTICE

%files service-resolver -f .mfiles-service-resolver
%doc LICENSE NOTICE

%files util-tracker -f .mfiles-util-tracker
%doc LICENSE NOTICE

%changelog
* Tue Nov 03 2026 Timofei Fedotov <sovtouch@altlinux.org> 8.1.0-alt1
- Initial build.
