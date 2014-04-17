# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%global debug_package %nil

%global snobrel 1.5

Name: snobol
Version: 4.%snobrel
Release: alt2
Summary: The SNOBOL programming language

Group: Development/Other
License: BSD
Packager: Ilya Mashkin <oddity@altlinux.ru>

Url: http://www.snobol4.org
Source0: ftp://ftp.ultimate.com/%name/%{name}4-%snobrel.tar.gz
Patch1: snobol-4.1.4.1-makefile.patch
Patch2: snobol-4.1.4.1-doc.patch

BuildRequires: tcl-devel
BuildRequires: tk-devel >= 8.4
BuildRequires: gdbm-devel
BuildRequires: m4

Obsoletes: snobol-devel < 4.1.4.1
Provides: snobol-devel = %version-%release

Provides: snobol-devel = %version-%release
Obsoletes: snobol-devel < %version-%release
Source44: import.info

%description
SNOBOL4, while known primarily as a string language excels at any task
involving symbolic manipulations.  It provides run time typing,
garbage collection, user data types, on the fly compilation.  It's
primary weakness is it's simple syntax, and lack of "structured
programming" and "object oriented" constructs.

%prep
%setup -n %{name}4-%snobrel
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure  --prefix=%prefix --mandir=%_mandir \
             --snolibdir=%_datadir/snobol4 \
              --with-tcl=%_libdir/tclConfig.sh
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYRIGHT README CHANGES doc/load.txt
%_bindir/snobol*
%_bindir/sdb*
%_datadir/snobol4/
%_mandir/man*/*

%changelog
* Tue Apr 17 2014 Ilya Mashkin <oddity@altlinux.ru> 4.1.5-alt2
- Build for Sisyphus

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.5-alt1_4
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4.1-alt1_4
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4.1-alt1_3
- initial fc import

