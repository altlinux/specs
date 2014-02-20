# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(Sys/Hostname.pm) perl(Test/More.pm) perl(Tk.pm) xvfb-run
# END SourceDeps(oneline)
%ifndef _build_display
%def_without test
%endif
%define module_version 1.000
%define module_name Language-Logo
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000
Release: alt2
Summary: An implementation of the Logo programming language
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JC/JCNORTON/LanguageLogo/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This module provides an implementation of the Logo programming language, with
all of the necessary drawing primitives in a Tk Canvas.  The Canvas object is
also referred to as the "screen".

The first construction of a Language::Logo object causes a server to be
created in a separate process; this server then creates a Tk GUI with a
Tk::Canvas for use by the client's "turtle", and responds to all requests
from the client's commands.  In this way, multiple clients may be constructed
simultaneously -- each one with its own "turtle".

In this first release, not all of the Logo language is implemented.
Rather, the primary commands available are those which directly affect
the turtle, and are related to drawing on the screen.  The intent is to
use the Logo in conjunction with Perl as a sort of "hybrid" language;
Perl us used as the higher-level language layer through which all loop
constructs, conditionals, and data-manipulation is done.  This allows
for a substantial level of programming power.




%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/L*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.000-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- initial import by package builder

