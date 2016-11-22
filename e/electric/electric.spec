Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           electric
Version:        8.09
Release:        alt1_11jpp8
Summary:        Sophisticated ASIC and MEM CAD System

License:        GPLv3
URL:            http://www.staticfreesoft.com/

Source0:        ftp://ftp.gnu.org/pub/gnu/electric/%{name}-%{version}.jar
Source1:        %{name}.desktop
Source2:        %{name}.1

BuildRequires:  ant
BuildRequires:  desktop-file-utils


BuildArch:      noarch
Source44: import.info

%description
Electric is a sophisticated electrical CAD system that can handle
many forms of circuit design, including custom IC layout (ASICs),
schematic drawing, hardware description language specifications,
and electro-mechanical hybrid layout.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -T -c %{name}-%{version} -a 0

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

jar xf %{SOURCE0}

#wrong-file-end-of-line-encoding
sed -i 's/\r//' packaging/README.txt packaging/LicenseGNU.txt

%build
ant -verbose        \
    jarForGNUBinary \
    javadoc


%install
# generating empty directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_javadir}/%{name}

# real java binary created by this spec file
install -pm 0755 %{name}-%{version}.jar \
                 %{buildroot}%{_javadir}/%{name}/%{name}.jar


# dummy executable file to call %%{name}.jar
cat > %{name} << EOF
#!/bin/bash
java -jar %{_javadir}/%{name}/%{name}.jar
EOF
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# Man page
install -d %{buildroot}%{_mandir}/man1/
install -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

# desktop file and its icon
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
install -d %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 com/sun/electric/tool/user/help/helphtml/iconplug.png \
                 %{buildroot}%{_datadir}/pixmaps/%{name}.png


# javadoc API
install -d %{buildroot}%{_javadocdir}/%{name}
%{__cp} -rp apidoc/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc packaging/README.txt ChangeLog.txt packaging/LicenseGNU.txt
%{_bindir}/%{name}
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/%{name}.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1_6jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1_5jpp7
- new version

