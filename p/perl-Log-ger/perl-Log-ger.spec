%define _unpackaged_files_terminate_build 1
%define module_name Log-ger
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dmp.pm) perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(parent.pm) perl(strict.pm) perl(vars.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.025
Release: alt1
Summary: A lightweight, flexible logging framework
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Log-ger

Source0: http://www.cpan.org/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Log::ger is yet another logging framework with the following features:

=over

=item * Separation of producers and consumers/listeners

Like the Log::Any manpage, this offers a very easy way for modules to produce some logs
without having to configure anything. Configuring output, level, etc can be done
in the application as log consumers/listeners. To read more about this, see the
documentation of the Log::Any manpage or the Log::ger::Manual manpage (but nevertheless see
the Log::ger::Manual manpage on why you might prefer Log::ger to Log::Any).

=item * Lightweight and fast

Slim distribution. No non-core dependencies, extra functionalities are
provided in separate distributions to be pulled as needed.

Low startup overhead. Only ~0.5-1ms. For comparison, the strict manpage ~0.2-0.5ms,
the warnings manpage ~2ms, the Log::Any manpage 0.15 ~2-3ms, Log::Any 1.049 ~8-10ms,
the Log::Log4perl manpage ~35ms. This is measured on a 2014-2015 PC and before doing any
output configuration. For more benchmarks, see the Bencher::Scenarios::LogGer manpage or
try yourself e.g. with the bencher-code manpage:

 %% bencher-code 'use Log::ger' 'use Log::Any' --startup

Fast. Low null-/stealth-logging overhead, about 1.5x faster than Log::Any, 3x
faster than Log4perl, and 5x faster than the Log::Fast manpage.

Conditional compilation. There is a plugin to optimize away unneeded logging
statements, like assertion/conditional compilation, so they have zero runtime
performance cost. See the Log::ger::Plugin::OptAway manpage.

Being lightweight means the module can be used more universally, from CLI to
long-running daemons to inside routines with tight loops.

=item * Flexible

Customizable levels and routine/method names. Can be used in a procedural or
OO style. Log::ger can mimic the interface of the Log::Any manpage, the Log::Contextual manpage,
the Log::Log4perl manpage, or some other popular logging frameworks, to ease migration or
adjust with your personal style.

Per-package settings. Each importer package can use its own...
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/L*

%changelog
* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.023-alt2
- to Sisyphus

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- regenerated from template by package builder

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- initial import by package builder

