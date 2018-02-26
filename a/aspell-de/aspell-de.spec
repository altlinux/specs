%define aspell_ver 0.60
%define ispell_ver 3.20
%define lang_ver 20040515
Name: aspell-de
Version: %aspell_ver
Release: alt2

Packager: Igor Vlasenko <viy@altlinux.org>
Summary: GNU Aspell Word List Package  for German.
License: GPL
Group: System/Internationalization

Url: http://aspell.net/

Source: ftp://alpha.gnu.org/gnu/aspell/aspell-lang-%lang_ver.tar.bz2
Source2: aspell-de-alt.tar.bz2

Requires: aspell >= %aspell_ver
BuildRequires: perl, perl-Encode
BuildRequires: aspell >= %aspell_ver
Provides: aspell-dictionary

%description
This is the Aspell word list for German.

%prep
%setup -q -n aspell-lang
tar -j -p -xf %SOURCE2

%__cat >create_list <<EOF
 #!/bin/sh
export LANG=C; cat wordlist.txt | sort -u | word-list-compress c > de.cwl 
./proc
EOF

chmod 700 create_list
./create_list

%build
./configure
%make

%install
%make_install DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README Copyright
%_libdir/aspell/*
%_datadir/*

%changelog
* Thu Aug 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.60-alt2
- rebuild

* Fri Jul 23 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt1
- special nonofficial version for aspell 0.60

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt2
- fix depedencies

* Tue Sep 16 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt1
- New official package from aspell.net
