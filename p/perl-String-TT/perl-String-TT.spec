%define module_version 0.03
%define module_name String-TT
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(PadWalker.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Sub/Exporter.pm) perl(Template.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/TableDriven.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(ok.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: use TT to interpolate lexical variables
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/B/BO/BOBTFISH/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
String::TT exports a `tt' function, which takes a TT
(Template Toolkit) template as its argument.  It uses the
current lexical scope to resolve variable references.  So if you say:

  my $foo = 42;
  my $bar = 24;

  tt '[%% foo %%] <-> [%% bar %%]';

the result will be `42 <-> 24'.

TT provides a slightly less rich namespace for variables than perl, so
we have to do some mapping.  Arrays are always translated from
`@array' to `array_a' and hashes are always translated from `%%hash'
to `hash_h'.  Scalars are special and retain their original name, but
they also get a `scalar_s' alias.  Here's an example:

  my $scalar = 'scalar';
  my @array  = qw/array goes here/;
  my %%hash   = ( hashes => 'are fun' );

  tt '[%% scalar %%] [%% scalar_s %%] [%% array_a %%] [%% hash_h %%]';

There is one special case, and that's when you have a scalar that is
named like an existing array or hash's alias:

  my $foo_a = 'foo_a';
  my @foo   = qw/foo array/;

  tt '[%% foo_a %%] [%% foo_a_s %%]'; # foo_a is the array, foo_a_s is the scalar

In this case, the `foo_a' accessor for the `foo_a' scalar will not
be generated.  You will have to access it via `foo_a_s'.  If you
delete the array, though, then `foo_a' will refer to the scalar.

This is a very cornery case that you should never encounter unless you
are weird.  99%% of the time you will just use the variable name.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

