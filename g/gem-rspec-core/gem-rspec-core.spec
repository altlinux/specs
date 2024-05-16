%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec-core

Name:          gem-rspec-core
Version:       3.13.0
Release:       alt1
Summary:       RSpec runner and formatters
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-core
Vcs:           https://github.com/rspec/rspec-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(cucumber) >= 1.3
BuildRequires: gem(minitest) >= 5.3
BuildRequires: gem(aruba) >= 0.14.9
BuildRequires: gem(coderay) >= 1.1.1
BuildRequires: gem(mocha) >= 0.13.0
BuildRequires: gem(rr) >= 1.0.4
BuildRequires: gem(flexmock) >= 0.9.0
BuildRequires: gem(thread_order) >= 1.1.0
BuildRequires: gem(rake) >= 13.0.0
BuildRequires: gem(diff-lcs) >= 1.4.3
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(yard) >= 0.9.24
BuildRequires: gem(thor) > 1.0.0
BuildRequires: gem(ffi) >= 1.15.0
BuildRequires: gem(childprocess) >= 3.0.0
BuildRequires: gem(simplecov) >= 0.8
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(rspec-support) >= 3.10.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(aruba) >= 0.15
BuildConflicts: gem(coderay) >= 1.2
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(flexmock) >= 0.10
BuildConflicts: gem(thread_order) >= 1.2
BuildConflicts: gem(diff-lcs) >= 2
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(rspec-support) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec-support >= 3.10.2,rspec-support < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency rr >= 3.0.4,rr < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
Requires:      gem(rspec-support) >= 3.10.2
Conflicts:     gem(rspec-support) >= 4
Obsoletes:     ruby-rspec-core < %EVR
Provides:      ruby-rspec-core = %EVR
Provides:      gem(rspec-core) = 3.13.0


%description
rspec-core provides the structure for writing executable examples of how your
code should behave, and an rspec command with tools to constrain which examples
get run and tailor the output.


%package       -n rspec
Version:       3.13.0
Release:       alt1
Summary:       RSpec runner and formatters executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-core
Group:         Other
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.0

%description   -n rspec
RSpec runner and formatters executable(s).

rspec-core provides the structure for writing executable examples of how your
code should behave, and an rspec command with tools to constrain which examples
get run and tailor the output.
%description   -n rspec -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-core.


%if_enabled    doc
%package       -n gem-rspec-core-doc
Version:       3.13.0
Release:       alt1
Summary:       RSpec runner and formatters documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.0

%description   -n gem-rspec-core-doc
RSpec runner and formatters documentation files.

rspec-core provides the structure for writing executable examples of how your
code should behave, and an rspec command with tools to constrain which examples
get run and tailor the output.
%description   -n gem-rspec-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-core.
%endif


%if_enabled    devel
%package       -n gem-rspec-core-devel
Version:       3.13.0
Release:       alt1
Summary:       RSpec runner and formatters development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.0
Requires:      gem(cucumber) >= 1.3
Requires:      gem(minitest) >= 5.3
Requires:      gem(aruba) >= 0.14.9
Requires:      gem(coderay) >= 1.1.1
Requires:      gem(mocha) >= 0.13.0
Requires:      gem(rr) >= 1.0.4
Requires:      gem(flexmock) >= 0.9.0
Requires:      gem(thread_order) >= 1.1.0
Requires:      gem(rake) >= 13.0.0
Requires:      gem(diff-lcs) >= 1.4.3
Requires:      gem(redcarpet) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(yard) >= 0.9.24
Requires:      gem(thor) > 1.0.0
Requires:      gem(ffi) >= 1.15.0
Requires:      gem(childprocess) >= 3.0.0
Requires:      gem(jruby-openssl) >= 0
Requires:      gem(simplecov) >= 0.8
Requires:      gem(test-unit) >= 3.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(aruba) >= 0.15
Conflicts:     gem(coderay) >= 1.2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rr) >= 4
Conflicts:     gem(flexmock) >= 0.10
Conflicts:     gem(thread_order) >= 1.2
Conflicts:     gem(diff-lcs) >= 2
Conflicts:     gem(yard) >= 1
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(test-unit) >= 4

%description   -n gem-rspec-core-devel
RSpec runner and formatters development package.

rspec-core provides the structure for writing executable examples of how your
code should behave, and an rspec command with tools to constrain which examples
get run and tailor the output.
%description   -n gem-rspec-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-core.
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

%files         -n rspec
%doc README.md
%_bindir/rspec

%if_enabled    doc
%files         -n gem-rspec-core-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-core-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.10.1 -> 3.13.0

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.1-alt1
- ^ 3.8.0 -> 3.10.1

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- > Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2
- Rebuild with mocha 1.5.0.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Package rspec executable

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for ALT Linux
