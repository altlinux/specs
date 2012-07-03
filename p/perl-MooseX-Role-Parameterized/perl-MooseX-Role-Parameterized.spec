%define dist MooseX-Role-Parameterized
Name: perl-%dist
Version: 0.27
Release: alt1

Summary: Roles with composition parameters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Module-Install perl-Moose perl-Test-Fatal

%description
Roles are composable units of behavior.  They are useful for factoring out
functionality common to many classes from any part of your class hierarchy.
See Moose::Cookbook::Roles::Recipe1 for an introduction to Moose::Role.

While combining roles affords you a great deal of flexibility, individual
roles have very little in the way of configurability.  Core Moose provides
-alias for renaming methods and -excludes for ignoring methods.  These
options are primarily for resolving role conflicts.  Depending on how much
of a purist you are, these options are solely for resolving role conflicts.
See Moose::Cookbook::Roles::Recipe2 for more about -alias and -excludes.

Because roles serve many different masters, they usually provide only the
least common denominator of functionality.  To empower roles further, more
configurability than -alias and -excludes is required.  Perhaps your role
needs to know which method to call when it is done processing.  Or what
default value to use for its url attribute.

Parameterized roles offer a solution to these (and other) kinds of problems.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/MooseX*

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- initial revision
