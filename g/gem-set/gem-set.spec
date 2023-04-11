%define        pkgname set

Name:          gem-%pkgname
Version:       1.0.3
Release:       alt1
Summary:       This library provides the Set class
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/set
Vcs:           https://github.com/ruby/set.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-test-unit
BuildRequires: gem-minitest >= 5.0
BuildRequires: gem-rake >= 12.0
Requires:      ruby-stdlibs
Provides:      gem(%pkgname) = 1.0.3

%description
This library provides the Set class, which deals with a collection of unordered
values with no duplicates. It is a hybrid of Array's intuitive inter-operation
facilities and Hash's fast lookup.

%package doc
Summary: Documentation for %name
Group: Documentation

%description doc
This library provides the Set class, which deals with a collection of unordered
values with no duplicates. It is a hybrid of Array's intuitive inter-operation
facilities and Hash's fast lookup. Set implements a collection of unordered
values with no duplicates. This is a hybrid of Array's intuitive inter-operation
facilities and Hash's fast lookup.

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
