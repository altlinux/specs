%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec-mocks

Name:          gem-rspec-mocks
Version:       3.13.0
Release:       alt1
Summary:       RSpec's 'test double' framework, with support for stubbing and mocking
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-mocks
Vcs:           https://github.com/rspec/rspec-mocks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(cucumber) >= 1.3
BuildRequires: gem(aruba) >= 1.1.0
BuildRequires: gem(minitest) >= 5.2
BuildRequires: gem(rake) > 12.3.2
BuildRequires: gem(diff-lcs) >= 1.4.3
BuildRequires: gem(yard) >= 0.9.24
BuildRequires: gem(ffi) >= 1.15.0
BuildRequires: gem(childprocess) >= 3.0.0
BuildRequires: gem(thor) > 1.0.0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(simplecov) >= 0.8
BuildRequires: gem(rspec-support) >= 3.10.2
BuildConflicts: gem(aruba) >= 3.0.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(diff-lcs) >= 2.0
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rspec-support) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec-support >= 3.10.2,rspec-support < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
Requires:      gem(diff-lcs) >= 1.4.3
Requires:      gem(rspec-support) >= 3.10.2
Conflicts:     gem(diff-lcs) >= 2.0
Conflicts:     gem(rspec-support) >= 4
Obsoletes:     ruby-rspec-mocks < %EVR
Provides:      ruby-rspec-mocks = %EVR
Provides:      gem(rspec-mocks) = 3.13.0


%description
rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.


%if_enabled    doc
%package       -n gem-rspec-mocks-doc
Version:       3.13.0
Release:       alt1
Summary:       RSpec's 'test double' framework, with support for stubbing and mocking documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-mocks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.13.0

%description   -n gem-rspec-mocks-doc
RSpec's 'test double' framework, with support for stubbing and mocking
documentation files.

rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.
%description   -n gem-rspec-mocks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-mocks.
%endif


%if_enabled    devel
%package       -n gem-rspec-mocks-devel
Version:       3.13.0
Release:       alt1
Summary:       RSpec's 'test double' framework, with support for stubbing and mocking development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-mocks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.13.0
Requires:      gem(cucumber) >= 1.3
Requires:      gem(aruba) >= 1.1.0
Requires:      gem(minitest) >= 5.2
Requires:      gem(rake) > 12.3.2
Requires:      gem(yard) >= 0.9.24
Requires:      gem(ffi) >= 1.15.0
Requires:      gem(childprocess) >= 3.0.0
Requires:      gem(thor) > 1.0.0
Requires:      gem(redcarpet) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(simplecov) >= 0.8
Requires:      gem(jruby-openssl) >= 0
Conflicts:     gem(aruba) >= 3.0.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(yard) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-rspec-mocks-devel
RSpec's 'test double' framework, with support for stubbing and mocking
development package.

rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.
%description   -n gem-rspec-mocks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-mocks.
%endif


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

%if_enabled    doc
%files         -n gem-rspec-mocks-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-mocks-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.10.2 -> 3.13.0

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.2-alt1
- ^ 3.8.0 -> 3.10.2

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for ALT Linux
