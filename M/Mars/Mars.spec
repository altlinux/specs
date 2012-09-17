BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           Mars
Version:        4.1
Release:        alt1_5jpp7
Summary:        An interactive development environment for programming in MIPS assembly language

Group:          Development/Java
License:        MIT
URL:            http://courses.missouristate.edu/KenVollmar/MARS/
Source0:        http://courses.missouristate.edu/KenVollmar/MARS/MARS_4_1_Jan_2011/Mars_4_1.jar
Source1:        Mars
Source2:        Mars.desktop
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Source44: import.info

%description
MARS is a lightweight interactive development environment (IDE) for
programming in MIPS assembly language, intended for educational-level
use with Patterson and Hennessy's Computer Organization and Design.

%prep
%setup -q -c Mars-%{version}

find -name '*.class' -exec rm -f '{}' \;

%build
sed -i 's/\r//' MARSlicense.txt

cat << EOF > META-INF/MANIFEST.MF
Manifest-Version: 1.0
Main-Class: Mars
EOF

find . -name "*.java" -exec javac '{}' \;
jar cmf META-INF/MANIFEST.MF Mars.jar PseudoOps.txt Config.properties Syscall.properties Settings.properties MARSlicense.txt mainclass.txt CreateMarsJar.bat Mars.java Mars.class docs help images mars

%install
install -Dpm 644 Mars.jar ${RPM_BUILD_ROOT}%{_javadir}/Mars.jar
install -Dpm 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}/Mars
desktop-file-install                                \
    --add-category="Development"                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}

%files
%{_javadir}/*
%{_bindir}/*
%{_datadir}/applications/Mars.desktop
%doc MARSlicense.txt

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_5jpp7
- new version

