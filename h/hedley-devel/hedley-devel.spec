%define        _unpackaged_files_terminate_build 1
%define        nomen hedley

%def_enable    check

Name:          %nomen-devel
Version:       15
Release:       alt1
Group:         Development/C++
Summary:       A C/C++ header to help move #ifdefs out of your code
License:       CC0-1.0 license
Url:           https://nemequ.github.io/hedley/
Vcs:           https://github.com/nemequ/hedley.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires: gcc-c++

%description
A C/C++ header to help move #ifdefs out of your code

Hedley is C/C++ a header file designed to smooth over some platform-specific
annoyances. The idea is to get rid of a bunch of the #ifdefs in your code and
put them in Hedley instead or, if you haven't bothered with platform-specific
functionality in your code, to make it easier to do so. This code can be used to
improve:

* Static analysis - better warnings and errors help you catch errors before they
  become a real issue.
* Optimizations - compiler hints help speed up your code.
* Manage public APIs
 * Visibility - keeping internal symbols private can make your program faster
   and smaller.
 * Versioning - help consumers avoid functions which are deprecated or too new
   for all the platforms they want to support.
* C/C++ interoperability - make it easier to use code in both C and C++
  compilers.
* and more!

You can safely use Hedley in your public API. If someone else includes a newer
version of Hedley later on, the newer Hedley will just redefine everything, and
if someone includes an older version it will simply be ignored.

It should be safe to use any of Hedley's features; if the platform doesn't
support the feature it will be silently ignored.


%prep
%setup

%install
%make
%__install -D -m 644 %nomen.h %buildroot%_includedir/%nomen.h
%__install -D -m 644 %{nomen}_undef.h %buildroot%_includedir/%{nomen}_undef.h

%check
cd test
%make
find . -type f -executable -exec {} \;

%files
%doc README.md
%_includedir/%{nomen}*.h


%changelog
* Thu Jul 10 2025 Pavel Skrylev <majioa@altlinux.org> 15-alt1
- Initial build for Sisyphus
