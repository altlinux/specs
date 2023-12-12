%define        _unpackaged_files_terminate_build 1
%define        gemname gyoku

Name:          gem-gyoku
Version:       1.4.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/gyoku
Vcs:           https://github.com/savonrb/gyoku.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(rexml) >= 3.0
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(builder) >= 2.1.2
Requires:      gem(rexml) >= 3.0
Conflicts:     gem(rexml) >= 4
Provides:      gem(gyoku) = 1.4.0


%description
Translates Ruby Hashes to XML.


%package       -n gem-gyoku-doc
Version:       1.4.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gyoku
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gyoku) = 1.4.0

%description   -n gem-gyoku-doc
Translates Ruby Hashes to XML documentation files.

%description   -n gem-gyoku-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gyoku.


%package       -n gem-gyoku-devel
Version:       1.4.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gyoku
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gyoku) = 1.4.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0

%description   -n gem-gyoku-devel
Translates Ruby Hashes to XML development package.

%description   -n gem-gyoku-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gyoku.


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

%files         -n gem-gyoku-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gyoku-devel
%doc README.md


%changelog
* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.1 -> 1.4.0

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1.1
- ! spec tags

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
