%define        _unpackaged_files_terminate_build 1
%define        gemname tty-spinner

Name:          gem-tty-spinner
Version:       0.9.3
Release:       alt1
Summary:       A terminal spinner for tasks that have non-deterministic time frame
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org
Vcs:           https://github.com/piotrmurach/tty-spinner.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(pastel) >= 0.7.2
BuildRequires: gem(simplecov) >= 0.16.1
BuildRequires: gem(coveralls) >= 0.8.22
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(tty-cursor) >= 0.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(pastel) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(tty-cursor) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pastel >= 0.8,pastel < 1
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(tty-cursor) >= 0.7
Conflicts:     gem(tty-cursor) >= 1
Provides:      gem(tty-spinner) = 0.9.3


%description
A terminal spinner for tasks that have non-deterministic time frame.


%package       -n gem-tty-spinner-doc
Version:       0.9.3
Release:       alt1
Summary:       A terminal spinner for tasks that have non-deterministic time frame documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-spinner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-spinner) = 0.9.3

%description   -n gem-tty-spinner-doc
A terminal spinner for tasks that have non-deterministic time frame
documentation files.

%description   -n gem-tty-spinner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-spinner.


%package       -n gem-tty-spinner-devel
Version:       0.9.3
Release:       alt1
Summary:       A terminal spinner for tasks that have non-deterministic time frame development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tty-spinner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tty-spinner) = 0.9.3
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(pastel) >= 0.7.2
Requires:      gem(simplecov) >= 0.16.1
Requires:      gem(coveralls) >= 0.8.22
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(pastel) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(yardstick) >= 0.10

%description   -n gem-tty-spinner-devel
A terminal spinner for tasks that have non-deterministic time frame development
package.

%description   -n gem-tty-spinner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tty-spinner.


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

%files         -n gem-tty-spinner-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tty-spinner-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.3-alt1
- + packaged gem with Ruby Policy 2.0
