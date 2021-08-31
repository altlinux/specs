%define        gemname hoe-rubygems

Name:          gem-hoe-rubygems
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin with additional RubyGems tasks
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jbarnette/hoe-rubygems
Vcs:           https://github.com/jbarnette/hoe-rubygems.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(hoe-rubygems) = 1.0.0


%description
A Hoe plugin with additional RubyGems tasks. Provides support for generating
gemspec files and installing with a prefix.


%package       -n gem-hoe-rubygems-doc
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin with additional RubyGems tasks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-rubygems
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-rubygems) = 1.0.0

%description   -n gem-hoe-rubygems-doc
A Hoe plugin with additional RubyGems tasks documentation files.

A Hoe plugin with additional RubyGems tasks. Provides support for generating
gemspec files and installing with a prefix.

%description   -n gem-hoe-rubygems-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-rubygems.


%package       -n gem-hoe-rubygems-devel
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin with additional RubyGems tasks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-rubygems
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-rubygems) = 1.0.0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-hoe-rubygems-devel
A Hoe plugin with additional RubyGems tasks development package.

A Hoe plugin with additional RubyGems tasks. Provides support for generating
gemspec files and installing with a prefix.

%description   -n gem-hoe-rubygems-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-rubygems.


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

%files         -n gem-hoe-rubygems-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-rubygems-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
