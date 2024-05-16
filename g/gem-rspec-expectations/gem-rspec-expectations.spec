%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec-expectations

Name:          gem-rspec-expectations
Version:       3.13.0
Release:       alt1
Summary:       Provides a readable API to express expected outcomes of a code example
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-expectations
Vcs:           https://github.com/rspec/rspec-expectations.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(aruba) >= 0.14.10
BuildRequires: gem(cucumber) >= 1.3
BuildRequires: gem(minitest) >= 5.2
BuildRequires: gem(rake) > 10.0.0
BuildRequires: gem(diff-lcs) >= 1.4.3
BuildRequires: gem(coderay) >= 0
BuildRequires: gem(yard) >= 0.9.24
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(ffi) > 1.9.24
BuildRequires: gem(childprocess) > 1.0.0
BuildRequires: gem(thor) > 1.0.0
BuildRequires: gem(rspec-support) >= 3.10.2
BuildConflicts: gem(aruba) >= 0.15
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(diff-lcs) >= 2.0
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rspec-support) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec-support >= 3.10.2,rspec-support < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(diff-lcs) >= 1.4.3
Requires:      gem(rspec-support) >= 3.10.2
Conflicts:     gem(diff-lcs) >= 2.0
Conflicts:     gem(rspec-support) >= 4
Obsoletes:     ruby-rspec-expectations < %EVR
Provides:      ruby-rspec-expectations = %EVR
Provides:      gem(rspec-expectations) = 3.13.0


%description
RSpec::Expectations lets you express expected outcomes on an object in an
example.


%if_enabled    doc
%package       -n gem-rspec-expectations-doc
Version:       3.13.0
Release:       alt1
Summary:       Provides a readable API to express expected outcomes of a code example documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-expectations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.13.0

%description   -n gem-rspec-expectations-doc
Provides a readable API to express expected outcomes of a code example
documentation files.

%description   -n gem-rspec-expectations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-expectations.
%endif


%if_enabled    devel
%package       -n gem-rspec-expectations-devel
Version:       3.13.0
Release:       alt1
Summary:       Provides a readable API to express expected outcomes of a code example development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-expectations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.13.0
Requires:      gem(aruba) >= 0.14.10
Requires:      gem(cucumber) >= 1.3
Requires:      gem(minitest) >= 5.2
Requires:      gem(rake) > 10.0.0
Requires:      gem(coderay) >= 0
Requires:      gem(yard) >= 0.9.24
Requires:      gem(redcarpet) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(ffi) > 1.9.24
Requires:      gem(childprocess) > 1.0.0
Requires:      gem(thor) > 1.0.0
Requires:      gem(jruby-openssl) >= 0
Conflicts:     gem(aruba) >= 0.15
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(yard) >= 1
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rspec-expectations-devel
Provides a readable API to express expected outcomes of a code example
development package.

%description   -n gem-rspec-expectations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-expectations.
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
%files         -n gem-rspec-expectations-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-expectations-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.10.1 -> 3.13.0

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.1-alt1
- ^ 3.8.2 -> 3.10.1

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.2-alt2
- Use Ruby Policy 2.0.

* Wed Oct 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for ALT Linux
