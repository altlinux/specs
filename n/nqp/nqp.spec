Name: nqp
Version: 2016.02
Release: alt1
Summary: Not Quite Perl

Group: Development/Other
License: Artistic 2
URL: https://github.com/perl6/nqp

# Cloned from https://github.com/perl6/nqp
Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: moarvm libmoarvm-devel perl-devel

BuildArch: noarch

%description
This is "Not Quite Perl" -- a lightweight Perl 6-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, perl6 or Rakudo) and is focused on being a
high-level way to create compilers and libraries for virtual machines (such as
the Parrot Virtual Machine [1], the JVM, and MoarVM [2]). Unlike a full-fledged
implementation of Perl 6, NQP strives to have as small a runtime footprint as
it can, while still providing a Perl 6 object model and regular expression
engine for the virtual machine.

%package doc
Summary: Documentation and examples for NQP
Group: Documentation
BuildArch:  noarch

%description doc
%summary

%prep
%setup

%build
perl Configure.pl --prefix=%_prefix --backends=moar
%make_build

%install
%makeinstall_std

%files
%_bindir/nqp
%_bindir/nqp-m
%dir %_datadir/nqp
%dir %_datadir/nqp/lib
%_datadir/nqp/lib/*.moarvm
%dir %_datadir/nqp/lib/profiler
%_datadir/nqp/lib/profiler/template.html
%doc CREDITS LICENSE README.pod

%files doc
%doc docs examples

%changelog
* Mon Feb 22 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.02-alt1
- 2016.02

* Tue Feb 02 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.01-alt1
- 2016.01

* Fri Dec 25 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt1
- 2015.12

* Sun Nov 29 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.11-alt1
- 2015.11

* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build

