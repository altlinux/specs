Name: perlconsole
Version: 0.4
Release: alt1
Summary: Light program that lets you evaluate Perl code interactively
License: GPLv2+
Group: Development/Perl
URL: http://sukria.net/%name.html
Source: http://search.cpan.org/CPAN/authors/id/S/SU/SUKRIA/%name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildPreReq: rpm-build-perl
BuildRequires: perl-devel %_bindir/pod2man
BuildRequires: perl(Getopt/Long.pm) perl(B/Keywords.pm) perl(Lexical/Persistence.pm) perl(Module/Refresh.pm) perl(Term/ReadLine.pm)

%description
Perl Console is a light program that lets you evaluate Perl code interactively.
It uses Readline for grabing input and provides completion with all
the namespaces loaded during your session.
This is pretty useful for Perl developers that write modules. You can load
a module in your session and test a function exported by the module.


%prep
%setup -q
%patch -p1


%build
%__perl Makefile.PL PREFIX=%_prefix INSTALLDIRS=vendor INSTALLMAN
%make_build
pod2man -s 1 %name{,.man}


%install
%makeinstall_std
install -pD -m 0644 %name.man %buildroot%_man1dir/%name.1


%check
%make_build test


%files
%doc AUTHORS CHANGES README
%_bindir/*
%perl_vendor_privlib/*
%_man1dir/*
%exclude %_libdir


%changelog
* Fri Apr 04 2014 Led <led@altlinux.ru> 0.4-alt1
- initial build
