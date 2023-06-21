%define        _unpackaged_files_terminate_build 1
%define        gemname backport

Name:          gem-backport
Version:       1.2.0
Release:       alt1
Summary:       A pure Ruby library for event-driven IO
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/castwide/backport
Vcs:           https://github.com/castwide/backport.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.14
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(backport) = 1.2.0


%description
A pure Ruby library for event-driven IO


%package       -n gem-backport-doc
Version:       1.2.0
Release:       alt1
Summary:       A pure Ruby library for event-driven IO documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета backport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(backport) = 1.2.0

%description   -n gem-backport-doc
A pure Ruby library for event-driven IO documentation files.

%description   -n gem-backport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета backport.


%package       -n gem-backport-devel
Version:       1.2.0
Release:       alt1
Summary:       A pure Ruby library for event-driven IO development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета backport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(backport) = 1.2.0
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.14
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-backport-devel
A pure Ruby library for event-driven IO development package.

%description   -n gem-backport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета backport.


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

%files         -n gem-backport-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-backport-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
