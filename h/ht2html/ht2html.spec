Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
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


Name:		ht2html
Version:	2.0
Release:	alt4_2jpp5.1
URL:		http://ht2html.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.bz2
License:	Public Domain
Group:		System/Libraries
Summary:	The www.python.org Web site generator
BuildRequires: python-devel
BuildArch:	noarch
Patch33: ht2html-2.0-alt-fix-whrandom.patch

%description
The www.python.org Web site generator.

%prep
%setup -q
bzcat %{SOURCE1} > %{name}
%patch33 -p1

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 calcroot.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 ht2html.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 BAWGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Banner.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 HTParser.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 IPC8Generator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 JPyGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 JPyLocalGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 LinkFixer.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 PDOGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 SelfGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Sidebar.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Skeleton.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 StandardGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc README doc/*.{html,png}
%{_datadir}/%{name}
%{_bindir}/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt4_2jpp5.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.0-alt4_2jpp5
- removed jpackage-1.5-compat dependency

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3_2jpp5.1
- Rebuilt with python 2.6

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_2jpp5
- converted from JPackage by jppimport script

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_2jpp1.7
- fixed jpackage release

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0-alt1_2jpp1.7.1
- Rebuilt with python-2.5.

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

