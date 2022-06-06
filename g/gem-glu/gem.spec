%define        gemname glu

Name:          gem-glu
Version:       8.3.0
Release:       alt1
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation
License:       MIT
Group:         Development/Ruby
Url:           https://rubygems.org/gems/glu
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rake-compiler) >= 1.0 gem(rake-compiler) < 2
BuildRequires: gem(rake-compiler-dock) >= 0.6.0 gem(rake-compiler-dock) < 2
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.16 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rake-compiler-dock >= 1.1.0,rake-compiler-dock < 2
Provides:      gem(glu) = 8.3.0


%description
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation.


%package       -n gem-glu-doc
Version:       8.3.0
Release:       alt1
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета glu
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(glu) = 8.3.0

%description   -n gem-glu-doc
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation documentation files.

%description   -n gem-glu-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета glu.


%package       -n gem-glu-devel
Version:       8.3.0
Release:       alt1
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета glu
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(glu) = 8.3.0
Requires:      gem(rdoc) >= 4.0

%description   -n gem-glu-devel
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation development package.

%description   -n gem-glu-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета glu.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-glu-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-glu-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 8.3.0-alt1
- + packaged gem with Ruby Policy 2.0
