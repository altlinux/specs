%define _unpackaged_files_terminate_build 1
%define sname SVN-Look

Name:  perl-SVN-Look
Version: 0.43
Release: alt1
Summary: Caching wrapper around the svnlook command
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/SVN-Look
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(List/MoreUtils.pm) perl(URI/file.pm) perl(XML/Simple.pm)
BuildRequires: subversion subversion-server-common

%description
The svnlook command is the workhorse of Subversion hook scripts, being used
to gather all sorts of information about a repository, its revisions, and
its transactions. This module provides a simple object oriented interface
to a specific svnlook invocation, to make it easier to hook writers to get
and use the information they need. Moreover, all the information gathered
by calling the svnlook command is cached in the object, avoiding
repetitious calls.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*

%changelog
* Thu May 26 2022 Alexandr Antonov <aas@altlinux.org> 0.43-alt1
- initial build for ALT

