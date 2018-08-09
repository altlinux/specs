Name: guile
Version: 2.2
Release: alt1

%define defver 22

Summary: GNU implementation of Scheme
License: None
Group: System/Configuration/Other
BuildArch: noarch

Provides: /usr/bin/guile

%description
This package provides the default %summary.

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
ln -sr %buildroot%_bindir/guile%defver %buildroot%_bindir/guile
ln -sr %buildroot%_man1dir/guile%defver.1.xz %buildroot%_man1dir/guile.1.xz

%set_compress_method none
%add_findreq_skiplist %_man1dir/*

%files
%_bindir/guile
%_man1dir/guile.1.xz

%changelog
* Thu Aug 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- initial
