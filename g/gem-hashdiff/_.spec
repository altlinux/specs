%define        gemname hashdiff

Name:          gem-hashdiff
Version:       1.0.1
Release:       alt1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/liufengyun/hashdiff
Vcs:           https://github.com/liufengyun/hashdiff.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(bluecloth) >= 0
BuildRequires: gem(rspec) >= 2.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.49.1 gem(rubocop) < 2
BuildRequires: gem(rubocop-rspec) >= 0 gem(rubocop-rspec) < 3
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
Provides:      gem(hashdiff) = 1.0.1


%description
Hashdiff is a ruby library to compute the smallest difference between two
hashes.

It also supports comparing two arrays.

Hashdiff does not monkey-patch any existing class. All features are contained
inside the Hashdiff module.


%package       -n gem-hashdiff-doc
Version:       1.0.1
Release:       alt1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hashdiff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hashdiff) = 1.0.1

%description   -n gem-hashdiff-doc
HashDiff is a ruby library to to compute the smallest difference between two
hashes documentation files.

Hashdiff is a ruby library to compute the smallest difference between two
hashes.

It also supports comparing two arrays.

Hashdiff does not monkey-patch any existing class. All features are contained
inside the Hashdiff module.

%description   -n gem-hashdiff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hashdiff.


%package       -n gem-hashdiff-devel
Version:       1.0.1
Release:       alt1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hashdiff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hashdiff) = 1.0.1
# Requires:      gem(bluecloth) >= 0
Requires:      gem(rspec) >= 2.0 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.49.1 gem(rubocop) < 2
Requires:      gem(rubocop-rspec) >= 0 gem(rubocop-rspec) < 3
Requires:      gem(yard) >= 0

%description   -n gem-hashdiff-devel
HashDiff is a ruby library to to compute the smallest difference between two
hashes development package.

Hashdiff is a ruby library to compute the smallest difference between two
hashes.

It also supports comparing two arrays.

Hashdiff does not monkey-patch any existing class. All features are contained
inside the Hashdiff module.

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
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.4.0 -> 1.0.1

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
