%define _unpackaged_files_terminate_build 1

%def_with check

Name: jtharness
Version: 6.0
Release: alt2

Summary: The JT harness is a test harness very well suited for most types of unit testing
License: GPL-2.0
Group: Development/Java
Url: https://github.com/openjdk/jtharness
Vcs: https://github.com/openjdk/jtharness

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: ant
BuildRequires: java-21-openjdk-devel
BuildRequires: tomcat-servlet-4.0-api
%if_with check
BuildRequires: xvfb-run
BuildRequires: javapackages-tools
BuildRequires: ant-junit
BuildRequires: mockito
BuildRequires: byte-buddy
BuildRequires: byte-buddy-agent
BuildRequires: objenesis
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
%endif

ExcludeArch: i586

%description
The JT harness is a test harness very well suited for most types
of unit testing. Originally developed as a test harness to run
TCK test suites, it has since evolved into a general purpose
test platform.

%prep
%setup
JUNIT_JAR=$(find /usr/share/java -name "junit.jar" 2>/dev/null | head -n 1)
ASM_JAR=$(find /usr/share/java -name "asm.jar" -not -path "*jdk-bridge*" 2>/dev/null | head -n 1)
ASM_COMMONS_JAR=$(find /usr/share/java -name "asm-commons.jar" 2>/dev/null | head -n 1)
SERVLET_JAR=$(find /usr/share/java \( -name "servlet-api.jar" -o -name "tomcat-servlet-api.jar" \) 2>/dev/null | head -n 1)

cat > build/local.properties << EOF
BUILD_DIR=../JTHarness-build
junitlib=$JUNIT_JAR
asmjar=$ASM_JAR
asmcommonsjar=$ASM_COMMONS_JAR
servletjar=$SERVLET_JAR
EOF

TMPXML=$(mktemp)
echo '    <target name="setup-test-deps">' > $TMPXML
echo '        <path id="test-deps.classpath">' >> $TMPXML

find /usr/share/java -type f \( \
    -name "junit.jar" -o \
    -name "hamcrest.jar" -o \
    -name "mockito-core.jar" -o \
    -name "byte-buddy.jar" -o \
    -name "byte-buddy-agent.jar" -o \
    -name "objenesis.jar" \
\) 2>/dev/null | sort -u | while read -r jar; do
    echo "            <pathelement location=\"${jar}\"/>" >> $TMPXML
done

echo '        </path>' >> $TMPXML
echo '    </target>' >> $TMPXML

awk -v file="$TMPXML" '
    /<target name="setup-test-deps">/ {
        skip=1;
        while ((getline line < file) > 0) print line;
        close(file);
        next
    }
    skip && /<\/target>/ { skip=0; next }
    !skip { print }
' build/build.xml > build/build.xml.new

mv build/build.xml.new build/build.xml
rm -f $TMPXML

%build
export LANG=ru_RU.UTF-8
export LC_ALL=ru_RU.UTF-8
cd build
ant

%install
cd ../JTHarness-build/binaries/lib/
install -D -m 0644 ./javatest.jar %buildroot%_javadir/javatest.jar

%check
cd build
xvfb-run -a ant test

%files
%_javadir/javatest.jar
%doc LICENSE README.md

%changelog
* Tue Aug 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 6.0-alt2
- Fix missing UI and Help libraries (Bugs 57222, 57223).
- Set UTF-8 locale during build to fix Cyrillic path issues (Bug 57224).
- Correct description.
- Added check section.

* Mon Aug 18 2025 Timofei Fedotov <sovtouch@altlinux.org> 6.0-alt1
- Initial build for ALT Sisyphus.
