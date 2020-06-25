# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(MRO/Compat.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(SQL/Abstract.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/Deep.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Warn.pm) perl(Text/Balanced.pm) perl(YAML/Tiny.pm)
# END SourceDeps(oneline)
%define module_name SQL-Abstract-Classic
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.91
Release: alt2
Summary: Generate SQL from Perl data structures
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RI/RIBASUSHI/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module was inspired by the excellent the DBIx::Abstract manpage.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

While based on the concepts used by the DBIx::Abstract manpage, there are
several important differences, especially when it comes to WHERE
clauses. I have modified the concepts used to make the SQL easier
to generate from Perl data structures and, IMO, more intuitive.
The underlying idea is for this module to do what you mean, based
on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes,
as this module figures it out.

To begin with, an SQL INSERT is as easy as just specifying a hash
of `key=value' pairs:

    my %%data = (
        name => 'Jimbo Bobson',
        phone => '123-456-7890',
        address => '42 Sister Lane',
        city => 'St. Louis',
        state => 'Louisiana',
    );

The SQL can then be generated with this:

    my($stmt, @bind) = $sql->insert('people', \%%data);

Which would give you something like this:

    $stmt = "INSERT INTO people
                    (address, city, name, phone, state)
                    VALUES (?, ?, ?, ?, ?)";
    @bind = ('42 Sister Lane', 'St. Louis', 'Jimbo Bobson',
             '123-456-7890', 'Louisiana');

These are then used directly in your DBI code:

    my $sth = $dbh->prepare($stmt);
    $sth->execute(@bind);

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/S*

%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.91-alt2
- to Sisyphus as perl-DBIx-Class dep

* Sun Oct 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.91-alt1
- initial import by package builder

