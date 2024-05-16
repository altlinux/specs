%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname silent_stream

Name:          gem-silent-stream
Version:       1.0.8
Release:       alt1
Summary:       ActiveSupport's Stream Silencing - Without ActiveSupport
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/silent_stream
Vcs:           https://github.com/pboling/silent_stream.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0.16
BuildRequires: gem(test-unit) >= 3.2
BuildRequires: gem(wwtd) >= 0
BuildRequires: gem(rubocop-gradual) >= 0.3.4
BuildRequires: gem(rubocop-lts) >= 10.1.1
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(standard) >= 1.33
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-minitest) >= 0
BuildConflicts: gem(rubocop-lts) >= 25
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-lts < 25
Provides:      gem(silent_stream) = 1.0.8


%description
ActiveSupport Kernel Reporting Detritus with a few enhancements


%if_enabled    doc
%package       -n gem-silent-stream-doc
Version:       1.0.8
Release:       alt1
Summary:       ActiveSupport's Stream Silencing - Without ActiveSupport documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета silent_stream
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(silent_stream) = 1.0.8

%description   -n gem-silent-stream-doc
ActiveSupport's Stream Silencing - Without ActiveSupport documentation
files.

ActiveSupport Kernel Reporting Detritus with a few enhancements
%description   -n gem-silent-stream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета silent_stream.
%endif


%if_enabled    devel
%package       -n gem-silent-stream-devel
Version:       1.0.8
Release:       alt1
Summary:       ActiveSupport's Stream Silencing - Without ActiveSupport development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета silent_stream
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(silent_stream) = 1.0.8
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0.16
Requires:      gem(test-unit) >= 3.2
Requires:      gem(wwtd) >= 0
Requires:      gem(rubocop-gradual) >= 0.3.4
Requires:      gem(rubocop-lts) >= 10.1.1
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(standard) >= 1.33
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-minitest) >= 0
Conflicts:     gem(rubocop-lts) >= 25
Conflicts:     gem(standard) >= 2

%description   -n gem-silent-stream-devel
ActiveSupport's Stream Silencing - Without ActiveSupport development
package.

ActiveSupport Kernel Reporting Detritus with a few enhancements
%description   -n gem-silent-stream-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета silent_stream.
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
%files         -n gem-silent-stream-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-silent-stream-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- + packaged gem with Ruby Policy 2.0
