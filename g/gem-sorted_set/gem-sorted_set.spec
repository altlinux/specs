%define        pkgname sorted_set

Name:          gem-%pkgname
Version:       1.0.3
Release:       alt1
Summary:       SortedSet for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/knu/sorted_set
Vcs:           https://github.com/knu/sorted_set.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-test-unit
BuildRequires: gem-rake >= 12.0
Requires:      ruby-stdlibs
Provides:      gem(%pkgname) = 1.0.3

%description
SortedSet implements a Set whose elements are sorted in ascending order
(according to the return values of their <=> methods) when iterating over them.

%package doc
Summary: Documentation for %name
Group: Documentation

%description doc
SortedSet implements a Set whose elements are sorted in ascending order
(according to the return values of their <=> methods) when iterating over them.
Every element in SortedSet must be mutually comparable to every other:
comparison with <=> must not return nil for any pair of elements.
Otherwise ArgumentError will be raised.
Currently this library does nothing for JRuby, as it has its own version of Set
and SortedSet.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Mon Apr 10 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
