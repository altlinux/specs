Name: jai
Version: 1.1.3
Release: alt1

%define distversion	1_1_3
%define doc_distversion	1_1
%define arch i586

Summary: Java Advanced Imaging API
Group: Development/Java
License: Sun Binary Code License
Url: http://java.sun.com/products/java-media/jai/

%def_without javadoc

%define javadir		%_datadir/java
%define javadocdir	%_datadir/javadoc

Source0: %name-%distversion-lib-linux-amd64.tar.gz
Source1: %name-%distversion-lib-linux-i586.tar.gz

%if_with javadoc
Source1: %name-%doc_distversion-mr-doc.zip
%endif

ExclusiveArch: %ix86 x86_64

%set_verify_elf_method textrel=relaxed

%description
The JavaTM Advanced Imaging application programming interface (API)
enables developers to easily incorporate high-performance,
network-enabled, scalable, platform-independent image processing into
Java technology-based applications and applets.

%package javadoc
Summary: Javadoc for %name
Group: Development/Documentation

%description javadoc
Javadoc for %name

%prep
%ifarch x86_64
%setup -q -n %name-%distversion
%else
%setup -q -n %name-%distversion -T -b 1
%endif
chmod 0644 *.txt

%if_with javadoc
%setup -q -n %name-%distversion -D -T -a 1
%endif

%install
# jars
install -d -m 0755           $RPM_BUILD_ROOT%javadir/%name
install -p -m 0644 lib/*.jar $RPM_BUILD_ROOT%javadir/%name

# libs
mkdir -p                     $RPM_BUILD_ROOT%_libdir
install -p -m 0755 lib/*.so  $RPM_BUILD_ROOT%_libdir

# javadoc
%if_with javadoc
install -d -m 0755	     $RPM_BUILD_ROOT%javadocdir/%name
cp -pr %name-apidocs/*     $RPM_BUILD_ROOT%javadocdir/%name
%endif

%files
%doc *.txt
%javadir/%name
%_libdir/*.so

%if_with javadoc
%files javadoc
%doc %javadocdir/%name
%endif

%changelog
* Sat Feb 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.1.3-alt1
- New version

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt1
- Ported to Sisyphus from the JPackage project
