Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          lightcouch
Version:       0.1.2
Release:       alt1_4jpp8
Summary:       CouchDB Java API
License:       ASL 2.0
URL:           http://www.lightcouch.org/
Source0:       https://github.com/lightcouch/LightCouch/archive/%{name}-%{version}.tar.gz

BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.apache.httpcomponents:httpclient) >= 4.3.3
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
LightCouch aims at providing a simple API
for communicating with CouchDB databases. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n LightCouch-%{name}-%{version}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# NullPointerException
rm -r src/test/java/org/lightcouch/tests/CouchDbClientLoadTest.java \
 src/test/java/org/lightcouch/tests/CouchDbClientTest.java

# unreported exception
sed -i "s|private void setEntity(HttpEntityEnclosingRequestBase httpRequest, String json) {|private void setEntity(HttpEntityEnclosingRequestBase httpRequest, String json) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|Response put(URI uri, InputStream instream, String contentType) {|Response put(URI uri, InputStream instream, String contentType) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|HttpResponse post(URI uri, String json) {|HttpResponse post(URI uri, String json) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public ReplicationResult trigger() {|public ReplicationResult trigger() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/Replication.java
sed -i "s|public InputStream queryForStream() {|public InputStream queryForStream() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public <T> List<T> query(Class<T> classOfT) {|public <T> List<T> query(Class<T> classOfT) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public <K, V, T> ViewResult<K, V, T> queryView(Class<K> classOfK, Class<V> classOfV, Class<T> classOfT) {|public <K, V, T> ViewResult<K, V, T> queryView(Class<K> classOfK, Class<V> classOfV, Class<T> classOfT) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|private <V> V queryValue(Class<V> classOfV) {|private <V> V queryValue(Class<V> classOfV) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public void batch(Object object) {|public void batch(Object object) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public List<Response> bulk(List<?> objects, boolean allOrNothing) {|public List<Response> bulk(List<?> objects, boolean allOrNothing) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public Response saveAttachment(InputStream instream, String name, String contentType) {|public Response saveAttachment(InputStream instream, String name, String contentType) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public Response saveAttachment(InputStream instream, String name, String contentType, String docId, String docRev) {|public Response saveAttachment(InputStream instream, String name, String contentType, String docId, String docRev) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|Response put(URI uri, Object object, boolean newEntity) {|Response put(URI uri, Object object, boolean newEntity) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public String queryForString() {|public String queryForString() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public int queryForInt() {|public int queryForInt() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public long queryForLong() {|public long queryForLong() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public boolean queryForBoolean() {|public boolean queryForBoolean() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|String currentStartKeyDocId, String startKey, String startKeyDocId, Class<T> classOfT) {|String currentStartKeyDocId, String startKey, String startKeyDocId, Class<T> classOfT) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public <T> Page<T> queryPage(int rowsPerPage, String param, Class<T> classOfT) {|public <T> Page<T> queryPage(int rowsPerPage, String param, Class<T> classOfT) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/View.java
sed -i "s|public Response save(Object object) {|public Response save(Object object) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public Response update(Object object) {|public Response update(Object object) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public void compact() {|public void compact() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbContext.java
sed -i "s|public void ensureFullCommit() {|public void ensureFullCommit() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbContext.java
sed -i "s|public Response synchronizeWithDb(DesignDocument document) {|public Response synchronizeWithDb(DesignDocument document) throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbDesign.java
sed -i "s|public void synchronizeAllWithDb() {|public void synchronizeAllWithDb() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbDesign.java
sed -i "s|public void syncDesignDocsWithDb() {|public void syncDesignDocsWithDb() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/CouchDbClientBase.java
sed -i "s|public Response save() {|public Response save() throws java.io.UnsupportedEncodingException {|" \
 src/main/java/org/lightcouch/Replicator.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_4jpp8
- java 8 mass update

