%define _unpackaged_files_terminate_build 1

Name:           perl-Inline-Python
Version:        0.57
Release:        alt1
Summary:        Write Perl subs and classes in Python
License:        GPLv2+ or Artistic-2.0
Group: 		Development/Perl
URL:            https://metacpan.org/release/Inline-Python
VCS:            git+https://github.com/niner/inline-python-pm
Source:        	%name-%version.tar

# quick hack not to link with static library
Patch1: Inline-Python-0.56-use-shared-lib.patch

BuildRequires: chrpath
BuildRequires: python3-devel perl(ExtUtils/MakeMaker.pm) perl(Inline.pm) perl(Test/Number/Delta.pm) perl(Test/Deep.pm) perl(Test/More.pm)
Requires: perl(Inline.pm)

%description
The Inline::Python module allows you to put Python source code directly
"inline" in a Perl script or module. It sets up an in-process Python
interpreter, runs your code, and then examines Python's symbol table for
things to bind to Perl. The process of interrogating the Python interpreter
for global variables only occurs the first time you run your Python code. The
name-space is cached, and subsequent calls use the cached version.

%prep
%setup
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

chrpath -d %buildroot%perl_vendorarch/auto/*/*/*.so

%files
%doc Changes README ToDo
%perl_vendorarch/auto/*
%perl_vendorarch/Inline*

%changelog
* Fri Sep 30 2022 Igor Vlasenko <viy@altlinux.org> 0.57-alt1
- new version

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.56-alt3
- added VCS: tag

* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.56-alt2
- fixed build

* Tue May 11 2021 Alexandr Antonov <aas@altlinux.org> 0.56-alt1
- initial build for ALT
