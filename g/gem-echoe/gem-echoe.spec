# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname echoe

Name:          gem-echoe
Version:       4.6.6.1
Release:       alt0.1
Summary:       A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment
License:       AFL
Group:         Development/Ruby
Url:           https://github.com/evan/echoe
Vcs:           https://github.com/evan/echoe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubyforge) >= 2.0.4
BuildRequires: gem(allison) >= 2.0.3
BuildRequires: gem(rdoc) >= 2.5.11
BuildRequires: gem(rake) >= 0.9.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubyforge) >= 2.0.4
Requires:      gem(allison) >= 2.0.3
Requires:      gem(rdoc) >= 2.5.11
Requires:      gem(rake) >= 0.9.2
Provides:      gem(echoe) = 4.6.6.1

%ruby_use_gem_version echoe:4.6.6.1

%description
A Rubygems packaging tool that provides Rake tasks for documentation, extension
compiling, testing, and deployment.


%package       -n gem-echoe-doc
Version:       4.6.6.1
Release:       alt0.1
Summary:       A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета echoe
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(echoe) = 4.6.6.1

%description   -n gem-echoe-doc
A Rubygems packaging tool that provides Rake tasks for documentation, extension
compiling, testing, and deployment documentation files.

%description   -n gem-echoe-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета echoe.


%package       -n gem-echoe-devel
Version:       4.6.6.1
Release:       alt0.1
Summary:       A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета echoe
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(echoe) = 4.6.6.1

%description   -n gem-echoe-devel
A Rubygems packaging tool that provides Rake tasks for documentation, extension
compiling, testing, and deployment development package.

%description   -n gem-echoe-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета echoe.


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

%files         -n gem-echoe-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-echoe-devel
%doc README.rdoc


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 4.6.6.1-alt0.1
- ^ 4.6.6 -> 4.6.6p1

* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 4.6.6-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
