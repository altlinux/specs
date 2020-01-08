%define _unpackaged_files_terminate_build 1
Name: perl-Filesys-Notify-Simple
Version: 0.14
Release: alt1

Summary: Filesys::Notify::Simple - Simple and dumb file system watcher
Group: Development/Perl
License: Perl
Url: %CPAN Filesys-Notify-Simple

# Cloned from git://github.com/miyagawa/Filesys-Notify-Simple.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: perl-devel perl-Test-SharedFork perl-Module-Install perl-Module-Install-Repository perl-Module-Install-ReadmeFromPod perl-Module-Install-AuthorTests perl-Test-Base
Requires: perl-Linux-Inotify2

%description
Filesys::Notify::Simple is a simple but unified interface to get
notifications of changes to a given filesystem path. It utilizes
inotify2 on Linux and fsevents on OS X if they're installed, with
a fallback to the full directory scan if they're not available.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes
%perl_vendor_privlib/Filesys/Notify/Simple*
%doc Changes

%changelog
* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new version

* Fri Mar 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- New version 0.08
- Added strict dependency on perl-Linux-Inotify2
- Source cloned from upstream git

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- New version 0.07

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build
