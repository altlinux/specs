%define        gemname jekyll-sass-converter

Name:          gem-jekyll-sass-converter
Version:       2.1.0
Release:       alt1.1
Summary:       A basic Sass converter for Jekyll
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll-sass-converter
Vcs:           https://github.com/jekyll/jekyll-sass-converter.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sassc) > 2.0.1 gem(sassc) < 3.0
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 0 gem(rspec) < 4
BuildRequires: gem(rubocop-jekyll) >= 0.4 gem(rubocop-jekyll) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(sassc) > 2.0.1 gem(sassc) < 3.0
Provides:      gem(jekyll-sass-converter) = 2.1.0


%description
A basic Sass converter for Jekyll.


%package       -n gem-jekyll-sass-converter-doc
Version:       2.1.0
Release:       alt1.1
Summary:       A basic Sass converter for Jekyll documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll-sass-converter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll-sass-converter) = 2.1.0

%description   -n gem-jekyll-sass-converter-doc
A basic Sass converter for Jekyll documentation files.

%description   -n gem-jekyll-sass-converter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll-sass-converter.


%package       -n gem-jekyll-sass-converter-devel
Version:       2.1.0
Release:       alt1.1
Summary:       A basic Sass converter for Jekyll development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll-sass-converter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll-sass-converter) = 2.1.0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 0 gem(rspec) < 4
Requires:      gem(rubocop-jekyll) >= 0.4 gem(rubocop-jekyll) < 1

%description   -n gem-jekyll-sass-converter-devel
A basic Sass converter for Jekyll development package.

%description   -n gem-jekyll-sass-converter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jekyll-sass-converter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-jekyll-sass-converter-doc
%ruby_gemdocdir

%files         -n gem-jekyll-sass-converter-devel


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.1.0-alt1
- initial build
