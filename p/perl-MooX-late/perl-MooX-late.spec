# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Moose.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Type/Utils.pm) perl(Types/Standard.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.015
%define module_name MooX-late
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.015
Release: alt1.1
Summary: easily translate Moose code to Moo
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/MooX-late

Source: http://www.cpan.org/authors/id/T/TO/TOBYINK/MooX-late-%{version}.tar.gz
BuildArch: noarch

%description
the Moo manpage is a light-weight object oriented programming framework which aims.to be compatible with the Moose manpage. It does this by detecting when Moose has
been loaded, and automatically "inflating" its classes and roles to full
Moose classes and roles. This way, Moo classes can consume Moose roles,
Moose classes can extend Moo classes, and so forth.

However, the surface syntax of Moo differs somewhat from Moose. For example
the `isa' option when defining attributes in Moose must be either a string
or a blessed the Moose::Meta::TypeConstraint manpage object; but in Moo must be a
coderef. These differences in surface syntax make porting code from Moose to
Moo potentially tricky. the MooX::late manpage provides some assistance by enabling a
slightly more Moosey surface syntax.

MooX::late does the following:

=over

=item 1.

Allows `isa => $string' to work when defining attributes for all
Moose's built-in type constraints (and assumes other strings are package
names).

This feature requires the Types::Standard manpage.

=item 2.

Retired feature: this is now built in to Moo.

Allows `default => $non_reference_value' to work when defining
attributes.

=item 3.

Allows `lazy_build => 1' to work when defining attributes.

=item 4.

Exports `blessed' and `confess' functions to your namespace.

=item 5.

Handles certain attribute traits. Currently `Hash', `Array' and `Code'
are supported. This feature requires the MooX::HandlesVia manpage. 

`String', `Number', `Counter' and `Bool' are unlikely to ever be
supported because of internal implementation details of Moo. If you need
another attribute trait to be supported, let me know and I will consider
it.

=item 6.

Supports `coerce => 1' if the type constraint is a blessed object
implementing the Type::API::Constraint::Coercible manpage.

=back

Five features. It is not the aim of `MooX::late' to make every aspect of
Moo behave exactly identically to Moose. It's just going after the low-hanging
fruit. So it does five things right now, and I promise that future versions
will never do more than seven.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README COPYRIGHT LICENSE Changes examples
%perl_vendor_privlib/M*

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1.1
- rebuild to restore role requires

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2
- moved to Sisyphus for perl update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- initial import by package builder

