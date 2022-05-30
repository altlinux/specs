%define _unpackaged_files_terminate_build 1

Name:  perl-Pod-Tidy
Version: 0.10
Release: alt1
Summary: Reformatting Pod Processor
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Pod-Tidy
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(Module/Build.pm) perl(IO/String.pm) perl(Pod/Find.pm) perl(File/Basename.pm) perl(File/Copy.pm) perl(File/Spec.pm) perl(Getopt/Long.pm) perl(Pod/Usage.pm) perl(Pod/Simple.pm) perl(Text/Glob.pm) perl(Text/Wrap.pm) perl(Encode/Newlines.pm) perl(Test/Cmd.pm) perl(Test/Distribution.pm) perl(Test/More.pm) perl(Exporter.pm) perl(Encode.pm) perl(File/Temp.pm) perl(Pod/Wrap.pm) perl(Pod/Parser.pm)

%description
This module provides the heavy lifting needed by the podtidy utility
although the API should be general enough that it can be used directly.

podtidy processes a Pod document and attempts to tidy it's formatting.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*
%_bindir/*
%_man1dir/*

%changelog
* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 0.10-alt1
- initial build for ALT

