%define        gemname jmespath

Name:          gem-jmespath
Version:       1.6.2
Release:       alt1
Summary:       Ruby implementation of JMESPath
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/jmespath/jmespath.rb
Vcs:           https://github.com/jmespath/jmespath.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(yard-sitemap) >= 1.0
BuildRequires: gem(rdiscount) >= 0
BuildRequires: gem(octokit) >= 0
BuildRequires: gem(absolute_time) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard-sitemap) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-jmespath
Provides:      ruby-jmespath
Provides:      gem(jmespath) = 1.6.2


%description
Ruby implementation of JMESPath.


%package       -n jmespath-rb
Version:       1.6.2
Release:       alt1
Summary:       Ruby implementation of JMESPath executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jmespath
Group:         Other
BuildArch:     noarch

Requires:      gem(jmespath) = 1.6.2

%description   -n jmespath-rb
Ruby implementation of JMESPath executable(s).

%description   -n jmespath-rb -l ru_RU.UTF-8
Исполнямка для самоцвета jmespath.


%package       -n gem-jmespath-doc
Version:       1.6.2
Release:       alt1
Summary:       Ruby implementation of JMESPath documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jmespath
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jmespath) = 1.6.2

%description   -n gem-jmespath-doc
Ruby implementation of JMESPath documentation files.

%description   -n gem-jmespath-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jmespath.


%package       -n gem-jmespath-devel
Version:       1.6.2
Release:       alt1
Summary:       Ruby implementation of JMESPath development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jmespath
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jmespath) = 1.6.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0
Requires:      gem(yard-sitemap) >= 1.0
Requires:      gem(rdiscount) >= 0
Requires:      gem(octokit) >= 0
Requires:      gem(absolute_time) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard-sitemap) >= 2

%description   -n gem-jmespath-devel
Ruby implementation of JMESPath development package.

%description   -n gem-jmespath-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jmespath.


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

%files         -n jmespath-rb
%_bindir/jmespath.rb

%files         -n gem-jmespath-doc
%ruby_gemdocdir

%files         -n gem-jmespath-devel


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.6.2-alt1
- ^ 1.4.0 -> 1.6.2

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2.1
- ! spec tags

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 31 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
