%define _unpackaged_files_terminate_build 1
%define _greenmail_standalone_dir %_javadir/%name
%define greenmail_webapp_dir %_datadir/%name

Name: greenmail
Version: 2.1.8
Release: alt1

Summary: Email test server for integration tests
License: Apache-2.0
Group: Development/Java
Url: https://greenmail-mail-test.github.io/greenmail
Vcs: https://github.com/greenmail-mail-test/greenmail.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: maven-war-plugin
BuildRequires: jackson-bom
BuildRequires: maven-shade-plugin
BuildRequires: maven-failsafe-plugin
BuildRequires: jakarta-mail
BuildRequires: angus-mail
BuildRequires: angus-activation
BuildRequires: jakarta-servlet
BuildRequires: jakarta-ws-rs
BuildRequires: slf4j log4j-slf4j
BuildRequires: jul-to-slf4j
BuildRequires: log4j
BuildRequires: junit
BuildRequires: junit5
BuildRequires: jersey-bom
BuildRequires: jersey-common
BuildRequires: jersey-client
BuildRequires: jersey-server
BuildRequires: jersey-hk2
BuildRequires: jersey-container-jdk-http
BuildRequires: jersey-container-servlet
BuildRequires: jersey-container-jetty-http
BuildRequires: jersey-media-json-jackson

%description
GreenMail provides in-memory mail servers (SMTP, SMTPS, POP3, POP3S, IMAP,
IMAPS) for integration tests and local development.

%package standalone
Summary: GreenMail standalone launcher
Group: Development/Java
Requires: java-17-openjdk-headless

%description standalone
Standalone GreenMail launcher with HTTP API support.

%package webapp
Summary: GreenMail embedded web application
Group: Development/Java
Requires: java-17-openjdk-headless
Requires: tomcat10

%description webapp
Embedded GreenMail web application archive.

%package junit4
Summary: GreenMail JUnit 4 support
Group: Development/Java

%description junit4
GreenMail integration helpers for JUnit 4 tests.

%package junit5
Summary: GreenMail JUnit 5 support
Group: Development/Java

%description junit5
GreenMail integration helpers for JUnit 5 tests.

%prep
%setup

# Spring modules are not available in target repository.
%pom_disable_module greenmail-spring pom.xml

# inject-maven-plugin is not packaged in ALT.
%pom_remove_plugin de.m3y.maven:inject-maven-plugin greenmail-core/pom.xml
%pom_remove_plugin -r -f org.codehaus.mojo:keytool-maven-plugin
%pom_remove_plugin -r -f :maven-enforcer-plugin

sed -i 's|<groupId>jakarta.servlet</groupId>|<groupId>javax.servlet</groupId>|' greenmail-webapp/pom.xml
sed -i 's|<artifactId>jakarta.servlet-api</artifactId>|<artifactId>javax.servlet-api</artifactId>|' greenmail-webapp/pom.xml
sed -i 's|<artifactId>jakarta.mail</artifactId>|<artifactId>angus-mail</artifactId>|g' pom.xml greenmail-core/pom.xml

# Parent POM is only a build aggregator.
%mvn_package :greenmail-parent __noinstall

# WAR artifact is installed manually because xmvn-install repository rejects WAR packaging.
%mvn_package :greenmail-webapp __noinstall

%build
# Skip tests because of no network access.
%mvn_build -s -j -f

%install
%mvn_install

install -Dpm0644 greenmail-webapp/target/greenmail-webapp-%version.war \
  %buildroot%greenmail_webapp_dir/greenmail-webapp.war

install -Dpm0755 /dev/stdin %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
JAR="%_greenmail_standalone_dir/greenmail-standalone.jar"
JAVA_EXTRA=""

usage() {
    echo "Usage: greenmail [JAVA_OPTS]" >&2
    echo "  Example: greenmail -Dgreenmail.setup.test.smtp -Dgreenmail.setup.test.api" >&2
    echo "  Env var: GREENMAIL_STANDALONE_JAVA_OPTS='-Dgreenmail.setup.test.all'" >&2
}

while [ $# -gt 0 ]; do
    case "$1" in
        --java-opt)
            [ $# -ge 2 ] || { usage; exit 2; }
            JAVA_EXTRA="${JAVA_EXTRA} $2"
            shift 2
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        --)
            shift
            break
            ;;
        -D*|-X*|-XX:*|-agentlib:*|-agentpath:*|-javaagent:*)
            JAVA_EXTRA="${JAVA_EXTRA} $1"
            shift
            ;;
        *)
            break
            ;;
    esac
done

GM_JAVA_OPTS="${GREENMAIL_STANDALONE_JAVA_OPTS:-}"
if [ -n "$JAVA_EXTRA" ]; then
    JAVA_EXTRA=${JAVA_EXTRA# }
    if [ -n "$GM_JAVA_OPTS" ]; then
        GM_JAVA_OPTS="$GM_JAVA_OPTS $JAVA_EXTRA"
    else
        GM_JAVA_OPTS="$JAVA_EXTRA"
    fi
fi

if [ -n "$GM_JAVA_OPTS" ]; then
    exec java $GM_JAVA_OPTS -jar "$JAR" "$@"
fi

exec java -jar "$JAR" "$@"
EOF

install -Dpm0755 /dev/stdin %buildroot%_bindir/greenmail-webapp <<'EOF'
#!/bin/sh
WAR="%greenmail_webapp_dir/greenmail-webapp.war"

HTTP_PORT="${GREENMAIL_WEBAPP_HTTP_PORT:-8080}"
SHUTDOWN_PORT="${GREENMAIL_WEBAPP_SHUTDOWN_PORT:-8005}"
BIND_ADDR="${GREENMAIL_WEBAPP_BIND_ADDR:-127.0.0.1}"
CONTEXT_PATH="${GREENMAIL_WEBAPP_CONTEXT_PATH:-/}"
BASE_DEF="${XDG_RUNTIME_DIR:-/tmp}/greenmail-webapp-${USER:-$(id -un)}"
CATALINA_BASE="${GREENMAIL_WEBAPP_BASE:-$BASE_DEF}"
CMD="${GREENMAIL_WEBAPP_TOMCAT_CMD:-start}"

JAVA_EXTRA=""
CATALINA_EXTRA=""

usage() {
    echo "Usage: greenmail-webapp [OPTIONS]" >&2
    echo "  --port N            HTTP port (default: 8080)" >&2
    echo "  --shutdown-port N   Tomcat shutdown port (default: 8005)" >&2
    echo "  --bind ADDR         Bind address (default: 127.0.0.1)" >&2
    echo "  --context-path /p   Context path (default: /)" >&2
    echo "  --base DIR          CATALINA_BASE directory" >&2
    echo "  --java-opt OPT      Append OPT to JAVA_OPTS" >&2
    echo "  --catalina-opt OPT  Append OPT to CATALINA_OPTS" >&2
    echo "  --tomcat-command C  start|stop (default: start)" >&2
}

while [ $# -gt 0 ]; do
    case "$1" in
        --port|--http-port)
            [ $# -ge 2 ] || { usage; exit 2; }
            HTTP_PORT="$2"
            shift 2
            ;;
        --shutdown-port)
            [ $# -ge 2 ] || { usage; exit 2; }
            SHUTDOWN_PORT="$2"
            shift 2
            ;;
        --bind)
            [ $# -ge 2 ] || { usage; exit 2; }
            BIND_ADDR="$2"
            shift 2
            ;;
        --context-path)
            [ $# -ge 2 ] || { usage; exit 2; }
            CONTEXT_PATH="$2"
            shift 2
            ;;
        --base)
            [ $# -ge 2 ] || { usage; exit 2; }
            CATALINA_BASE="$2"
            shift 2
            ;;
        --java-opt)
            [ $# -ge 2 ] || { usage; exit 2; }
            JAVA_EXTRA="${JAVA_EXTRA} $2"
            shift 2
            ;;
        --catalina-opt)
            [ $# -ge 2 ] || { usage; exit 2; }
            CATALINA_EXTRA="${CATALINA_EXTRA} $2"
            shift 2
            ;;
        --tomcat-command)
            [ $# -ge 2 ] || { usage; exit 2; }
            CMD="$2"
            shift 2
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        -D*|-X*|-XX:*)
            JAVA_EXTRA="${JAVA_EXTRA} $1"
            shift
            ;;
        *)
            usage
            exit 2
            ;;
    esac
done

TOMCAT_SERVER=/usr/libexec/tomcat/server
CATALINA_HOME="${CATALINA_HOME:-/usr/share/tomcat}"
if [ ! -x "$TOMCAT_SERVER" ]; then
    echo "greenmail-webapp: unable to find /usr/libexec/tomcat/server" >&2
    echo "Install tomcat10 package." >&2
    exit 1
fi

mkdir -p \
    "$CATALINA_BASE/conf/Catalina/localhost" \
    "$CATALINA_BASE/logs" \
    "$CATALINA_BASE/temp" \
    "$CATALINA_BASE/work" \
    "$CATALINA_BASE/webapps"

for conf in \
    catalina.properties \
    logging.properties \
    web.xml \
    context.xml

do
    if [ ! -f "$CATALINA_BASE/conf/$conf" ] && \
       [ -f "$CATALINA_HOME/conf/$conf" ]; then
        cp -f "$CATALINA_HOME/conf/$conf" "$CATALINA_BASE/conf/$conf"
    fi
done

case "$CONTEXT_PATH" in
    /) CTX_FILE="ROOT.xml" ;;
    /*) CTX_FILE="${CONTEXT_PATH#/}.xml" ;;
    *)
        echo "greenmail-webapp: context path must start with /" >&2
        exit 2
        ;;
esac

cat > "$CATALINA_BASE/conf/server.xml" <<EOT
<Server port="$SHUTDOWN_PORT" shutdown="SHUTDOWN">
  <Service name="Catalina">
    <Connector
      port="$HTTP_PORT"
      address="$BIND_ADDR"
      protocol="HTTP/1.1"
      connectionTimeout="20000"
      redirectPort="8443" />
    <Engine name="Catalina" defaultHost="localhost">
      <Host name="localhost" appBase="webapps"
            autoDeploy="true" unpackWARs="true" />
    </Engine>
  </Service>
</Server>
EOT

cat > "$CATALINA_BASE/conf/Catalina/localhost/$CTX_FILE" <<EOT
<Context docBase="$WAR" />
EOT

if [ -n "${GREENMAIL_WEBAPP_JAVA_OPTS:-}" ]; then
    if [ -n "${JAVA_OPTS:-}" ]; then
        JAVA_OPTS="$JAVA_OPTS ${GREENMAIL_WEBAPP_JAVA_OPTS}"
    else
        JAVA_OPTS="${GREENMAIL_WEBAPP_JAVA_OPTS}"
    fi
fi

if [ -n "$JAVA_EXTRA" ]; then
    JAVA_EXTRA=${JAVA_EXTRA# }
    if [ -n "${JAVA_OPTS:-}" ]; then
        JAVA_OPTS="$JAVA_OPTS $JAVA_EXTRA"
    else
        JAVA_OPTS="$JAVA_EXTRA"
    fi
fi

if [ -n "${GREENMAIL_WEBAPP_CATALINA_OPTS:-}" ]; then
    if [ -n "${CATALINA_OPTS:-}" ]; then
        CATALINA_OPTS="$CATALINA_OPTS ${GREENMAIL_WEBAPP_CATALINA_OPTS}"
    else
        CATALINA_OPTS="${GREENMAIL_WEBAPP_CATALINA_OPTS}"
    fi
fi

if [ -n "$CATALINA_EXTRA" ]; then
    CATALINA_EXTRA=${CATALINA_EXTRA# }
    if [ -n "${CATALINA_OPTS:-}" ]; then
        CATALINA_OPTS="$CATALINA_OPTS $CATALINA_EXTRA"
    else
        CATALINA_OPTS="$CATALINA_EXTRA"
    fi
fi

export CATALINA_HOME CATALINA_BASE JAVA_OPTS CATALINA_OPTS

exec "$TOMCAT_SERVER" "$CMD"
EOF

%files -f .mfiles-greenmail
%doc --no-dereference README.md
%doc --no-dereference license.txt

%files standalone -f .mfiles-greenmail-standalone
%_bindir/greenmail

%files webapp
%_bindir/greenmail-webapp
%greenmail_webapp_dir/greenmail-webapp.war

%files junit4 -f .mfiles-greenmail-junit4
%files junit5 -f .mfiles-greenmail-junit5
%changelog
* Wed Mar 18 2026 Ivan Khanas <xeno@altlinux.org> 2.1.8-alt1
- Initial build for ALT.
