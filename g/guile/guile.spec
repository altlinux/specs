Name: guile
Version: 2.2
Release: alt2

%define defver 22

Summary: GNU implementation of Scheme
License: None
Group: System/Configuration/Other
BuildArch: noarch

Provides: /usr/bin/guile

%package devel
Summary: A Guile development package
Group:  Development/Scheme
Requires: %name = %version-%release
Provides: /usr/bin/guild
Provides: /usr/bin/guile-config

%description
This package provides the default %summary.

%description devel
This package provides the default %summary.

%install
mkdir -p %buildroot{%_bindir,%_rpmmacrosdir,%_man1dir}
cat > %buildroot%_rpmmacrosdir/guile << 'E_O_F'
%%guile_version %version
%%guile_ccachedir %%(guile-config info siteccachedir)
%%guile_extensiondir %%(guile-config info extensiondir)
E_O_F

ln -sr %buildroot%_bindir/guile%defver %buildroot%_bindir/guile
ln -sr %buildroot%_bindir/guild%defver %buildroot%_bindir/guild
ln -s  guild %buildroot%_bindir/guile-tools

ln -sr %buildroot%_bindir/guile%defver-config %buildroot%_bindir/guile-config
ln -sr %buildroot%_bindir/guile%defver-snarf %buildroot%_bindir/guile-snarf

ln -sr %buildroot%_man1dir/guile%defver.1.xz %buildroot%_man1dir/guile.1.xz

%set_compress_method none
%add_findreq_skiplist %_man1dir/*

%files
%_bindir/guile
%_man1dir/guile.1.xz

%files devel
%_bindir/guild
%_bindir/guile-config
%_bindir/guile-snarf
%_bindir/guile-tools
%_rpmmacrosdir/guile

%changelog
* Fri Aug 10 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt2
- provide guile-devel (closes: ##34496)

* Thu Aug 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- initial
