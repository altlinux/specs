%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname nokogiri-diff

Name:          gem-nokogiri-diff
Version:       0.3.0
Release:       alt1
Summary:       Calculate the differences between two XML/HTML documents
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/nokogiri-diff#readme
Vcs:           https://github.com/postmodern/nokogiri-diff.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(nokogiri) >= 1.5
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(tdiff) >= 0.4
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(tdiff) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      ruby >= 2.0.0
Requires:      gem(nokogiri) >= 1.5
Requires:      gem(tdiff) >= 0.4
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(tdiff) >= 1
Provides:      gem(nokogiri-diff) = 0.3.0

%description
Nokogiri::Diff adds the ability to calculate the differences (added or removed
nodes) between two XML/HTML documents.


%if_enabled    doc
%package       -n gem-nokogiri-diff-doc
Version:       0.3.0
Release:       alt1
Summary:       Calculate the differences between two XML/HTML documents documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nokogiri-diff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(nokogiri-diff) = 0.3.0

%description   -n gem-nokogiri-diff-doc
Calculate the differences between two XML/HTML documents documentation
files.

Nokogiri::Diff adds the ability to calculate the differences (added or removed
nodes) between two XML/HTML documents.

%description   -n gem-nokogiri-diff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nokogiri-diff.
%endif


%if_enabled    devel
%package       -n gem-nokogiri-diff-devel
Version:       0.3.0
Release:       alt1
Summary:       Calculate the differences between two XML/HTML documents development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nokogiri-diff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(nokogiri-diff) = 0.3.0
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(kramdown) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yard) >= 1

%description   -n gem-nokogiri-diff-devel
Calculate the differences between two XML/HTML documents development
package.

Nokogiri::Diff adds the ability to calculate the differences (added or removed
nodes) between two XML/HTML documents.

%description   -n gem-nokogiri-diff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nokogiri-diff.
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
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-nokogiri-diff-doc
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-nokogiri-diff-devel
%doc ChangeLog.md LICENSE.txt README.md
%endif


%changelog
* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
