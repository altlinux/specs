%define        gemname hashdiff

Name:          gem-hashdiff
Version:       1.0.1
Release:       alt1.1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/liufengyun/hashdiff
Vcs:           https://github.com/liufengyun/hashdiff.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bluecloth) >= 0
BuildRequires: gem(rspec) >= 2.0
BuildRequires: gem(rubocop) >= 0.49.1
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(hashdiff) = 1.0.1


%description
Hashdiff is a ruby library to compute the smallest difference between two
hashes.

It also supports comparing two arrays.

Hashdiff does not monkey-patch any existing class. All features are contained
inside the Hashdiff module.


%package       -n gem-hashdiff-doc
Version:       1.0.1
Release:       alt1.1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hashdiff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hashdiff) = 1.0.1

%description   -n gem-hashdiff-doc
HashDiff is a ruby library to to compute the smallest difference between two
hashes documentation files.

%description   -n gem-hashdiff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hashdiff.


%package       -n gem-hashdiff-devel
Version:       1.0.1
Release:       alt1.1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hashdiff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hashdiff) = 1.0.1
Requires:      gem(bluecloth) >= 0
Requires:      gem(rspec) >= 2.0
Requires:      gem(rubocop) >= 0.49.1
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rake) >= 14

%description   -n gem-hashdiff-devel
HashDiff is a ruby library to to compute the smallest difference between two
hashes development package.

%description   -n gem-hashdiff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hashdiff.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md spec/hashdiff/readme_spec.rb
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hashdiff-doc
%doc README.md spec/hashdiff/readme_spec.rb
%ruby_gemdocdir

%files         -n gem-hashdiff-devel
%doc README.md spec/hashdiff/readme_spec.rb


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- ! closes build reqs under check condition

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.4.0 -> 1.0.1

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
