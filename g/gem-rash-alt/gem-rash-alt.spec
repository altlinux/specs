%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rash_alt

Name:          gem-rash-alt
Version:       0.4.12
Release:       alt1
Summary:       simple extension to Hashie::Mash for rubyified keys
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/shishi/rash_alt
Vcs:           https://github.com/shishi/rash_alt.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hashie) >= 3.4
BuildRequires: gem(rake) >= 13.0.3
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rspec) >= 3.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_alias_names rash_alt,rash-alt
Requires:      gem(hashie) >= 3.4
Provides:      gem(rash_alt) = 0.4.12

%description
simple extension to Hashie::Mash for rubyified keys, all keys are converted to
underscore to eliminate horrible camelCasing


%if_enabled    doc
%package       -n gem-rash-alt-doc
Version:       0.4.12
Release:       alt1
Summary:       simple extension to Hashie::Mash for rubyified keys documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rash_alt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rash_alt) = 0.4.12

%description   -n gem-rash-alt-doc
simple extension to Hashie::Mash for rubyified keys documentation files.

simple extension to Hashie::Mash for rubyified keys, all keys are converted to
underscore to eliminate horrible camelCasing

%description   -n gem-rash-alt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rash_alt.
%endif


%if_enabled    devel
%package       -n gem-rash-alt-devel
Version:       0.4.12
Release:       alt1
Summary:       simple extension to Hashie::Mash for rubyified keys development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rash_alt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rash_alt) = 0.4.12
Requires:      gem(rake) >= 13.0.3
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rspec) >= 3.4

%description   -n gem-rash-alt-devel
simple extension to Hashie::Mash for rubyified keys development package.

simple extension to Hashie::Mash for rubyified keys, all keys are converted to
underscore to eliminate horrible camelCasing

%description   -n gem-rash-alt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rash_alt.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rash-alt-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rash-alt-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Oct 15 2025 Pavel Skrylev <majioa@altlinux.org> 0.4.12-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
