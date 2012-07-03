Name: jpcap
Version: 0.7
Release: alt4

Summary: A Java library for capturing and sending network packets
Summary(ru_RU.UTF8): Java библиотека для перехвата и отправки сетевых пакетов
License: LGPL
Group: Development/Java

Url: http://netresearch.ics.uci.edu/kfujii/jpcap/doc/
Packager: Rinat Bikov <becase@altlinux.org>


Source: %url/../%name-%version.tar.gz

BuildRequires(pre): /proc rpm-build-java
BuildRequires(pre): java-devel >= 1.6.0
BuildRequires(pre): jpackage-utils
BuildRequires(pre): ant junit
BuildRequires(pre): libpcap-devel >= 0.9
Requires: java >= 1.6
Requires: libpcap0.8 >= 0.9


%description
Jpcap is a Java library for capturing and sending network packets from Java applications.

This Jpcap package requires Sun's JDK 1.6 or higher,
and libpcap 0.9 or higher.

%description -l ru_RU.UTF8
Jpcap - это библиотека Java для захвата и отправки сетевых пакетов из Java-приложения.
Для выполнения своих функций использует библиотеку libpcap.

%package javadoc
Summary: API documentation for %{name}
Summary(ru_RU.UTF8): API документация для %{name}
Group: Development/Java
Requires: java-common
BuildArch: noarch


%description javadoc
Javadoc for %{name}
%description javadoc -l ru_RU.UTF8
Javadoc для %{name}

%prep
%setup -q
sed -i "s/-shared/-shared -fPIC/g" src/c/Makefile 
sed -i "1i #include<malloc.h>" src/c/JpcapWriter.c 

%build
cd src/c
%make clean
%make
cd ../..
mkdir bin
%ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar
%ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 javadoc

%install
install -d $RPM_BUILD_ROOT
install -pD -m 644  lib/%name.jar $RPM_BUILD_ROOT%{_javadir}/%name-%version.jar
ln -sf %name-%version.jar $RPM_BUILD_ROOT%{_javadir}/%name.jar
install -pD -m 644 src/c/lib%{name}.so $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.%{version}
ln -sf lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

#mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}/
cp -pr doc/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}/

%files
%defattr(0644,root,root,0755)
%doc README COPYING ChangeLog
%{_javadir}/*
%{_libdir}/lib%{name}.so*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}

%changelog
* Mon Feb 7 2011 Rinat Bikov <becase@altlinux.org> 0.7-alt4
- Fixed build with debug info

* Tue Jul 13 2010 Rinat Bikov <becase@altlinux.org> 0.7-alt3
- Spec leanup

* Mon Jun 21 2010 Rinat Bikov <becase@altlinux.org> 0.7-alt2
- Javadoc package created (closes: #22608)

* Tue Dec 8 2009 Rinat Bikov <becase@altlinux.org> 0.7-alt1
- Initial build
