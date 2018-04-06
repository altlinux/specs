Name:    shc
Version: 3.9.6
Release: alt1
Summary: Shell Script Compiler

Group:   System/Libraries
License: GPLv3
URL:     https://github.com/neurobin/shc

# Source0-url: https://github.com/neurobin/shc/archive/3.9.6.tar.gz
Source0: %name-%version.tar

BuildRequires: gcc

%description
A generic shell script compiler. 
Shc takes a script, which is specified on the command line and produces C source code. 
The generated source code is then compiled and linked to produce a stripped binary executable.

%prep
%setup -q

%build
# %%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/*
%_man1dir/*

%changelog
* Fri Apr 06 2018 Pavel Vainerman <pv@altlinux.ru> 3.9.6-alt1
- new version (3.9.6) with rpmgs script

* Thu Mar 11 2014 Ilya Mashkin <oddity at altlinux.ru> 3.8.9-alt1
- 3.8.9 (Closes: #25694)

* Wed Oct 22 2008 Ilya Mashkin <oddity at altlinux.ru> 3.8.6-alt1
- 3.8.6

* Mon Jul 18 2005 Alex Yustasov <yust at altlinux.ru> 3.8.3-alt1
- 3.8.3

* Wed Jan 26 2005 Alex Yustasov <yust at altlinux.ru> 3.7-alt1
- initial release
