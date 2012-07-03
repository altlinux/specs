
Name: libre2-devel-static
Version: 0.0.1
Release: alt1
Summary: Regular expressions processing library for C++ programs developed by Google Inc
License: DSD
Group: Development/C++
URL: http://code.google.com/p/re2

Source: re2-%version.tar.gz

Patch1: re2-0.0.1-alt-install.patch

Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Fri Mar 12 2010
BuildRequires: gcc-c++

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.  Backtracking engines are typically full
of features and convenient syntactic sugar but can be forced into
taking exponential amounts of time on even small inputs. RE2 uses
automata theory to guarantee that regular expression searches run in
time linear in the size of the input. RE2 implements memory limits, so
that searches can be constrained to a fixed amount of memory. RE2 is
engineered to use a small fixed C++ stack footprint no matter what
inputs or regular expressions it must process; thus RE2 is useful in
multithreaded environments where thread stacks cannot grow arbitrarily
large.

%prep
%setup -q -n re2-%version
%patch1 -p1
%build
make
make test

%install
make prefix=%buildroot%prefix libdir=%buildroot%_libdir install

%files
%doc AUTHORS CONTRIBUTORS doc LICENSE README
%_libdir/*
%_includedir/*

%changelog
* Fri Mar 12 2010 Michael Pozhidaev <msp@altlinux.ru> 0.0.1-alt1
- First ALT Linux release

