Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Parser Generator with Java Extension
Name:		byaccj
Epoch:		0
Version:	1.15
Release:	alt1_19jpp8
License:	Public Domain
URL:		http://byaccj.sourceforge.net/

Source0:	http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz

BuildRequires:  gcc
Source44: import.info

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible 
parser generator. Standard YACC takes a YACC source file, and 
generates one or more C files from it, which if compiled properly, 
will produce a LALR-grammar parser. This is useful for expression 
parsing, interactive command parsing, and file reading. Many 
megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce 
C/C++ parsers. I have added a "-J" flag which will cause BYACC to 
generate Java source code, instead. So there finally is a YACC for 
Java now! 

%prep
%setup -q -n %{name}%{version}
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4||g' src/Makefile

%build
pushd src
make yacc CFLAGS="%{optflags}" LDFLAGS=""
popd

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_bindir}/%{name}

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_19jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_16jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_6jpp7
- new release

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_5jpp7
- new release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_5jpp5
- updated from fedora 13

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp5
- converted from JPackage by jppimport script

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_2jpp1.7
- converted from JPackage by jppimport script

