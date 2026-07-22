%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname super_diff

Name:          gem-super-diff
Version:       0.19.0
Release:       alt1
Summary:       A better way to view differences between complex data structures in RSpec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/splitwise/super_diff
Vcs:           https://github.com/splitwise/super_diff.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4.1
BuildRequires: gem(attr_extras) >= 6.2.4
BuildRequires: gem(bundler-audit) >= 0
BuildRequires: gem(childprocess) >= 0
BuildRequires: gem(climate_control) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(diff-lcs) >= 1.5
BuildRequires: gem(patience_diff) >= 1.2
BuildRequires: gem(prettier_print) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(attr_extras) >= 8
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(patience_diff) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.1,appraisal < 3
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
%ruby_alias_names super_diff,super-diff
Requires:      ruby >= 3.1
Requires:      gem(appraisal) >= 2.4.1
Requires:      gem(attr_extras) >= 6.2.4
Requires:      gem(bundler-audit) >= 0
Requires:      gem(childprocess) >= 0
Requires:      gem(climate_control) >= 0
Requires:      gem(debug) >= 0
Requires:      gem(diff-lcs) >= 1.5
Requires:      gem(patience_diff) >= 1.2
Requires:      gem(prettier_print) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(attr_extras) >= 8
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(patience_diff) >= 2
Provides:      gem(super_diff) = 0.19.0

%description
SuperDiff is a gem that hooks into RSpec to intelligently display the
differences between two data structures of any type.


%if_enabled    doc
%package       -n gem-super-diff-doc
Version:       0.19.0
Release:       alt1
Summary:       A better way to view differences between complex data structures in RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета super_diff
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(super_diff) = 0.19.0

%description   -n gem-super-diff-doc
A better way to view differences between complex data structures in RSpec
documentation files.

SuperDiff is a gem that hooks into RSpec to intelligently display the
differences between two data structures of any type.

%description   -n gem-super-diff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета super_diff.
%endif


%if_enabled    devel
%package       -n gem-super-diff-devel
Version:       0.19.0
Release:       alt1
Summary:       A better way to view differences between complex data structures in RSpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета super_diff
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(super_diff) = 0.19.0

%description   -n gem-super-diff-devel
A better way to view differences between complex data structures in RSpec
development package.

SuperDiff is a gem that hooks into RSpec to intelligently display the
differences between two data structures of any type.

%description   -n gem-super-diff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета super_diff.
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
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-super-diff-doc
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-super-diff-devel
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 0.19.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
