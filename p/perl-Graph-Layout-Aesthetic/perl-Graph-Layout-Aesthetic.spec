# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Config.pm) perl(Pod/Usage.pm) perl(Test/More.pm) perl(Tie/Array.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.12
%define module_name Graph-Layout-Aesthetic
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators unzip

Name: perl-%module_name
Version: 0.12
Release: alt1.gitcf5e428.1.1
Summary: A module for laying out graphs
Group: Development/Perl
License: perl
URL: https://github.com/pypt/p5-Graph-Layout-Aesthetic
#Url: %CPAN %module_name
#Latest commit cf5e428 on 16 Nov 2013 @pypt pypt (blindly) fix a couple of unit tests
Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TH/THOSPEL/%{module_name}-%{module_version}-git.zip

Requires: /usr/bin/gnuplot

%description
A Graph::Layout::Aesthetic object represents a state in the process of laying
out a graph. The idea is that the state is repeatedly modified until an
acceptable layout is reached. This is done by considering the current state
from the point of view of a number of aesthetic criteria, each of which will
provide a step along which it would like to change the current state. A
weighted average is then taken of all these steps, leading to a proposed step.
The size of this step is then limited using a decreasing parameter (the
temperature) and applied. Small random disturbances may also be applied to
avoid getting stuck in a subspace.

The package also comes with a simple commandline tool gloss.pl
(based on this package) that allows you to lay out graphs.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name
%prep
%setup -q -n p5-%{module_name}-master

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/G*
%perl_vendor_autolib/*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.gitcf5e428.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.gitcf5e428.1
- rebuild with new perl 5.24.1

* Sun Apr 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.gitcf5e428
- initial import by package builder

