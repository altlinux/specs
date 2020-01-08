%define _unpackaged_files_terminate_build 1
%define sname minion

Name: perl-Minion
Version: 10.02
Release: alt1
Summary: Job queue
License: Artistic-2.0
Group: Development/Perl
Url: http://search.cpan.org/dist/Minion/
Source0: http://www.cpan.org/authors/id/S/SR/SRI/Minion-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Mojo/Pg.pm)

Requires: perl(Mojolicious.pm)

%description
Minion is a high performance job queue for the Perl programming language,
with support for multiple named queues, priorities, delayed jobs, job
dependencies, job progress, job results, retries with backoff, rate
limiting, unique jobs, statistics, distributed workers, parallel
processing, autoscaling, remote control, at http://mojolicious.org admin
ui, resource leak protection and multiple backends (such as at
http://www.postgresql.org).
Job queues allow you to process time and/or computationally intensive tasks
in background processes, outside of the request/response lifecycle of web
applications. Among those tasks you'll commonly find image resizing, spam
filtering, HTTP downloads, building tarballs, warming caches and basically
everything else you can imagine that's not super fast.

%prep
%setup -q -n Minion-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md examples
%perl_vendorlib/Minion*
%perl_vendorlib/Mojolicious*
%doc README.md Changes

%changelog
* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 10.02-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 10.0-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 9.13-alt1
- automated CPAN update

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 9.12-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 9.11-alt1
- automated CPAN update

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 9.10-alt1
- automated CPAN update

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 9.09-alt1
- automated CPAN update

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 9.08-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 9.07-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 9.06-alt1
- automated CPAN update

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 9.05-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 9.03-alt1
- initial build for ALT
