%define        gemname ruby2_keywords

Name:          gem-ruby2-keywords
Version:       0.0.4
Release:       alt1
Summary:       Shim library for Module#ruby2_keywords
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/ruby2_keywords
Vcs:           https://github.com/ruby/ruby2_keywords.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names ruby2_keywords,ruby2-keywords
Provides:      gem(ruby2_keywords) = 0.0.4


%description
Provides empty Module#ruby2_keywords method, for the forward source-level
compatibility against ruby2.7 and ruby3.


%package       -n gem-ruby2-keywords-doc
Version:       0.0.4
Release:       alt1
Summary:       Shim library for Module#ruby2_keywords documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby2_keywords
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby2_keywords) = 0.0.4

%description   -n gem-ruby2-keywords-doc
Shim library for Module#ruby2_keywords documentation files.

Provides empty Module#ruby2_keywords method, for the forward source-level
compatibility against ruby2.7 and ruby3.

%description   -n gem-ruby2-keywords-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby2_keywords.


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

%files         -n gem-ruby2-keywords-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- ^ 0.0.2 -> 0.0.4

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- + packaged gem with usage Ruby Policy 2.0
