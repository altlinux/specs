%define        gemname shoulda-matchers

Name:          gem-shoulda-matchers
Version:       4.5.1
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality
License:       MIT
Group:         Development/Ruby
Url:           https://matchers.shoulda.io/
Vcs:           https://github.com/thoughtbot/shoulda-matchers.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 4.2.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 4.2.0
Provides:      gem(shoulda-matchers) = 4.5.1


%description
Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.


%package       -n gem-shoulda-matchers-doc
Version:       4.5.1
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shoulda-matchers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shoulda-matchers) = 4.5.1

%description   -n gem-shoulda-matchers-doc
Simple one-liner tests for common Rails functionality documentation
files.

Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.

%description   -n gem-shoulda-matchers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shoulda-matchers.


%package       -n gem-shoulda-matchers-devel
Version:       4.5.1
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shoulda-matchers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shoulda-matchers) = 4.5.1

%description   -n gem-shoulda-matchers-devel
Simple one-liner tests for common Rails functionality development
package.

Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.

%description   -n gem-shoulda-matchers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shoulda-matchers.


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

%files         -n gem-shoulda-matchers-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-shoulda-matchers-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 4.5.1-alt1
- + packaged gem with Ruby Policy 2.0
