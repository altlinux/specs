%define _unpackaged_files_terminate_build 1
%define module_name Data-Printer
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(B/Deparse.pm) perl(Capture/Tiny.pm) perl(Carp.pm) perl(Clone/PP.pm) perl(DBIx/Class/Core.pm) perl(DBIx/Class/Schema.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/HomeDir.pm) perl(File/HomeDir/Test.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(MRO/Compat.pm) perl(Package/Stash.pm) perl(Scalar/Util.pm) perl(Sort/Naturally.pm) perl(Term/ANSIColor.pm) perl(Test/More.pm) perl(base.pm) perl(if.pm) perl(mro.pm) perl(version.pm) perl(charnames.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001000
Release: alt1
Summary: colored pretty-print of Perl data structures and objects
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/G/GA/GARU/%{module_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl(DBD/DBM.pm)

%description
Want to see what's inside a variable in a complete, colored
and human-friendly way?

  use Data::Printer;   # or just "use DDP" for short
  
  p @array;            # no need to pass references

Code above might output something like this (with colors!):

   [
       [0] "a",
       [1] "b",
       [2] undef,
       [3] "c",
   ]

You can also inspect objects:

    my $obj = SomeClass->new;

    p($obj);

Which might give you something like:

  \ SomeClass  {
      Parents       Moose::Object
      Linear @ISA   SomeClass, Moose::Object
      public methods (3) : bar, foo, meta
      private methods (0)
      internals: {
         _something => 42,
      }
  }

Data::Printer is fully customizable. If you want to change how things
are displayed, or even its standard behavior. Take a look at the
available customizations. Once you figure out
your own preferences, create a
configuration file for
yourself and Data::Printer will automatically use it!

That's about it! Feel free to stop reading now and start dumping
your data structures! For more information, including feature set,
how to create filters, and general tips, just keep reading :)

Oh, if you are just experimenting and/or don't want to use a
configuration file, you can set all options during initialization,
including coloring, identation and filters!

  use Data::Printer {
      color => {
         'regex' => 'blue',
         'hash'  => 'yellow',
      },
      filters => {
         'DateTime' => sub { $_[0]->ymd },
         'SCALAR'   => sub { "oh noes, I found a scalar! $_[0]" },
      },
  };

The first `{}' block is just syntax sugar, you can safely ommit it
if it makes things easier to read:

  use DDP colored => 1;

  use Data::Printer  deparse => 1, sort_keys => 0;



%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README* examples CONTRIBUTING.md
%perl_vendor_privlib/D*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.001000-alt1
- automated CPAN update

* Fri Mar 05 2021 Igor Vlasenko <viy@altlinux.org> 1.000004-alt1
- automated CPAN update

* Wed Mar 03 2021 Igor Vlasenko <viy@altlinux.org> 1.000003-alt1
- automated CPAN update

* Thu Feb 25 2021 Igor Vlasenko <viy@altlinux.org> 1.000001-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- initial import by package builder

