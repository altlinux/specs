Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-core
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define base_name       supported
%define short_name      taglibs-%{base_name}
%define name            jakarta-%{short_name}

%define pom_ver         1.1.2
%define application_ver 1.0.1
%define benchmark_ver   1.0
%define bsf_ver         1.0
%define cache_ver       1.0
%define datetime_ver    1.0.1
%define dbtags_ver      1.0.0
%define i18n_ver        1.0
%define input_ver       1.0
%define io_ver          1.0
%define jmstags_ver     1.0
%define jndi_ver        1.0
%define log_ver         1.0
%define mailer_ver      1.1
%define page_ver        1.0.1
%define random_ver      1.0.2
%define rdc_ver         1.0
%define regexp_ver      1.0.1
%define request_ver     1.0.1
%define response_ver    1.0.1
%define scrape_ver      1.0
%define session_ver     1.0.1
%define string_ver      1.1.0
%define xsl_ver         1.0.1
%define xtags_ver       1.0


Name:           jakarta-taglibs-supported
Version:        1.1.2
Release:        alt3_0.20050928.4jpp5
Epoch:          0
Summary:        Jakarta-supported custom JSTL libraries
License:        Apache Software License
Group:          Development/Java
#Vendor:         JPackage Project
#Distribution:   JPackage
URL:            http://jakarta.apache.org/taglibs/
Source0:        http://cvs.apache.org/builds/jakarta-taglibs/nightly/src/jakarta-taglibs-src-20050921.tar.gz
Source1:        http://repo1.maven.org/maven2/taglibs/application/1.0.1/application-1.0.1.pom
Source2:        http://repo1.maven.org/maven2/taglibs/benchmark/1.0/benchmark-1.0.pom
Source3:        bsf-1.0.pom
Source4:        cache-1.0.pom
Source5:        http://repo1.maven.org/maven2/taglibs/datetime/1.0.1/datetime-1.0.1.pom
Source6:        http://repo1.maven.org/maven2/taglibs/dbtags/1.0.0/dbtags-1.0.0.pom
Source7:        i18n-1.0.pom
Source8:        input-1.0.pom
Source9:        io-1.0.pom
Source10:       jmstags-1.0.pom
Source11:       jndi-1.0.pom
Source12:       http://repo1.maven.org/maven2/taglibs/log/1.0/log-1.0.pom
Source13:       http://repo1.maven.org/maven2/taglibs/mailer/1.1/mailer-1.1.pom
Source14:       http://repo1.maven.org/maven2/taglibs/page/1.0.1/page-1.0.1.pom
Source15:       http://repo1.maven.org/maven2/taglibs/random/1.0.2/random-1.0.2.pom
Source16:       rdc-1.0.pom
Source17:       http://repo1.maven.org/maven2/taglibs/regexp/1.0.1/regexp-1.0.1.pom
Source18:       http://repo1.maven.org/maven2/taglibs/request/1.0.1/request-1.0.1.pom
Source19:       http://repo1.maven.org/maven2/taglibs/response/1.0.1/response-1.0.1.pom
Source20:       scrape-1.0.pom
Source21:       http://repo1.maven.org/maven2/taglibs/session/1.0.1/session-1.0.1.pom
Source22:       http://repo1.maven.org/maven2/taglibs/string/1.1.0/string-1.1.0.pom
Source23:       xtags-1.0.pom
Patch0:         jakarta-taglibs-supported-rdc-Number.patch

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant17 >= 0:1.6.5
BuildRequires: ant17-nodeps
BuildRequires: ant17-trax
BuildRequires: bsf
BuildRequires: dom4j
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-messenger
BuildRequires: jakarta-taglibs-standard
BuildRequires: glassfish-jaf
BuildRequires: glassfish-javamail
BuildRequires: jaxen
BuildRequires: geronimo-jms-1.1-api
BuildRequires: geronimo-jsp-2.0-api
BuildRequires: log4j
BuildRequires: oro
BuildRequires: servletapi4
BuildRequires: geronimo-servlet-2.4-api
BuildRequires: struts
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Tag libraries that are officially supported at Jakarta Taglibs. 
It is important to note that the functionality covered by some 
of these tag libraries may coincide with standardization 
efforts in the Java Community Process (JCP), both presently 
and in the future. 

%package        poms
Summary:        POMs for Supported Tag Libraries
Group:          Development/Java
Version:        %{version}

%description    poms
%{summary}.


%package        application
Summary:        Application Tag Library
Group:          Development/Java
Version:        %{application_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    application
The Application custom tag library contains tags which can be 
used to access information contained in the ServletContext for 
a web application.
Tags are provided to access information in "application"-scoped 
attributes and web application initialization parameters, which 
are defined in the "/WEB-INF/web.xml" file.

%package        benchmark
Summary:        Benchmark Tag Library
Group:          Development/Java
Version:        %{benchmark_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    benchmark
In dicussions about how best to design tag libraries, issues of 
performance sometimes arise. The simple 'benchmark' tag library 
should aid in the performance testing of other taglibs and JSP 
pages in general. This library isn't a full-featured benchmarking 
package. It's just a simple way to get rough data if you want to 
sketch the relative performance of tags, tag combinations, or 
arbitrary JSP fragments.

%package        bsf
Summary:        BSF Tag Library
Group:          Development/Java
Version:        %{bsf_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: bsf

%description    bsf
The Bean Scripting Framework (BSF) is an architecture for 
incorporating scripting into Java applications and applets. 
Scripting languages such as Netscape Rhino (Javascript), Tcl, 
Python, NetRexx, Ruby, JudoScript, and XSLT are commonly used 
to augment an application's function or to script together a 
set of application components to form an application.

%package        cache
Summary:        Cache Tag Library
Group:          Development/Java
Version:        %{cache_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    cache
The Cache Taglib lets you cache fragments of your JSP pages. 
In a large web application where performance is important, 
caching might be appropriate at many levels within your 
architecture. Caching fragments of JSP pages is the option 
that's simultaneously the most flexible and the most tedious 
(that is, the most noticeable to JSP page authors). Using the 
Cache Taglib, you can mark individual sections of your JSP 
page as cacheable.

%package        datetime
Summary:        DateTime Tag Library
Group:          Development/Java
Version:        %{datetime_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    datetime
The DateTime custom tag library contains tags which can be 
used to handle date and time related functions. Tags are 
provided for formatting a Date for output, generating a Date 
from HTML forum input, using time zones, and localization.

%package        dbtags
Summary:        DBTags Tag Library
Group:          Development/Java
Version:        %{dbtags_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    dbtags
The DBTags custom tag library contains tags which can be 
used to read from and write to an SQL database.

%package        i18n
Summary:        I18N Tag Library
Group:          Development/Java
Version:        %{i18n_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    i18n
The I18N custom tag library contains tags that help manage 
the complexity of creating internationalized web applications. 
For those not familiar with the term "i18n", it is a standard 
abbreviation for "internationalization", which starts with the 
letter I, ends with the letter N, and contains a total of 18 
letters.
While some may see similarity with the struts message tag, 
these tags have several advantages, particularly with respect 
to message arguments, not to mention the fact that its a 
standalone tag library and doesn't require the user to adopt 
(or rip components out of) struts. 

%package        input
Summary:        Input Tag Library
Group:          Development/Java
Version:        %{input_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    input
The "input" tag extension library lets you present HTML 
<form> elements that are tied to the ServletRequest that 
caused the current JSP page to run. That is, using this 
library, you can easily prepopulate form elements with prior 
values that the user has chosen -- or with default values for 
the first time a user hits a web page. This is useful when 
you need to present the same page to the user several times 
(e.g., for server-side validation).

%package        io
Summary:        IO Tag Library
Group:          Development/Java
Version:        %{io_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    io
The IO custom tag library contains tags which can be used 
to perform a variety of input and output related tasks from 
inside JSP. A variety of protocols are supported such as HTTP, 
HTTPS, FTP, XML-RPC and SOAP requests.

%package        jmstags
Summary:        JMS Tag Library
Group:          Development/Java
Version:        %{jmstags_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: jms_1_1_api
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-messenger

%description    jmstags
The JMS custom tag library contains tags which can be used to 
perform a variety of JMS related operations such as sending and 
receiving messages from inside JSP. This taglib is currently 
built on top of the Messenger component from Jakarta Commons. 

%package        jndi
Summary:        JNDI Tag Library
Group:          Development/Java
Version:        %{jndi_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    jndi
The JNDI Tag Library creates an instance of a javax.naming.Context
based on the values of the attributes providing some of the 
standard values. In addition to the System properties and the 
jndi.properties, some standard properties are scanned in the 
pageContext attributes.

%package        log
Summary:        Log Tag Library
Group:          Development/Java
Version:        %{log_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: log4j
Requires: jakarta-commons-logging
Requires: jakarta-taglibs-standard

%description    log
The Log library allows you to embed logging calls in your JSP 
which can be output to a variety of destinations thanks to the 
power of the log4j project.

%package        mailer
Summary:        Mailer Tag Library
Group:          Development/Java
Version:        %{mailer_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: glassfish-jaf
Requires: glassfish-javamail

%description    mailer
This custom tag library is used to send e-mail. 


%package        page
Summary:        Page Tag Library
Group:          Development/Java
Version:        %{page_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    page
The Page custom tag library contains tags which can be used 
to access all the information about the PageContext for a JSP 
page.
Tags are provided to access information in "page"-scoped 
attributes.

%package        random
Summary:        Random Tag Library
Group:          Development/Java
Version:        %{random_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    random
This custom tag library is used to create random string 
and number generators. 

%package        rdc
Summary:        Reusable Dialog Components (RDC) Tag Library
Group:          Development/Java
Version:        %{rdc_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: jakarta-commons-el
Requires: jakarta-commons-logging

%description    rdc
JSP-2.0 Reusable Dialog Components (RDC) --- a framework for 
creating JSP taglibs that aid in rapid development of voice 
and multimodal applications. 

%package        regexp
Summary:        Regexp Tag Library
Group:          Development/Java
Version:        %{regexp_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: oro

%description    regexp
The Regexp custom tag library contains tags which can be used 
to perform Perl syntax regular expressions.
These tags implement the 3 most common Perl5 operations 
involving regular expressions:
[m]/pattern/[i][m][s][x] 
s/pattern/replacement/[g][i][m][o][s][x] 
and split() 
As with Perl, any non-alphanumeric character can be used 
in lieu of the slashes.

%package        request
Summary:        Request Tag Library
Group:          Development/Java
Version:        %{request_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    request
The Request custom tag library contains tags which can be used to 
access all the information about the HTTP request for a JSP page.
Tags are provided to access information in the HTTP request for 
HTTP input parameters from a POST or GET, HTTP Headers, Cookies, 
request attributes, and session information related to this request.

%package        response
Summary:        Response Tag Library
Group:          Development/Java
Version:        %{response_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    response
The Response custom tag library contains tags which can be used 
to set all the information for an HTTP response for a JSP page.
This includes creating cookies and setting their values, setting 
HTTP headers, returning back an HTTP error, or sending an HTTP 
redirect.

%package        scrape
Summary:        Scrape Tag Library
Group:          Development/Java
Version:        %{scrape_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    scrape
The scrape tag library can scrape or extract content from web 
documents and display the content in your JSP. For example, 
you could scrape stock quotes from other web sites and display 
them in your pages.

%package        session
Summary:        Session Tag Library
Group:          Development/Java
Version:        %{session_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard

%description    session
The Session JSP tag library provides tags for reading or 
modifying client HttpSession information.
A servlet container uses an HttpSession to store information 
about a clients session on the server. By default a JSP page 
will create a session for a user. The user is tied to the 
session using either a Cookie or by using URL rewriting. This 
is how you can tie information to a user between multiple HTTP 
requests to your server.
Session Attributes are what makes it possible to store 
information about a clients session between multiple HTTP 
requests. A session attribute consists of a name and value. To 
save information about a users session on your server use the 
setattribute tag.

%package        string
Summary:        String Tag Library
Group:          Development/Java
Version:        %{string_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: jakarta-commons-lang

%description    string
This custom tag library is used to manipulate Strings. 
It is currently built on top of the Lang 2.0 component 
from Jakarta Commons. 

%package        xtags
Summary:        XTags Tag Library
Group:          Development/Java
Version:        %{xtags_ver}
Requires: %{name}-poms = %{epoch}:%{pom_ver}-%{release}
Requires: jakarta-taglibs-standard
Requires: adaptx
Requires: dom4j
Requires: jaxen
Requires: xalan-j2
Requires: xerces-j2

%description    xtags
XTags is a JSP custom tag library for working with XML. XTags 
implements an XSLT-like language allowing XML to be styled and 
processed from directly within a JSP page using familiar XSLT 
and XPath techniques. 
In many ways XTags is like XSLT implemented in JSP allowing you 
to seamlessly work with JSP, custom tags, JavaBeans and the 
whole J2EE platform from inside a single piece of JSP! 
XTags is currently built on top of dom4j the flexible open 
source XML framework for the Java platform. Though increasingly 
XTags will use a pluggable XPath engine to support the travesal 
of DOM and Java Beans too. 


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires: jakarta-taglibs-standard
Requires: jakarta-taglibs-supported-application
Requires: jakarta-taglibs-supported-benchmark
Requires: jakarta-taglibs-supported-bsf
Requires: jakarta-taglibs-supported-cache
Requires: jakarta-taglibs-supported-datetime
Requires: jakarta-taglibs-supported-dbtags
Requires: jakarta-taglibs-supported-i18n
Requires: jakarta-taglibs-supported-input
Requires: jakarta-taglibs-supported-io
Requires: jakarta-taglibs-supported-jmstags
Requires: jakarta-taglibs-supported-jndi
Requires: jakarta-taglibs-supported-log
Requires: jakarta-taglibs-supported-mailer
Requires: jakarta-taglibs-supported-page
Requires: jakarta-taglibs-supported-random
Requires: jakarta-taglibs-supported-rdc
Requires: jakarta-taglibs-supported-regexp
Requires: jakarta-taglibs-supported-request
Requires: jakarta-taglibs-supported-response
Requires: jakarta-taglibs-supported-scrape
Requires: jakarta-taglibs-supported-session
Requires: jakarta-taglibs-supported-string
Requires: jakarta-taglibs-supported-xtags
Requires: adaptx
Requires: bsf
Requires: dom4j
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-el
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-messenger
Requires: jakarta-taglibs-standard
Requires: glassfish-jaf
Requires: glassfish-javamail
Requires: jaxen
Requires: jms_1_1_api
Requires: log4j
Requires: oro
Requires: servletapi4
Requires: servletapi5
Requires: struts
Requires: xalan-j2
Requires: xerces-j2

%description    demo
%{summary}.


%prep
%setup -q -n jakarta-taglibs
cp build.properties.sample build.properties
for b in */build.xml; do
    sed -i -e 's/file://' $b
done

%patch0 -b .sav0

%build
export CLASSPATH=$(build-classpath glassfish-javamail jaf_1_1_api jaxen xalan-j2-serializer)
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first \
    -Dbase.dir=$(pwd) \
    -Dbsf.jar=$(build-classpath bsf) \
    -Dservlet.jar=$(build-classpath servlet_2_3_api) \
    -Dservlet23.jar=$(build-classpath servlet_2_3_api) \
    -Dservlet24.jar=$(build-classpath servlet_2_4_api) \
    -Djsp20.jar=$(build-classpath jsp_2_0_api) \
    -Djsp-api.jar=$(build-classpath jsp_2_0_api) \
    -Djms.jar=$(build-classpath jms_1_1_api) \
    -Djakarta-oro2.jar=$(build-classpath oro) \
    -Djdbc2_0-stdext.jar=$(build-classpath jdbc-stdext) \
    -Ddom4j.jar=$(build-classpath dom4j) \
    -Ddom.jar=$(build-classpath dom) \
    -Dsax.jar=$(build-classpath sax) \
    -Djaxp.jar=$(build-classpath jaxp) \
    -Djaxp-api.jar=$(build-classpath jaxp) \
    -Dxalan.jar=$(build-classpath xalan-j2) \
    -DxercesImpl.jar=$(build-classpath xerces-j2) \
    -Djstl.jar=$(build-classpath taglibs-core) \
    -Dstandard.jar=$(build-classpath taglibs-standard) \
    -Dstruts12.jar=$(build-classpath struts) \
    -Dcommons-beanutils.jar=$(build-classpath commons-beanutils) \
    -Dcommons-beanutils-core.jar=$(build-classpath commons-beanutils-core) \
    -Dcommons-collections.jar=$(build-classpath commons-collections) \
    -Dcommons-digester.jar=$(build-classpath commons-digester) \
    -Dcommons-el.jar=$(build-classpath commons-el) \
    -Dcommons-lang.jar=$(build-classpath commons-lang) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dcommons-messenger.jar=$(build-classpath commons-messenger) \
    -Dcrimson.jar=$(build-classpath xerces-j2) \

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
for tl in application benchmark bsf cache datetime dbtags i18n input io jmstags jndi log mailer page random rdc regexp request response scrape session string xtags; do
case ${tl} in
application) ver=%{application_ver};;
benchmark) ver=%{benchmark_ver};;
bsf) ver=%{bsf_ver};;
cache) ver=%{cache_ver};;
datetime) ver=%{datetime_ver};;
dbtags) ver=%{dbtags_ver};;
i18n) ver=%{i18n_ver};;
input) ver=%{input_ver};;
io) ver=%{io_ver};;
jmstags) ver=%{jmstags_ver};;
jndi) ver=%{jndi_ver};;
log) ver=%{log_ver};;
mailer) ver=%{mailer_ver};;
page) ver=%{page_ver};;
random) ver=%{random_ver};;
rdc) ver=%{rdc_ver};;
regexp) ver=%{regexp_ver};;
request) ver=%{request_ver};;
response) ver=%{response_ver};;
scrape) ver=%{scrape_ver};;
session) ver=%{session_ver};;
string) ver=%{string_ver};;
xtags) ver=%{xtags_ver};;
esac
cp -p dist/$tl/taglibs-${tl}.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-taglibs-${tl}-${ver}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${tl}-${ver}
cp -pr build/${tl}/${tl}-doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${tl}-${ver}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/${tl}-${ver}
cp -p build/${tl}/${tl}-doc/*.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/${tl}-${ver}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/${tl}-${ver}
cp -p dist/${tl}/${tl}-doc.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/${tl}-${ver}
cp -p dist/${tl}/${tl}-examples.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/${tl}-${ver}
cp -p LICENSE $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/${tl}-${ver}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *${tl}-${ver}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *${tl}-${ver}*; do ln -sf ${jar} `echo $jar| sed "s|-${ver}||g"`; done)
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-application.pom
%add_to_maven_depmap taglibs application %{application_ver} JPP jakarta-taglibs-application
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-benchmark.pom
%add_to_maven_depmap taglibs benchmark %{benchmark_ver} JPP jakarta-taglibs-benchmark
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-bsf.pom
%add_to_maven_depmap taglibs bsf %{bsf_ver} JPP jakarta-taglibs-bsf
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-cache.pom
%add_to_maven_depmap taglibs cache %{cache_ver} JPP jakarta-taglibs-cache
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-datetime.pom
%add_to_maven_depmap taglibs datetime %{datetime_ver} JPP jakarta-taglibs-datetime
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-dbtags.pom
%add_to_maven_depmap taglibs dbtags %{dbtags_ver} JPP jakarta-taglibs-dbtags
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-i18n.pom
%add_to_maven_depmap taglibs i18n %{i18n_ver} JPP jakarta-taglibs-i18n
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-input.pom
%add_to_maven_depmap taglibs input %{input_ver} JPP jakarta-taglibs-input
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-io.pom
%add_to_maven_depmap taglibs io %{io_ver} JPP jakarta-taglibs-io
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-jmstags.pom
%add_to_maven_depmap taglibs jmstags %{jmstags_ver} JPP jakarta-taglibs-jmstags
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-jndi.pom
%add_to_maven_depmap taglibs jndi %{jndi_ver} JPP jakarta-taglibs-jndi
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-log.pom
%add_to_maven_depmap taglibs log %{log_ver} JPP jakarta-taglibs-log
install -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-mailer.pom
%add_to_maven_depmap taglibs mailer %{mailer_ver} JPP jakarta-taglibs-mailer
install -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-page.pom
%add_to_maven_depmap taglibs page %{page_ver} JPP jakarta-taglibs-page
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-random.pom
%add_to_maven_depmap taglibs random %{random_ver} JPP jakarta-taglibs-random
install -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-rdc.pom
%add_to_maven_depmap taglibs rdc %{rdc_ver} JPP jakarta-taglibs-rdc
install -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-regexp.pom
%add_to_maven_depmap taglibs regexp %{regexp_ver} JPP jakarta-taglibs-regexp
install -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-request.pom
%add_to_maven_depmap taglibs request %{request_ver} JPP jakarta-taglibs-request
install -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-response.pom
%add_to_maven_depmap taglibs response %{response_ver} JPP jakarta-taglibs-response
install -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-scrape.pom
%add_to_maven_depmap taglibs scrape %{scrape_ver} JPP jakarta-taglibs-scrape
install -m 644 %{SOURCE21} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-session.pom
%add_to_maven_depmap taglibs session %{session_ver} JPP jakarta-taglibs-session
install -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-string.pom
%add_to_maven_depmap taglibs string %{string_ver} JPP jakarta-taglibs-string
install -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jakarta-taglibs-xtags.pom
%add_to_maven_depmap taglibs xtags %{xtags_ver} JPP jakarta-taglibs-xtags


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files poms
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}

%files application
%doc %{_datadir}/%{name}-%{version}/application-%{application_ver}/LICENSE
%{_javadir}/*application*.jar

%files benchmark
%doc %{_datadir}/%{name}-%{version}/benchmark-%{benchmark_ver}/LICENSE
%{_javadir}/*benchmark*.jar

%files bsf
%doc %{_datadir}/%{name}-%{version}/bsf-%{bsf_ver}/LICENSE
%{_javadir}/*bsf*.jar

%files cache
%doc %{_datadir}/%{name}-%{version}/cache-%{cache_ver}/LICENSE
%{_javadir}/*cache*.jar

%files datetime
%doc %{_datadir}/%{name}-%{version}/datetime-%{datetime_ver}/LICENSE
%{_javadir}/*datetime*.jar

%files dbtags
%doc %{_datadir}/%{name}-%{version}/dbtags-%{dbtags_ver}/LICENSE
%{_javadir}/*dbtags*.jar

%files i18n
%doc %{_datadir}/%{name}-%{version}/i18n-%{i18n_ver}/LICENSE
%{_javadir}/*i18n*.jar

%files input
%doc %{_datadir}/%{name}-%{version}/input-%{input_ver}/LICENSE
%{_javadir}/*input*.jar

%files io
%doc %{_datadir}/%{name}-%{version}/io-%{io_ver}/LICENSE
%{_javadir}/*io*.jar

%files jmstags
%doc %{_datadir}/%{name}-%{version}/jmstags-%{jmstags_ver}/LICENSE
%{_javadir}/*jmstags*.jar

%files jndi
%doc %{_datadir}/%{name}-%{version}/jndi-%{jndi_ver}/LICENSE
%{_javadir}/*jndi*.jar

%files log
%doc %{_datadir}/%{name}-%{version}/log-%{log_ver}/LICENSE
%{_javadir}/*log*.jar

%files mailer
%doc %{_datadir}/%{name}-%{version}/mailer-%{mailer_ver}/LICENSE
%{_javadir}/*mailer*.jar

%files page
%doc %{_datadir}/%{name}-%{version}/page-%{page_ver}/LICENSE
%{_javadir}/*page*.jar

%files random
%doc %{_datadir}/%{name}-%{version}/random-%{random_ver}/LICENSE
%{_javadir}/*random*.jar

%files rdc
%doc %{_datadir}/%{name}-%{version}/rdc-%{rdc_ver}/LICENSE
%{_javadir}/*rdc*.jar

%files regexp
%doc %{_datadir}/%{name}-%{version}/regexp-%{regexp_ver}/LICENSE
%{_javadir}/*regexp*.jar

%files request
%doc %{_datadir}/%{name}-%{version}/request-%{request_ver}/LICENSE
%{_javadir}/*request*.jar

%files response
%doc %{_datadir}/%{name}-%{version}/response-%{response_ver}/LICENSE
%{_javadir}/*response*.jar

%files scrape
%doc %{_datadir}/%{name}-%{version}/scrape-%{scrape_ver}/LICENSE
%{_javadir}/*scrape*.jar

%files session
%doc %{_datadir}/%{name}-%{version}/session-%{session_ver}/LICENSE
%{_javadir}/*session*.jar

%files string
%doc %{_datadir}/%{name}-%{version}/string-%{string_ver}/LICENSE
%{_javadir}/*string*.jar

%files xtags
%doc %{_datadir}/%{name}-%{version}/xtags-%{xtags_ver}/LICENSE
%{_javadir}/*xtags*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt3_0.20050928.4jpp5
- build with ant17

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_0.20050928.4jpp5
- selected java5 compiler explicitly

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_0.20050928.4jpp5
- new jpp release

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_0.20050928.3jpp5
- converted from JPackage by jppimport script

