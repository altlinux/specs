Name:           zip4j
Version:        2.11.6
Release:        alt1

Summary:        A Java library for zip files and streams
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/srikanth-lingala/zip4j
VCS:            https://github.com/srikanth-lingala/zip4j

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch

%description
Zip4j is the most comprehensive Java library for zip files or streams. As of
this writing, it is the only Java library which has support for zip encryption,
apart from several other features. It tries to make handling zip files/streams
a lot more easier. No more clunky boiler plate code with input streams and
output streams. As you can see in the usage section below, working with zip
files can now even be a single line of code, compared to this. I mean no offense
to the Java's built-in zip support. In fact, this library depends on Java's
built-in zip code and it would have been significantly more complicated
challenging if I had to write compression logic as well. But lets be honest,
working with zip files or streams can be a lot of boiler plate code. The main
goal of this library is to provide a simple API for all usual actions of a zip
file or streams by doing the heavy lifting within the library and not have
developers worry about having to deal with streams, etc.

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin

%build
# tests disabled cause missing powermock (gradle)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%changelog
* Thu Apr 16 2026 Evgeniy Serov <scala@altlinux.org> 2.11.6-alt1
- Initial build for Sisyphus.
