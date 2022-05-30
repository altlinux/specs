%define _unpackaged_files_terminate_build 1

Name:           perl-Mason-Tidy
Version:        2.57
Release:        alt1
Summary:        Tidy HTML::Mason/Mason components
License:        GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url:            https://metacpan.org/dist/Mason-Tidy
Source: %name-%version.tar
BuildArch:      noarch

BuildRequires: perl(Capture/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(Method/Signatures/Simple.pm) perl(Moo.pm) perl(Perl/Tidy.pm) perl(Pod/Simple/Search.pm) perl(IPC/System/Simple.pm) perl(Test/Class/Most.pm) perl(Test/Most.pm) perl(Pod/Man.pm) perl(Test/More.pm) perl(Getopt/Long.pm) perl(File/Temp.pm)

%description
Mason::Tidy is the engine used by masontidy. You can call this API from
your own program instead of executing masontidy.
masontidy tidies Mason 1 and Mason 2 components, using perltidy to format
the Perl code that can be embedded in various places in the component.
masontidy does not (yet) attempt to tidy the HTML or other non-Perl content
in a component.

%prep
%setup

%build
#corrected inserting semicolons after a last
#statement of a block. That break Mason-Tidy CLI.t tests like this.
sed -i -e 's,argv        => $self->perltidy_line_argv . " -fnl -fbl",argv        => $self->perltidy_line_argv . " -fnl -fbl -nasc ",g' lib/Mason/Tidy.pm
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*
%_bindir/masontidy
%_man1dir/masontidy.1*

%changelog
* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 2.57-alt1
- initial build for ALT
