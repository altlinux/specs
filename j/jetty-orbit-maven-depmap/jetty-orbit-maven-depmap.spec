BuildRequires: rpm-build-java
Name: jetty-orbit-maven-depmap
Version: 1.0
Summary: maven depmap for org.eclipse.jetty.orbit jetty pom dependencies
License: GPL2+
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt2jpp1

Requires: jakarta-taglibs-standard
Requires: geronimo-annotation
Requires: geronimo-jaspic-spec
Requires: geronimo-jta
Requires: glassfish-jaf
Requires: glassfish-javamail
Requires: glassfish-jsp
Requires: objectweb-asm
Requires: tomcat-el-2.2-api
Requires: tomcat-jsp-2.2-api
Requires: tomcat-servlet-3.0-api

%description
%summary

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%_mavendepmapfragdir
cat > $RPM_BUILD_ROOT%_mavendepmapfragdir/%name << 'EOF'
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.servlet</artifactId>
        <version>8.1.0.v20120127</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>tomcat-servlet-3.0-api</artifactId>
        <version>3.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.security.auth.message</artifactId>
        <version>1.1</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>geronimo-jaspic-spec</artifactId>
        <version>1.1</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.mail.glassfish</artifactId>
        <version>1.4.0</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>glassfish-javamail-monolithic</artifactId>
        <version>1.4.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.transaction</artifactId>
        <version>1.1.1</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>geronimo-jta</artifactId>
        <version>1.1.1</version>
    </jpp>
</dependency>
<dependency>
    <maven>
	<groupId>org.eclipse.jetty.orbit</groupId>
	<artifactId>javax.annotation</artifactId>
        <version>1.0</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>geronimo-annotation</artifactId>
        <version>1.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>org.objectweb.asm</artifactId>
        <version>3.3.1</version>
    </maven>
    <jpp>
        <groupId>JPP/objectweb-asm</groupId>
        <artifactId>asm-all</artifactId>
        <version>3.3.1</version>
    </jpp>
</dependency>
<dependency>
    <maven>
	<groupId>org.eclipse.jetty.orbit</groupId>
	<artifactId>javax.servlet.jsp.jstl</artifactId>
        <version>3.0</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>taglibs-core</artifactId>
        <version>3.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
	<groupId>org.eclipse.jetty.orbit</groupId>
	<artifactId>javax.servlet.jsp</artifactId>
        <version>3.0</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>tomcat-jsp-api</artifactId>
        <version>3.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.el</artifactId>
        <version>2.2</version>
    </maven>
    <jpp> 
        <groupId>JPP</groupId>
        <artifactId>tomcat-el-api</artifactId>
        <version>7.0.23</version> 
    </jpp>
</dependency>
<dependency>
    <maven>
	<groupId>org.eclipse.jetty.orbit</groupId>
	<artifactId>org.apache.taglibs.standard.glassfish</artifactId>
        <version>3.0</version>
    </maven>
    <jpp>
        <groupId>JPP</groupId>
        <artifactId>taglibs-standard</artifactId>
        <version>3.0</version>
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>com.sun.el</artifactId>
        <version>2.2</version>
    </maven>
    <jpp> 
        <groupId>JPP</groupId>
        <artifactId>tomcat-el-api</artifactId>
        <version>7.0.23</version> 
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>org.apache.jasper.glassfish</artifactId>
        <version>2.2</version>
    </maven>
    <jpp> 
        <groupId>JPP</groupId>
	<artifactId>glassfish-jsp</artifactId>
        <version>7.0.23</version> 
    </jpp>
</dependency>
<dependency>
    <maven>
        <groupId>org.eclipse.jetty.orbit</groupId>
        <artifactId>javax.activation</artifactId>
        <version>2.2</version>
    </maven>
    <jpp> 
        <groupId>JPP</groupId>
	<artifactId>glassfish-jaf</artifactId>
        <version>7.0.23</version> 
    </jpp>
</dependency>
EOF


%files
%_mavendepmapfragdir/%name

%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2jpp1
- updated depmap

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1jpp1
- maven depmap for org.eclipse.jetty.orbit jetty pom dependencies
