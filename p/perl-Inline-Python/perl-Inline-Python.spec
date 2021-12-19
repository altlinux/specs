%define _unpackaged_files_terminate_build 1

Name:           perl-Inline-Python
Version:        0.56
Release:        alt2
Summary:        Write Perl subs and classes in Python
License:        GPL+ or Artistic
Group: 		Development/Perl
URL:            https://metacpan.org/release/Inline-Python
Source:        	%name-%version.tar

# patch found in Fedora:
#               Call Py_Initialize() before calling PyBytes_FromString()
#               Fixes segmentation fault with python 3.10
#               https://github.com/niner/inline-python-pm/pull/33
Patch0:         %{name}-pyinit.patch
# quick hack not to link with static library
Patch1: Inline-Python-0.56-use-shared-lib.patch


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
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README ToDo
%perl_vendorarch/auto/*
%perl_vendorarch/Inline*

%changelog
* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.56-alt2
- fixed build

* Tue May 11 2021 Alexandr Antonov <aas@altlinux.org> 0.56-alt1
- initial build for ALT
