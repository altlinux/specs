Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

Summary:	Parser Generator with Java Extension
Name:		byaccj
Version:	1.14
Release:	alt1_5jpp5
Epoch:		0
License:	Public Domain
URL:		http://byaccj.sourceforge.net/
Group:		Development/Java
Source0:	http://downloads.sourceforge.net/%{name}/%{name}%{version}_src.tar.gz
Requires: man-pages

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
%setup -q -n %{name}%{version}_src

%build
pushd src
make linux CFLAGS="%{optflags}"
popd

sed -i 's/\r//g' docs/tf.y

%install

# manual
install -d -m 755 %{buildroot}%{_mandir}/man1
mv docs/yacc.cat %{buildroot}%{_mandir}/man1

# jars
mkdir -p %{buildroot}%{_bindir}
cp -p src/yacc.linux \
  %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -p docs/* %{buildroot}%{_docdir}/%{name}-%{version}
cp -p src/readme %{buildroot}%{_docdir}/%{name}-%{version}
cp -p src/README %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man1/yacc.cat*
%attr(755, root, root) %{_bindir}/%{name}


%changelog
* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_5jpp5
- updated from fedora 13

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp5
- converted from JPackage by jppimport script

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_2jpp1.7
- converted from JPackage by jppimport script

